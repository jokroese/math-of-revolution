from model import *
import matplotlib.pyplot as plt

model = VirusModel(num_nodes=100, avg_node_degree=2, initial_outbreak_size=1, alpha=0.03, beta=0.05)
# while number_infected(model)>0:
#     model.step()
for n in range(10):
    model.step()

df = model.datacollector.get_model_vars_dataframe()
df.plot()
plt.xlabel('Time (Days)')
plt.ylabel('Number of Individuals')
plt.show()