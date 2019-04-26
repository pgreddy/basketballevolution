from sklearn.mixture import GaussianMixture
import numpy as np
import sys

sys.path.append('./src/util/')

import evaluator as ev
import visualizer as viz
import pca_util

data_path = sys.argv[1]
print(data_path)
data_full = np.genfromtxt(data_path, delimiter=',')

k = 3;

# Remove the first two columns which include data
training = data_full[:,2:]
pca, trans_data = pca_util.get_pca(training)

cluster = GaussianMixture(n_components=k)
cluster.fit(trans_data)
cluster_labels = cluster.predict(trans_data)

print(cluster_labels)

# test cross-validation script from this file
score = ev.cross_validate(trans_data, 
						GaussianMixture(n_components=k), 
						folds = 3, 
						metric = "silhouette",
						debug_print = "off")
print(score)

viz.visualize(trans_data, cluster_labels, two_d = True, three_d = False, plot_name="mixmod_2d")
viz.visualize(trans_data, cluster_labels, two_d = False, three_d = True, plot_name="mixmod_3d")