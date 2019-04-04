import sys


# GENERATE MAP

categories = {}
with open(sys.argv[1]) as mapfile:
    for alllines in mapfile:
        # Google Sheets Downloads as a single line, this is to avoid that
        lines = alllines.split("\r")
        for line in lines:
            els = line.split(",")
            if len(els) > 3:
                categories[(els[0].strip(), els[1].strip())] = els[3].strip()

# WRITE TRANSLATION TO FILE

with open(sys.argv[2]) as eventfile, open(sys.argv[3], 'w') as outfile:
    next(eventfile)
    for line in eventfile:
        els = line.split(",")

        # els[0] is event number over entire set (unused)
        # els[1] is event action type
        actiontype = els[1]

        # els[2] is event message type
        messagetype = els[2]

        # els[3] is event number within set (unused)
        # els[4] is game id (unused)
        # els[5] is home description of event (unused)
        # els[6] is neutral description of event (unused)
        # els[7] is play clock time (unused)
        # els[8] is period (unused)
        # els[9] is person 1 type (unused)
        # els[10] is person 2 type (unused)
        # els[11] is person 3 type (unused)
        # els[12] is player 1 id
        p1id = els[12]

        # els[13] is player 1 name (unused)
        # els[14] is player 1 team abbrev (unused)
        # els[15] is player 1 team city (unused)
        # els[16] is player 1 team id (unused)
        # els[17] is player 1 team nickname (unused)
        # els[18] is player 2 id
        p2id = els[18]

        # els[19] is player 2 name (unused)
        # els[20] is player 2 team abbrev (unused)
        # els[21] is player 2 team city (unused)
        # els[22] is player 2 team id (unused)
        # els[23] is player 2 team nickname (unused)
        # els[24] is player 3 id (unused)
        # els[25] is player 3 name (unused)
        # els[26] is player 3 team abbrev (unused)
        # els[27] is player 3 team city (unused)
        # els[28] is player 3 team id (unused)
        # els[29] is player 3 team nickname (unused)
        # els[30] is game score
        gmscore = els[30]

        # els[31] is score margin (unused)
        # els[32] is visitor description of event (unused)
        # els[33] is clock time (unused)

        newevent = categories.get((actiontype, messagetype), '0')
        outfile.write(p1id + ', ' + p2id + ', ' + newevent + ', ' + gmscore + '\n')
        


