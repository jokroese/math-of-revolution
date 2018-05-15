import axelrod as axl
import matplotlib.pyplot as plt

# #match between two players
# players= (axl.Alternator(),axl.TitForTat())
# match = axl.Match(players,50)
# interactions = match.play()
# interactions
# print(interactions)


# tournament 2 between multiple  with one random player
players = (axl.Cooperator(),axl.Alternator(),axl.TitForTat(), axl.Random(), axl.Defector())
tournament = axl.Tournament(players, turns=100)
results=tournament.play()
print(results.ranked_names)

# hi-tek plot
plot = axl.Plot(results)
_, ax = plt.subplots()
xlabel = ax.set_xlabel('Strategies')
ylabel = ax.set_ylabel('Average Pay-off')
p = plot.boxplot(ax=ax)
p.show()

q=plot.payoff()
q.show()

print(results.repetitions)