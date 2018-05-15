from model import *	#imports the libraries needed in model.py
import matplotlib.pyplot as plt #for drawing the results

# # one run
model = MoneyModel(10)
for i in range(10):
    model.step()

agent_wealth = [a.wealth for a in model.schedule.agents]
plt.hist(agent_wealth, bins=range(max(agent_wealth)),
	normed=True, rwidth=0.5, align='left')
plt.xlabel('Agent Wealth')
plt.ylabel('Frequency Density')


plt.show()