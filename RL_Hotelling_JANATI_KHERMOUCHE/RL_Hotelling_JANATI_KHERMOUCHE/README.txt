Hotelling's Spatial Competition Simulation

This project is a simulation based on Hotelling's spatial competition model, implementing reinforcement learning concepts, especially Double Q-learning, to study the behavior of agents and consumers in a defined space.

Description

The simulation uses multiple classes to model the behaviors of agents (represented by the Trainer class), strategies (defined in Policy), and consumers (managed by Buffer). It also includes a feature to simulate the "laziness" of consumers, influencing their interaction with agents based on distance.

Prerequisites

Before running the simulation, make sure you have Python 3 installed on your machine. Additionally, the following libraries need to be installed:

pygame
numpy
matplotlib
These dependencies can be installed using the requirements.txt file.

Installation

Install Dependencies: Navigate to the project folder and install the required dependencies:

bash
Copy code
cd RL_Hotelling_JANATI_KHERMOUCHE
pip install -r requirements.txt
Execution
To run the simulation, execute the main script:

bash
Copy code
python3 main.py

Or copy the directory like cd Users / etc.. and launch with the command : python3 main.py when you are in the folder.

Follow the on-screen instructions to input simulation parameters via the Tkinter interface.

Project Structure

The project is organized as follows:

main.py: The main script to start the simulation.
trainer.py: Contains the simulation logic and agent behavior.
policy.py: Manages the learning strategies of agents.
buffer.py: Models consumer behavior and positions.

Contribution

Contributions to this project are welcome. If you'd like to contribute, please fork the repository and create a pull request with your changes.

