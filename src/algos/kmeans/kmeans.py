from sklearn.cluster import KMeans
import numpy as np
import sys

sys.path.append('./src/util/')

import evaluator as ev

data_path = sys.argv
print(data_path)
data_full = np.genfromtxt(data_path, delimiter=',')

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
