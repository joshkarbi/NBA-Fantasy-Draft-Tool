'''
  Analyze stats from previous season for all players,
  given strategy defined in a config file (command line arg)

  ie. python3 analyze-data.py config/strategy.json
'''

import json
import sys

class Player:
    def __init__(self, score, name, position):
        self.score = score
        self.name = name
        self.pos = position
    def __lt__(self, other):
        return self.score < other.score

# read config file, based on categories and weights assign score to each player
# and output to "drafting list" CSV to use in draft

with open('data/player_combined_data.csv') as data:

    strategy_name = str(sys.argv[1])

    config = json.load(open(strategy_name) )
    print(config)
    # get indices of each CSV category
    tokens = {}
    i = 0
    for token in data.readlines()[0].split(','):
        tokens[token.replace('\n', '')] = i
        i+= 1

    print("FOUND TOKENS:")
    print(tokens)
    print("\n\n")

    # final score -> (player name, position)
    results = {}
    data.seek(0)

    results = []
    for line in data.readlines()[1:]:
        line = line.split(',')
        score = 0
        for category in config["player_stat_categories"].keys():
            score_this_category = float(line[tokens[category]]) * config["player_stat_categories"][category]
            score += score_this_category
            print(category, " ", score_this_category)
        print("Total player score ", score)
        name = line[tokens["name"]]
        positions = line[tokens["positions"]]
        results.append(Player(score, name, positions))

    results.sort(reverse=True)
    outfile2 = open('output_files/players_ranked_by_score_' + strategy_name.replace('.json', '').replace('config/', '') + ".csv", 'w+')
    outfile2.write("Name,Position,Score\n")
    for result in results:
        outfile2.write(result.name+","+result.pos+","+str(result.score)+"\n")

