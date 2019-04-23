from sklearn.cluster import AgglomerativeClustering
import numpy as np
import pandas as pd
from sklearn import metrics
import scipy.cluster.hierarchy as shc
import pdb
from sklearn.model_selection import KFold
import statistics as st

data_full = np.genfromtxt('../../../data/data_v1/final/training_data_v1_final.csv', delimiter=',')

# Remove the first two columns which include data
training = data_full[0:60,2:]

def cross_validate( data, cluster, folds = 5, metric = "silhouette", debug_print = "off"):
	# initialize return values and index variable
	kf = KFold(n_splits=folds, shuffle = True)
	kf.get_n_splits(data)
	
	i = 0
	score = np.zeros(folds)
	
	# run through each fold in kf
	for train_index, test_index in kf.split(data):
		if debug_print == "on":
			print("iter: %.3f" % i)
			print("TRAIN:", train_index, "TEST:", test_index)

		X_train, X_test = data[train_index], data[test_index]
		
		# train model on training set and get predicted labels for test data
		cluster.fit(X_train) 
		cluster_labels = cluster.labels_
		
		# evaluate predicted labels using the metric specified (default is silhouette)
		if metric == "silhouette":
			sample_size = 300
			score[i] = metrics.silhouette_score(X_train, cluster_labels, #TODO: we want this to be X_test!!
											metric='euclidean',
											sample_size=sample_size)
		i = i+1
		
	# return cross-validated score
	return st.mean(score);

#Run clustering algorithm
score = cross_validate(training, 
						AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward'), 
						folds = 5, 
						metric = "silhouette",
						debug_print = "off")
print(score)
