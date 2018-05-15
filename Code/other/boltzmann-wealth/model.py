from mesa import Agent, Model
from mesa.time import RandomActivation
import random
from mesa.datacollection import DataCollector

class MoneyAgent(Agent):
    """ An agent with fixed initial wealth."""
    def __init__(self, model, unique_id, init_wealth):
        self.wealth = init_wealth
        self.unique_id=unique_id
        self.model=model

    def step(self):
        if self.wealth > 0:
            other_agent = random.choice(self.model.schedule.agents)
            other_agent.wealth += 1
            self.wealth -= 1

class MoneyModel(Model):
    """A model with some number of agents."""
    def __init__(self, n, init_wealth):
        # hold the number of agents
        self.num_agents = n
        self.schedule = RandomActivation(self)

        # Create agents
        for i in range(self.num_agents):
            a = MoneyAgent(self, i, init_wealth)
            self.schedule.add(a)

        self.datacollector = DataCollector(
            agent_reporters={"Wealth": lambda a: a.wealth})  

    def step(self):
        '''Advance the model by one step.'''
        # print("New step.")
        self.datacollector.collect(self)
        self.schedule.step()