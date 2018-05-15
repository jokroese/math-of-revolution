from model import *
import matplotlib.pyplot as plt

num_nodes_int=70

model = VirusModel(num_nodes=num_nodes_int, avg_node_degree=6, initial_outbreak_size=1, alpha=0.006, beta=0.8, gamma=0.06, delta=1/200, k=3, n=5)
for i in range(400):
    model.step()

df = model.datacollector.get_model_vars_dataframe()[["Susceptible","Carrier","Infected","Removed"]]
df.plot()
plt.show()
#
#
# df2 = model.datacollector.get_model_vars_dataframe()[["Active Clustering", "Exposed Clustering"]]
# df2.plot()
# plt.show()

# df3 = model.datacollector.get_model_vars_dataframe()[["Infective Diffusion", "Exposed Diffusion"]]
# df3.plot()
# plt.show()