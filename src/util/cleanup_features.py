import sys

comps = sys.argv[1].split('.')

with open(sys.argv[1]) as featurefile:
    firstline = featurefile.readline()
    start_els = firstline.split(',')
    max_feature_vals = [0] * len(start_els)
    for line in featurefile:
        els = line.split(',')
        for i in range(len(els)):
            max_feature_vals[i] = max(max_feature_vals[i], float(els[i]))

with open(sys.argv[1]) as featurefile, \
     open(comps[0] + '_final.' + comps[1], 'w') as final_features:
    for line in featurefile:
        els = line.split(',')
        # import pdb; pdb.set_trace()
        if int(els[int(sys.argv[2])]) > int(sys.argv[3]):
            final_line = els[0] + ',' + els[1]
            for i in range(2, len(els)):
                if max_feature_vals[i] > 10:
                    final_line = final_line + ',' +  str(float(els[i])/max_feature_vals[i])
                else:
                    final_line = final_line + ',' + els[i]

            final_features.write(final_line + '\n')
