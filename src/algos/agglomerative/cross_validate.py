from sklearn.cluster import AgglomerativeClustering
import numpy as np
import pandas as pd
from sklearn import metrics
import scipy.cluster.hierarchy as shc
import pdb

data_full = np.genfromtxt('../../../data/data_v1/final/training_data_v1_final.csv', delimiter=',')

# Remove the first two columns which include data
training = data_full[:,2:]

#pdb.set_trace()

def cross_validate( data, cluster_method = "agglomerative", folds = 5, metric = "silhouette"):   
	# train model on training set, using specific clustering method, and get predicted labels for test data
	if cluster_method == "agglomerative":
		cluster = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')  
		cluster.fit_predict(training) 
		cluster_labels = cluster.labels_
	
	# evaluate predicted labels using the metric specified (default is silhouette)
	if metric == "silhouette":
		sample_size = 300
		score = metrics.silhouette_score(data, cluster_labels,
										metric='euclidean',
                                    	sample_size=sample_size)
	
	# return cross-validated silhouette score
	return score;

#Run clustering algorithm
score = cross_validate(training, cluster_method = "agglomerative", folds = 5, metric = "silhouette")
print(score)
