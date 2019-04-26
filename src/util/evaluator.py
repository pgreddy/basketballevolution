import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.model_selection import KFold
import statistics as st

def cross_validate( data, cluster, folds = 5, metric = "silhouette", sample_size = 300, debug_print = "off"):
	# initialize return values
	i = 0
	score = np.zeros(folds)
	
	# edge case when there's only one fold
	if folds < 2:
		# train model on training set and get predicted labels for test data
		cluster.fit(data) 
		cluster_labels = cluster.labels_
	
		# evaluate predicted labels using the metric specified (default is silhouette)
		if metric == "silhouette":
			score[i] = metrics.silhouette_score(data, cluster_labels,
											metric='euclidean',
											sample_size=sample_size)
		return st.mean(score);

	# initialize folds variable
	kf = KFold(n_splits=folds, shuffle = True)
	kf.get_n_splits(data)

	# run through each fold in kf
	for train_index, test_index in kf.split(data):
		if debug_print == "on":
			print("iter: %.3f" % i)
			print("TRAIN:", train_index, "TEST:", test_index)

		X_train, X_test = data[train_index], data[test_index]
	
		# train model on training set and get predicted labels for test data
		cluster.fit(X_train)
		cluster_labels = cluster.predict(X_test)
	
		# evaluate predicted labels using the metric specified (default is silhouette)
		if metric == "silhouette":
			score[i] = metrics.silhouette_score(X_test, cluster_labels,
											metric='euclidean',
											sample_size=sample_size)
		i = i+1
		
	# return cross-validated score
	return st.mean(score);