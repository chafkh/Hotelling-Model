import pygame
import random
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import tkinter as tk
from tkinter import simpledialog

class Policy:
    def __init__(self, space_size):
        self.q_table1_agent1 = np.zeros(space_size)
        self.q_table2_agent1 = np.zeros(space_size)
        self.q_table1_agent2 = np.zeros(space_size)
        self.q_table2_agent2 = np.zeros(space_size)

    def update_q_table(self, q_table1, q_table2, current_state, next_state, reward, learning_rate, discount_factor):
        current_state %= len(q_table1)
        next_state %= len(q_table1)
        if random.choice([True, False]):
            best_action = np.argmax(q_table1[next_state])
            q_table1[current_state] = ((1 - learning_rate) * q_table1[current_state] +
                                       learning_rate * (reward + discount_factor * q_table2[best_action]))
        else:
            best_action = np.argmax(q_table2[next_state])
            q_table2[current_state] = ((1 - learning_rate) * q_table2[current_state] +
                                       learning_rate * (reward + discount_factor * q_table1[best_action]))
