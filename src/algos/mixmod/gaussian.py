from sklearn.mixture import GaussianMixture
import numpy as np
import pandas as pd
import scipy.cluster.hierarchy as shc
import sys

sys.path.append('../../util/')

import visualizer as viz
import pca_util
import evaluator as ev

data_full = np.genfromtxt('../../../data/data_v1/final/training_data_v1_final.csv', delimiter=',')

# remove the first two columns which include data
training = data_full[0:20,2:]
test = data_full[21:40,2:]

# run clustering algorithm
cluster = GaussianMixture(n_components=3)
cluster.fit(training)
cluster_labels = cluster.predict(test)

print(cluster_labels)

# test cross-validation script from this file
score = ev.cross_validate(training, 
						GaussianMixture(n_components=3), 
						folds = 2, 
						metric = "silhouette",
						debug_print = "off")
print(score)