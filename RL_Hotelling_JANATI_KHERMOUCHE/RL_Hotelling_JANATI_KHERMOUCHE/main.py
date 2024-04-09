import tkinter as tk
from tkinter import simpledialog
from buffer import Buffer
from policy import Policy
from trainer import Trainer

class Main:
    def __init__(self):
        self.competition = None

    def get_parameters(self):
        # Création d'une fenêtre Tkinter pour les paramètres d'entrée
        root = tk.Tk()
        root.withdraw()  # Cache la fenêtre Tkinter principale

        # Demande à l'utilisateur d'entrer les paramètres
        laziness_enabled = simpledialog.askstring("Parameters", "Activate the laziness of the consumers? (Yes/No):", parent=root) == "Yes"
        num_agents = simpledialog.askinteger("Parameters", "Number of agents:", parent=root, minvalue=1, maxvalue=10)
        space_size = simpledialog.askinteger("Parameters", "Space size (put 250 for optimality):", parent=root, minvalue=100, maxvalue=1000)
        learning_rate = simpledialog.askfloat("Parameters", "Learning rate (like 0.80, with a dot):", parent=root, minvalue=0.0, maxvalue=1.0)
        discount_factor = simpledialog.askfloat("Parameters", "Discount factor (with a dot):", parent=root, minvalue=0.0, maxvalue=1.0)
        exploration_decay = simpledialog.askfloat("Parameters", "Exploration decay (with a dot):", parent=root, minvalue=0.0, maxvalue=1.0)
        num_random_consumers = simpledialog.askinteger("Parameters", "Number of random consumers:", parent=root, minvalue=100, maxvalue=10000)

        # Création d'un objet Trainer avec les paramètres spécifiés
        self.competition = Trainer(num_agents, space_size, learning_rate, discount_factor, exploration_decay, num_random_consumers, laziness_enabled)

    def start(self):
        # Lance la méthode pour obtenir les paramètres et démarre la simulation
        self.get_parameters()
        if self.competition:
            self.competition.run_simulation()

if __name__ == "__main__":
    main = Main()
    main.start()
