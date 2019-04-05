import sys
import os
# Used to allow arbitrary functions of inputs
import parser


# GENERATE FEATURE EQUATIONS
features = []
with open(sys.argv[1]) as featurefile:
    for line in featurefile:
        features.append(parser.expr(line).compile())


data_files = [f for f in os.listdir(sys.argv[2]) if not f.startswith('.')]

with open(sys.argv[3] + 'training_data_' + sys.argv[4] + '.csv', 'w') as trainingfile:
    for data_file in data_files:
        data_file_path = data_file.split('.')
        data_prefix = data_file_path[0]
        data_suffix = '.' + data_file_path[1]
        # READ AND PARSE PLAYER ATTRIBUTES
        players = {}
        with open(sys.argv[2] + data_prefix + data_suffix) as eventfile:
            for line in eventfile:
                els = line.split(",")
                pid = int(els[0])
                event = int(els[2])

                if pid in players.keys():
                    players[pid][event] = players[pid][event] + 1
                else:
                    players[pid] = [0] * (6)
                    players[pid][event] = players[pid][event] + 1

        # COMPUTE AND WRITE FEATURES
        with open(sys.argv[3] + data_prefix + data_suffix, 'w') as outfile:
            # ASSUMED FORMAT IS `{pid: [x[0], x[1], x[2], x[3] ...]}`
            for player in players.keys():
                line = str(player)
                for feature in features:
                    x = players[player];
                    line = line + ', ' + str(eval(feature))
                outfile.write(line + '\n')

                # SAVE TO COMPLETE TRAINING FILE
                years = data_file.split('-')
                trainingfile.write(years[0] + ', ' + line + '\n')