from __future__ import division


from model_cor import *	#imports the libraries needed in model.py
import matplotlib.pyplot as plt #for drawing the results

import numpy as np

# import pylab
from scipy.optimize import curve_fit

node_degree = []
wealth = []

num_inst=1000 #number of instantiations
num_agents=50 #number of agents
num_steps=100 #number of steps

for j in range(num_inst):
    # Run the model
    model = MoneyModel(num_agents)
    for i in range(num_steps):
        model.step()

    # Store the results
    for agent in model.schedule.agents:
        node_degree.append(model.G.degree(agent.unique_id))
        wealth.append(agent.wealth)
        print(str(agent.wealth)+' '+str(model.G.degree(agent.unique_id))+' '+str(agent.unique_id))



xdata=node_degree
ydata=wealth

def sigmoid(x, b, k, n):
    y = b * (k**n)/(k**n + x**n)
    return y

# def sigmoid(x, x0, k):
#     y = max(wealth) / (1 + np.exp(-k*(x-x0)))
#     return y



popt, pcov = curve_fit(sigmoid, xdata, ydata)
print(popt)

x = np.linspace(0, max(xdata), max(xdata))
y = sigmoid(x, *popt)

plt.scatter(xdata,ydata,alpha=0.05,label='data')
plt.xlabel('Node Degree')
plt.ylabel('Agent Wealth')

plt.plot(x, y,color="#ff6699",alpha=0.7,label='best fit')
plt.legend()

plt.show()
