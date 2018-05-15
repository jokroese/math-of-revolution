import random

from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
import networkx as nx

from mesa.space import NetworkGrid


def compute_gini(model):
    agent_wealths = [agent.wealth for agent in model.schedule.agents]
    x = sorted(agent_wealths)
    N = model.num_agents
    B = sum(xi * (N - i) for i, xi in enumerate(x)) / (N * sum(x))
    return 1 + (1 / N) - 2 * B


class MoneyModel(Model):
    """A model with some number of agents."""
    #One agent per node

    def __init__(self, num_agents):

        self.num_agents = num_agents
        # self.G = nx.erdos_renyi_graph(n=num_agents, p=0.5)
        self.G = nx.barabasi_albert_graph(n=num_agents, m= 1)
        self.grid = NetworkGrid(self.G)
        self.schedule = RandomActivation(self)
        self.datacollector = DataCollector(
            # model_reporters={"Gini": compute_gini},
            agent_reporters={"Wealth": lambda _: _.wealth,
                             "Degree": lambda _: _.degree
                             }
        )

        # Create agents
        for i in range(self.num_agents):
            a = MoneyAgent(i, self)
            self.schedule.add(a)
            # Assign the agent to a node
            self.grid.place_agent(a, i)

        self.running = True
        self.datacollector.collect(self)

    def step(self):
        self.schedule.step()
        # collect data
        self.datacollector.collect(self)

    def run_model(self, n):
        for i in range(n):
            self.step()


class MoneyAgent(Agent):
    """ An agent with fixed initial wealth."""

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 1
        self.degree = 0

    def give_money(self):
        neighbors_nodes = self.model.grid.get_neighbors(self.pos, include_center=False)
        neighbors = self.model.grid.get_cell_list_contents(neighbors_nodes)
        if len(neighbors) > 0:
            other = random.choice(neighbors)
            other.wealth += 1
            self.wealth -= 1

    def step(self):
        # self.move()
        if self.wealth > 0:
            self.give_money()

    def find_degree(self, model, unique_ID):
        self.degree=model.G.degree(self.unique_id)

