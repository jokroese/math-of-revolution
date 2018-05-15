import random
import math
from enum import Enum
import networkx as nx

from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
from mesa.space import NetworkGrid


class State(Enum):
    SUSCEPTIBLE, INFECTED, REMOVED = range(3)

def number_state(model, state):
    return sum([1 for a in model.grid.get_all_cell_contents() if a.state is state])

def number_infected(model):
    return number_state(model, State.INFECTED)


def number_susceptible(model):
    return number_state(model, State.SUSCEPTIBLE)


def number_removed(model):
    return number_state(model, State.REMOVED)

class VirusModel(Model):

    def __init__(self, num_nodes, avg_node_degree, initial_outbreak_size, alpha, beta):
        self.num_nodes = num_nodes
        prob = avg_node_degree / self.num_nodes
        self.initial_outbreak_size = initial_outbreak_size if initial_outbreak_size <= num_nodes else num_nodes
        self.alpha = alpha
        self.beta = beta

        self.G = nx.barabasi_albert_graph(n=self.num_nodes,m=3)
        # self.G = nx.erdos_renyi_graph(n=self.num_nodes, p=prob)
        self.grid = NetworkGrid(self.G)

        self.schedule = RandomActivation(self)

        self.datacollector = DataCollector({"Susceptible": number_susceptible,
                                            "Infected": number_infected,
                                            "Removed": number_removed})

        # Create agents
        for i, node in enumerate(self.G.nodes()):
            a = VirusAgent(i, self, State.SUSCEPTIBLE, self.alpha, self.beta,)
            self.schedule.add(a)
            self.grid.place_agent(a, node)

        # Infect some nodes
        infected_nodes = random.sample(self.G.nodes(), self.initial_outbreak_size)
        for a in self.grid.get_cell_list_contents(infected_nodes):
            a.state = State.INFECTED

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
    def __init__(self, unique_id, model, initial_state, alpha, beta):

        super().__init__(unique_id, model)
        self.state = initial_state
        self.alpha = alpha
        self.beta = beta

    def try_to_infect_neighbors(self):
        neighbors_nodes = self.model.grid.get_neighbors(self.pos, include_center=False)
        susceptible_neighbors = [agent for agent in self.model.grid.get_cell_list_contents(neighbors_nodes) if
                                 agent.state is State.SUSCEPTIBLE]
        for a in susceptible_neighbors:
            if random.random() < self.beta:
                a.state = State.INFECTED

    def try_gain_resistance(self):
        if random.random() < self.alpha:
            self.state = State.REMOVED

    def step(self):
        if self.state is State.INFECTED:
            self.try_to_infect_neighbors()
            self.try_gain_resistance()