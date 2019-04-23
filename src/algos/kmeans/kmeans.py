from sklearn.cluster import KMeans
import numpy as np
import sys

sys.path.append('../../util/')

import visualizer as viz
import pca_util

data_full = np.genfromtxt('../../../data/data_v1/final/training_data_v1_final.csv', delimiter=',')
# Remove the first two columns which include data
training = data_full[:,2:]

# TODO:
#   Turn this into a function, num_components and k should be arguments
num_components = 5;
k = 3;
pca, trans_data = pca_util.get_pca(num_components, training)
kmeans = KMeans(n_clusters=k).fit(trans_data)
print(kmeans.labels_)
print(kmeans.inertia_)

viz.visualize(trans_data, kmeans.labels_, two_d = True, three_d = False)
viz.visualize(trans_data, kmeans.labels_, two_d = False, three_d = True)

# For debugging:
#import pdb; pdb.set_trace()
