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
        players = {}
        conditionalplayers = [dict() for x in range(len(conditionals))]
        with open(sys.argv[3] + data_prefix + data_suffix) as eventfile:
            for line in eventfile:
                els = line.split(",")
                p1id = int(els[0])
                event = int(els[2])
                attr = []
                for x in els[0:]:
                    try:
                        attr.append(int(x))
                    except:
                        attr.append(-1)

                # PARSE FOR GENERAL FILE
                if p1id in players.keys():
                    players[p1id][event] = players[p1id][event] + 1
                else:
                    players[p1id] = [0] * (6)
                    players[p1id][event] = players[p1id][event] + 1
                
                # PARSE FOR CONDITIONALS
                for i in range (len(conditionals)):
                    if (eval(conditionals[i])):
                        if p1id in conditionalplayers[i].keys():
                            conditionalplayers[i][p1id][event] = conditionalplayers[i][p1id][event] + 1
                        else:
                            conditionalplayers[i][p1id] = [0] * (6)
                            conditionalplayers[i][p1id][event] = conditionalplayers[i][p1id][event] + 1
                
                

        # COMPUTE AND WRITE FEATURES
        y = conditionalplayers
        with open(sys.argv[4] + data_prefix + data_suffix, 'w') as outfile:
            # ASSUMED FORMAT IS `{pid: [x[0], x[1], x[2], x[3] ...]}`
            for pid in players.keys():
                line = str(pid)
                for feature in features:
                    x = players[pid]
                    try:
                        line = line + ', ' + str(eval(feature))
                    except:
                        line = line + ',0'
                outfile.write(line + '\n')

                # SAVE TO COMPLETE TRAINING FILE
                years = data_file.split('-')
                trainingfile.write(years[0] + ', ' + line + '\n')