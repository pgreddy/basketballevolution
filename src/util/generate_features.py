import sys

# Used to allow arbitrary functions of inputs
import parser


# GENERATE FEATURE EQUATIONS
features = []
with open(sys.argv[1]) as featurefile:
    for line in featurefile:
        features.append(parser.expr(line).compile())

# READ AND PARSE PLAYER ATTRIBUTES
players = {}
with open(sys.argv[2]) as eventfile:
    for line in eventfile:
        els = line.split(",")
        pid = int(els[0])
        event = int(els[2])

        if pid in players.keys():
            players[pid][event] = players[pid][event] + 1
        else:
            players[pid] = [0] * (int(sys.argv[4]) + 1)
            players[pid][event] = players[pid][event] + 1

# COMPUTE AND WRITE FEATURES
with open(sys.argv[3], 'w') as outfile:
    # ASSUMED FORMAT IS `{pid: [x[0], x[1], x[2], x[3] ...]}`
    for player in players.keys():
        line = str(player)
        for feature in features:
            x = players[player];
            line = line + ', ' + str(eval(feature))
        outfile.write(line + '\n')