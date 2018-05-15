import axelrod as axl
import numpy as np
import csv

download_dir = "axelrod-tournament.csv" #where file will go
csv = open(download_dir, "w")   #allow writing to file
columnTitleRow= 'Strategy Name, Average Pay-off\n'
csv.write(columnTitleRow)

# players = [s() for s in axl.basic_strategies]
players = [s() for s in axl.strategies]
# players = [axl.Cooperator(),axl.Alternator(),axl.TitForTat(), axl.Random(), axl.Defector()]
tournament = axl.Tournament(players,repetitions=1,turns=1)
results=tournament.play()
for i in range(len(players)):
    player_name = players[i].name
    player_score = np.mean(results.normalised_scores[i])
    print(player_name + ' ' + str(player_score))
    csv.write(player_name + ',' + str(player_score) + '\n')