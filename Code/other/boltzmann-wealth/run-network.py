from model-space import *	#imports the libraries needed in model.py
import matplotlib.pyplot as plt #for drawing the results

# # one run
model = MoneyModel(50,10,10)
for i in range(10):
    model.step()

agent_wealth = [a.wealth for a in model.schedule.agents]
plt.hist(agent_wealth)
plt.show()


# #multiple runs
# all_wealth = []
# for j in range(10):		#number of instantiations
#     # Run the model
#     model = MoneyModel(1000,10,10) #number of agents
#     for i in range(100):		#number of steps
#         model.step()

#     # Store the results
#     for agent in model.schedule.agents:
#         all_wealth.append(agent.wealth)

# plt.hist(all_wealth, bins=range(max(all_wealth)+1))
# plt.show()



# #grid
# import numpy as np

# model = MoneyModel(10, 10, 10)
# for i in range(10):
#     model.step()

# agent_counts = np.zeros((model.grid.width, model.grid.height))
# for cell in model.grid.coord_iter():
#     cell_content, x, y = cell
#     agent_count = len(cell_content)
#     agent_counts[x][y] = agent_count
# plt.imshow(agent_counts, interpolation='nearest')
# plt.colorbar()
# plt.show()


# #plotting gini
# model = MoneyModel(50, 10, 10)
# for i in range(100):
#     model.step()

# #gini coefficients graph
# # gini = model.datacollector.get_model_vars_dataframe()
# # gini.plot()

# agent_wealth = model.datacollector.get_agent_vars_dataframe()
# agent_wealth.head()
# plt.show()


#batch run
# from mesa.batchrunner import BatchRunner
#
# fixed_params = {"width": 10,
#                 "height": 10}
# variable_params = {"N": range(10, 500, 10)}
#
# batch_run = BatchRunner(MoneyModel,
#                         fixed_parameters=fixed_params,
#                         variable_parameters=variable_params,
#                         iterations=1,
#                         max_steps=30,
#                         model_reporters={"Gini": compute_gini})
# batch_run.run_all()
#
# run_data = batch_run.get_model_vars_dataframe()
# run_data.head()
# plt.scatter(run_data.N, run_data.Gini)
# plt.show()