from model import *
import matplotlib.pyplot as plt

num_nodes_int=700

model = VirusModel(num_nodes=num_nodes_int, avg_node_degree=6, prob_rewire=0.2, initial_outbreak_size=1, alpha=0.006, beta=0.08, gamma=0.06, k=3, n=5)
for i in range(1000):
    model.step()


df = model.datacollector.get_model_vars_dataframe()
df.plot()
plt.show()