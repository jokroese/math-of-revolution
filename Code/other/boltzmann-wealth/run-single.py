# a single run of the model.
# the two different runs are because you need different lengths of time
# to reach the equilibrium distribution and
# different plotting



from model import *	#imports the libraries needed in model.py
import matplotlib.pyplot as plt #for drawing the results

# # model with initial wealth 1
# model = MoneyModel(100,1)
# for i in range(100):
#     model.step()

# agent_wealth = [a.wealth for a in model.schedule.agents]

# plt.hist(agent_wealth, bins=range(max(agent_wealth)+1),
# 	normed=True, rwidth=0.5, align='left')
# plt.xlabel('Agent Wealth')
# plt.ylabel('Frequency Density')


# model with initial wealth 10
model = MoneyModel(100,10)
for i in range(10000):
    model.step()

agent_wealth = [a.wealth for a in model.schedule.agents]

plt.hist(agent_wealth,
	normed=True, rwidth=1)
plt.xlabel('Agent Wealth')
plt.ylabel('Frequency Density')



plt.show()