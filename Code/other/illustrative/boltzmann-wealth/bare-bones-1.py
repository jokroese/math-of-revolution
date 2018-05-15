# instantiate one model with 100 agents and 1 initial wealth
model = MoneyModel(100,1)

class MoneyModel(Model):
    """A model with some number of agents."""
    def __init__(self, n, init_wealth):
        # hold the number of agents
        self.num_agents = n

        # Create agents
        for i in range(self.num_agents):
            a = MoneyAgent(i, self, init_wealth)
            self.schedule.add(a)

class MoneyAgent(Agent):
    """ An agent with fixed initial wealth."""
    def __init__(self, model, unique_id, init_wealth):
        self.wealth = init_wealth

    def step(self):
        if self.wealth > 0:
            other_agent = random.choice(self.model.schedule.agents)
            other_agent.wealth += 1
            self.wealth -= 1