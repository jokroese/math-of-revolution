import axelrod as axl
import matplotlib.pyplot as plt
import random

num_agents=5

# axl.seed(0)
# player_list = [axl.Cooperator(),axl.Alternator(),axl.TitForTat(), axl.Random(), axl.Defector()]
# player_list = axl.strategies
player_list = [s() for s in axl.basic_strategies]
print(player_list)
players = []
for i in range(num_agents):
    n= round(random.random()*(len(player_list)-1))
    players.append(player_list[n])
print(players)
mp = axl.MoranProcess(players)
populations = mp.play()
ax = mp.populations_plot()
ax.title('Hi')
plt.show()