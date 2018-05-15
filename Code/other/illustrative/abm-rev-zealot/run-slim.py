from model import *
import matplotlib.pyplot as plt

num_nodes_int=7000

model = VirusModel(num_nodes=num_nodes_int, avg_node_degree=6, prob_rewire=0.2, initial_outbreak_size=1, alpha=0.006, beta=0.8, gamma=0.06, delta=1/200, k=3, n=5)
for i in range(400):
    model.step()

s_green = "#ADD694"
e_yellow = "#FFCD47"
i_pink = "#F2728C"
r_blue = "#67B8C7"

df = model.datacollector.get_model_vars_dataframe()[["Susceptible","Carrier","Infected","Removed"]]
df.plot(color=[s_green,e_yellow,i_pink,r_blue])
plt.xlabel("Time (Days)")
plt.ylabel("Number of Individuals")
plt.show()

df2 = model.datacollector.get_model_vars_dataframe()[["Exposed Clustering","Active Clustering"]]
df2.plot(color=[e_yellow,i_pink])
plt.xlabel("Time (Days)")
plt.ylabel(r'Clustering, $C_i$')
plt.show()

df3 = model.datacollector.get_model_vars_dataframe()[["Exposed Spread","Infective Spread"]]
df3.plot(color=[e_yellow,i_pink])
plt.xlabel("Time (Days)")
plt.ylabel(r'Spread, $S_i$')
plt.show()