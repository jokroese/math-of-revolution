from model import *
import matplotlib.pyplot as plt

model = VirusModel(num_nodes=10, avg_node_degree=2, initial_outbreak_size=1, alpha=0.5, beta=0.5)
for i in range(10):
    model.step()


num_infected = [1 for a.State.INFECTED in model.schedule.agents]
plt.chart(num_infected)
plt.show()