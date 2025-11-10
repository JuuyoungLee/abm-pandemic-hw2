# HW2 Agent-Based Model for Pandemic Spread
# Name: Juyoung LEE
# BMI500 HW11
# Fall 2025
# This file will implement:
# 1. Grid environment
# 2. Agents (S, I, R states)
# 3. Movement
# 4. Infection and recovery rules
import random
import numpy as np

# States:
# 0 = Susceptible (S)
# 1 = Infected (I)
# 2 = Recovered (R)

class Agent:
    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state

class PandemicABM:
    def __init__(self, grid_size=(75, 75), n_agents=100,
                 initial_S=95, initial_I=5, initial_R=0,
                 p_infection=0.1, p_recovery=0.05, 
                 move_prob=1.0, # social distancing
                 avoid_strength=0.0): # avoidance behavior
        """
        Initialize grid, agents & basic parameters.
        """
        self.width, self.height = grid_size
        self.p_infection = p_infection
        self.p_recovery = p_recovery
        self.move_prob = move_prob # social distancing
        self.avoid_strength = avoid_strength # avoidance behavior

        # Create agents in random positions
        self.agents = []
        states = [0]*initial_S + [1]*initial_I + [2]*initial_R
        random.shuffle(states)

        for state in states:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            self.agents.append(Agent(x, y, state))

    def move_agent(self, agent):
        """
        Move agent to one of its neighbors (8-direction or stay).
        Here: up, down, left, right, or stay.
        """
        ''' # before update
        dx, dy = random.choice([(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)])
        agent.x = (agent.x + dx) % self.width
        agent.y = (agent.y + dy) % self.height
        '''
        '''
        # updated after add move_prob
        if random.random() < self.move_prob:
            dx, dy = random.choice([(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)])
            agent.x = (agent.x + dx) % self.width
            agent.y = (agent.y + dy) % self.height
        '''
        
        if random.random() > self.move_prob:
            return
        # possible moves
        moves = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # if no avoidance, choose randomly
        if self.avoid_strength == 0:
            dx, dy = random.choice(moves)
            agent.x = (agent.x + dx) % self.width
            agent.y = (agent.y + dy) % self.height
            return
        
        # evaluate each move based on infected count
        scores = []
        for dx, dy in moves:
            new_x = (agent.x + dx) % self.width
            new_y = (agent.y + dy) % self.height
            infected_nearby = sum(
                1 for a in self.agents if a.x == new_x and a.y == new_y and a.state == 1
            )
            score = 1 / (1 + infected_nearby)  # fewer infected = higher score
            scores.append(score)
        
        # randomness + avoidance
        scores = np.array(scores, dtype=float)
        scores = (1 - self.avoid_strength) * 1 + self.avoid_strength * scores
        scores = scores / scores.sum()  # normalize probabilities

        # choose a move
        idx = np.random.choice(len(moves), p=scores)
        dx, dy = moves[idx]
        agent.x = (agent.x + dx) % self.width
        agent.y = (agent.y + dy) % self.height

    def step(self):
        """
        Perform 1 simulation step:
        1) Move all agents
        2) Infection
        3) Recovery
        """
        # 1. Movement
        for agent in self.agents:
            self.move_agent(agent)

        # 2. Infection — group agents by location
        positions = {}
        for agent in self.agents:
            positions.setdefault((agent.x, agent.y), []).append(agent)

        for pos, agents_here in positions.items():
            infected_present = any(a.state == 1 for a in agents_here)
            if infected_present:
                for a in agents_here:
                    if a.state == 0:  # S → I
                        if random.random() < self.p_infection:
                            a.state = 1

        # 3. Recovery — I → R
        for agent in self.agents:
            if agent.state == 1:
                if random.random() < self.p_recovery:
                    agent.state = 2

    def count_states(self):
        """
        Count how many S, I, R exist currently.
        """
        S = sum(1 for a in self.agents if a.state == 0)
        I = sum(1 for a in self.agents if a.state == 1)
        R = sum(1 for a in self.agents if a.state == 2)
        return S, I, R

    def run(self, steps=200):
        """
        Run the model for a number of steps and record populations.
        Returns: lists of S, I, R over time.
        """
        S_list, I_list, R_list = [], [], []

        for _ in range(steps):
            S, I, R = self.count_states()
            S_list.append(S)
            I_list.append(I)
            R_list.append(R)
            self.step()

        return S_list, I_list, R_list
