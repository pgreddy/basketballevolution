import sys
import os
# Used to allow arbitrary functions of inputs
import parser

# GENERATE FEATURE EQUATIONS
features = []
with open(sys.argv[1]) as featurefile:
    for line in featurefile:
        features.append(parser.expr(line).compile())

# GENERATE CONDITIONAL EQUATIONS
conditionals = []
with open(sys.argv[2]) as conditionalfile:
    for line in conditionalfile:
        conditionals.append(parser.expr(line).compile())


data_files = [f for f in os.listdir(sys.argv[3]) if not f.startswith('.')]

with open(sys.argv[4] + 'training_data_' + sys.argv[5] + '.csv', 'w') as trainingfile:
    for data_file in data_files:
        data_file_path = data_file.split('.')
        data_prefix = data_file_path[0]
        data_suffix = '.' + data_file_path[1]

        # READ AND PARSE PLAYER ATTRIBUTES
        primary_players = {}
        secondary_players = {}
        conditional_primary_players = [dict() for x in range(len(conditionals))]
        conditional_secondary_players = [dict() for x in range(len(conditionals))]
        with open(sys.argv[3] + data_prefix + data_suffix) as eventfile:
            for line in eventfile:
                els = line.split(",")
                p1id = int(els[0])
                try:
                    p2id = int(els[1])
                except:
                    p2id = -1
                event = int(els[2])
                attr = []
                for x in els[0:]:
                    try:
                        attr.append(int(x))
                    except:
                        attr.append(-1)

                # PARSE FOR GENERAL FILE FOR PLAYER 1
                if p1id in primary_players.keys():
                    primary_players[p1id][event] = primary_players[p1id][event] + 1
                else:
                    primary_players[p1id] = [0] * (13)
                    primary_players[p1id][event] = primary_players[p1id][event] + 1

                # PARSE FOR GENERAL FILE FOR PLAYER 2
                if p2id in secondary_players.keys():
                    secondary_players[p2id][event] = secondary_players[p2id][event] + 1
                else:
                    secondary_players[p2id] = [0] * (13)
                    secondary_players[p2id][event] = secondary_players[p2id][event] + 1

                # PARSE FOR CONDITIONALS
                for i in range (len(conditionals)):
                    if (eval(conditionals[i])):
                        if p1id in conditional_primary_players[i].keys():
                            conditional_primary_players[i][p1id][event] = conditional_primary_players[i][p1id][event] + 1
                        else:
                            conditional_primary_players[i][p1id] = [0] * (13)
                            conditional_primary_players[i][p1id][event] = conditional_primary_players[i][p1id][event] + 1

                        if p2id in conditional_secondary_players[i].keys():
                            conditional_secondary_players[i][p2id][event] = conditional_secondary_players[i][p2id][event] + 1
                        else:
                            conditional_secondary_players[i][p2id] = [0] * (13)
                            conditional_secondary_players[i][p2id][event] = conditional_secondary_players[i][p2id][event] + 1



        # COMPUTE AND WRITE FEATURES
        z = conditional_primary_players
        with open(sys.argv[4] + data_prefix + data_suffix, 'w') as outfile:
            # ASSUMED FORMAT IS `{pid: [x[0], x[1], x[2], x[3] ...]}`
            for pid in primary_players.keys():
                line = str(pid)
                for feature in features:
                    x = primary_players.get(pid, [])
                    y = secondary_players.get(pid, [])
                    try:
                        line = line + ', ' + str(eval(feature))
                    except:
                        line = line + ',0'
                outfile.write(line + '\n')

                # SAVE TO COMPLETE TRAINING FILE
                years = data_file.split('-')
                trainingfile.write(years[0] + ', ' + line + '\n')
