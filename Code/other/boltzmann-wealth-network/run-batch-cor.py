from __future__ import division


from model_cor import *	#imports the libraries needed in model.py
import matplotlib.pyplot as plt #for drawing the results

import numpy as np

node_degree = []
all_wealth = []

num_inst=1 #number of instantiations
num_agents=50 #number of agents
num_steps=100 #number of steps

# w, h = 0, 0;
# data = [[0 for x in range(w)] for y in range(h)]

for j in range(num_inst):
    # Run the model
    model = MoneyModel(num_agents)
    for i in range(num_steps):
        model.step()

    # Store the results
    for agent in model.schedule.agents:
        node_degree.append(model.G.degree(agent.unique_id))
        all_wealth.append(agent.wealth)
        print(str(agent.wealth)+' '+str(model.G.degree(agent.unique_id))+' '+str(agent.unique_id))

x=node_degree
y=all_wealth

plt.scatter(x,y,alpha=0.5)
plt.xlabel('Node Degree')
plt.ylabel('Agent Wealth')

plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))

plt.show()
