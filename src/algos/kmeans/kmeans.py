from sklearn.cluster import KMeans
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

kmeans = KMeans(n_clusters=k).fit(trans_data)
print(kmeans.labels_)
print(kmeans.inertia_)

score = ev.cross_validate(training, 
			  KMeans(n_clusters=k), 
			  folds = 3, 
			  metric = "silhouette",
			  debug_print = "off")			
print(score)

viz.visualize(trans_data, kmeans.labels_, two_d = True, three_d = False)
viz.visualize(trans_data, kmeans.labels_, two_d = False, three_d = True)
