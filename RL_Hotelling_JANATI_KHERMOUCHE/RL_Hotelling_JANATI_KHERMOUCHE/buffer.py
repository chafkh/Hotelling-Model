import pygame
import random
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import tkinter as tk
from tkinter import simpledialog

class Buffer:
    def __init__(self, space_size, num_random_consumers):
        self.random_consumer_locations = [random.randint(0, space_size) for _ in range(num_random_consumers)]
