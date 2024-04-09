import pygame
import random
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import tkinter as tk
from tkinter import simpledialog
from buffer import Buffer
from policy import Policy

class Trainer:
    def __init__(self, num_agents, space_size, learning_rate, discount_factor, exploration_decay, num_random_consumers, laziness_enabled=False, laziness_threshold=50):
        self.buffer = Buffer(space_size, num_random_consumers)
        self.policy = Policy(space_size)
        self.num_agents = num_agents
        self.space_size = space_size
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_prob = 1.0
        self.exploration_decay = exploration_decay
        self.max_episodes = 8000
        self.laziness_enabled = laziness_enabled
        self.laziness_threshold = laziness_threshold
        self.init_pygame()

    def init_pygame(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Hotelling's Spatial Competition")

    def consumer_preference(self, agent_positions):
        rewards = [0, 0]
        for consumer_location in self.buffer.random_consumer_locations:
            distances = [abs(consumer_location - pos) for pos in agent_positions]
            if self.laziness_enabled and min(distances) > self.laziness_threshold:
                continue
            closest_agent = distances.index(min(distances))
            rewards[closest_agent] += 1
        return rewards

    def run_simulation(self):
        running = True
        episode = 0
        convergence_data = []
        font = pygame.font.Font(None, 36)
        while running and episode < self.max_episodes:
            initial_positions = [self.space_size // 2 for _ in range(self.num_agents)]
            agent_positions = initial_positions.copy()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            for agent_index in range(self.num_agents):
                i = (episode + agent_index) % self.num_agents
                if random.uniform(0, 1) < self.exploration_prob:
                    action = random.randint(0, self.space_size - 1)
                else:
                    action = np.argmax(self.policy.q_table1_agent1 if i == 0 else self.policy.q_table1_agent2)
                agent_positions[i] = action

            rewards = self.consumer_preference(agent_positions)
            for agent_index in range(self.num_agents):
                current_state = agent_positions[agent_index]
                next_state = (current_state + random.choice([-1, 1])) % self.space_size
                if agent_index == 0:
                    self.policy.update_q_table(self.policy.q_table1_agent1, self.policy.q_table2_agent1, 
                                               current_state, next_state, rewards[agent_index], 
                                               self.learning_rate, self.discount_factor)
                else:
                    self.policy.update_q_table(self.policy.q_table1_agent2, self.policy.q_table2_agent2, 
                                               current_state, next_state, rewards[agent_index], 
                                               self.learning_rate, self.discount_factor)

            self.screen.fill((255, 255, 255))
            for consumer_location in self.buffer.random_consumer_locations:
                color = (0, 255, 0)
                if self.laziness_enabled and min([abs(consumer_location - pos) for pos in agent_positions]) > self.laziness_threshold:
                    color = (255, 255, 0)
                pygame.draw.circle(self.screen, color, (int(800 * consumer_location / self.space_size), 300), 5)
            for i, pos in enumerate(agent_positions):
                color = (0, 0, 255) if i == 0 else (255, 0, 0)
                pygame.draw.circle(self.screen, color, (int(800 * pos / self.space_size), 300), 10)
            info_text = [
                f'Episode: {episode}',
                f'Agents number: {self.num_agents}',
                f'Windows space: {self.space_size}',
                f'Learning rate: {self.learning_rate}',
                f'Discount factor: {self.discount_factor}',
                f'Exploration decay: {self.exploration_prob:.4f}',
                f'Number of consumers: {len(self.buffer.random_consumer_locations)}',
                'Laziness activated' if self.laziness_enabled else 'Laziness disactivated'
            ]
            for i, line in enumerate(info_text):
                text_surface = font.render(line, True, (0, 0, 0))
                self.screen.blit(text_surface, (10, 10 + 20 * i))

            pygame.display.flip()
            episode += 1

            convergence_data.append(np.mean(agent_positions))
            self.exploration_prob *= self.exploration_decay

        # Génération et affichage du graphique en bas à gauche après l'exécution
        plt.figure(figsize=(5, 3))
        plt.plot(convergence_data, label='Average Agent Position')
        plt.xlabel('Episode')
        plt.ylabel('Average Position')
        plt.title('Agent Convergence Over Time')
        plt.legend()
        plt.grid(True)
        image_path = os.path.join(os.getcwd(), 'convergence_figure.png')
        plt.savefig(image_path)
        plt.close()
        graph_image = pygame.image.load(image_path)
        self.screen.blit(graph_image, (10, 250))  # Position en bas à gauche
        pygame.display.flip()

        # Boucle d'attente pour la fermeture de Pygame
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()
