import random
import math
from enum import Enum
import networkx as nx

from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
from mesa.space import NetworkGrid

class State(Enum):
    SUSCEPTIBLE, INACTIVE, ACTIVE, REMOVED = range(4)

def number_state(model, state):
    return sum([1 for a in model.grid.get_all_cell_contents() if a.state is state])

def number_susceptible(model):
    return number_state(model, State.SUSCEPTIBLE)

def number_inactive(model):
    return number_state(model, State.INACTIVE)

def number_active(model):
    return number_state(model, State.ACTIVE)

def number_removed(model):
    return number_state(model, State.REMOVED)

class VirusModel(Model):
    def __init__(self, num_nodes, avg_node_degree, prob_rewire, initial_outbreak_size, alpha, beta, gamma, k, n):

        self.num_nodes = num_nodes
        self.avg_node_degree = avg_node_degree
        self.prob_rewire=prob_rewire
        self.G = nx.watts_strogatz_graph(n=self.num_nodes,k=avg_node_degree,p=prob_rewire)
        # self.G = nx.erdos_renyi_graph(n=self.num_nodes, p=prob)
        self.grid = NetworkGrid(self.G)
        self.schedule = RandomActivation(self)
        self.initial_outbreak_size = initial_outbreak_size if initial_outbreak_size <= num_nodes else num_nodes
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma

        self.k=k
        self.n=n

        # Create agents
        for i, node in enumerate(self.G.nodes()):
            a = VirusAgent(i, self, State.SUSCEPTIBLE, self.alpha, self.beta, self.gamma, self.k, self.n)
            self.schedule.add(a)
            # Add the agent to the node
            self.grid.place_agent(a, node)

        # Infect some nodes
        active_nodes = random.sample(self.G.nodes(), self.initial_outbreak_size)
        for a in self.grid.get_cell_list_contents(active_nodes):
            a.state = State.ACTIVE

        self.datacollector = DataCollector(
            model_reporters={
                             "Infected": number_active,
                             "Susceptible": number_susceptible,
                             "Carrier": number_inactive,
                             "Removed": number_removed
                             # "Active Clustering": infective_clustering,
                             }
        )

        self.running = True
        self.datacollector.collect(self)

    def removed_susceptible_ratio(self):
        try:
            return number_state(self, State.REMOVED) / number_state(self, State.SUSCEPTIBLE)
        except ZeroDivisionError:
            return math.inf

    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)

    def run_model(self, n):
        for i in range(n):
            self.step()


class VirusAgent(Agent):
    def __init__(self, unique_id, model, initial_state, alpha, beta, gamma, k, n):
        super().__init__(unique_id, model)

        self.state = initial_state

        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma

        self.k = k
        self.n = n

    def try_to_infect_neighbors(self):
        neighbors_nodes = self.model.grid.get_neighbors(self.pos, include_center=False)
        susceptible_neighbors = [agent for agent in self.model.grid.get_cell_list_contents(neighbors_nodes) if
                                 agent.state is State.SUSCEPTIBLE]
        for a in susceptible_neighbors:
            if random.random() < self.beta:
                a.state = State.INACTIVE

    def try_become_active(self):
        neighbors_nodes = self.model.grid.get_neighbors(self.pos, include_center=False)
        active_neighbors = [agent for agent in self.model.grid.get_cell_list_contents(neighbors_nodes) if
                                 agent.state is State.ACTIVE]
        num_active_neighbors=len(active_neighbors)
        # prop_active_neighbors = active_neighbors/neighbors_nodes
        x=random.random()
        y = (-((self.k**(-self.n))*(x-1))/x)**(-1/self.n)
        if y < num_active_neighbors:
            self.state = State.ACTIVE

    def try_gain_resistance(self):
        if random.random() < self.alpha:
            self.state = State.REMOVED

    def step(self):
        if self.state is State.ACTIVE:
            self.try_to_infect_neighbors()
            self.try_gain_resistance()
            # self.try_become_inactive()
        elif self.state is State.INACTIVE:
            self.try_become_active()