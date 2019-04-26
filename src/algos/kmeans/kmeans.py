from sklearn.cluster import KMeans
import numpy as np
import sys

sys.path.append('../../util/')

import evaluator as ev

data_full = np.genfromtxt('../../../data/data_v1/final/training_data_v1_final.csv', delimiter=',')
# Remove the first two columns which include data
training = data_full[:,2:]
kmeans = KMeans(n_clusters=10).fit(training)
print(kmeans.labels_)
print(kmeans.inertia_)

score = ev.cross_validate(training, 
						KMeans(n_clusters=3), 
						folds = 3, 
						metric = "silhouette",
						debug_print = "off")			
print(score)
