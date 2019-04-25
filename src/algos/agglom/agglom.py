from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import scipy.cluster.hierarchy as shc
import pdb
import sys

sys.path.append('../../util/')

import visualizer as viz
import pca_util
import evaluator as ev

data_full = np.genfromtxt('../../../data/data_v1/final/training_data_v1_final.csv', delimiter=',')

# remove the first two columns which include data
training = data_full[:,2:]

# run clustering algorithm
cluster = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')  
cluster.fit_predict(training) 
print(cluster.labels_)

# test cross-validation script from this file
score = ev.cross_validate(training, 
						AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward'), 
						folds = 1, 
						metric = "silhouette",
						debug_print = "off")
print(score)

score = ev.cross_validate(training, 
						KMeans(n_clusters=3), 
						folds = 3, 
						metric = "silhouette",
						debug_print = "off")			
print(score)

#pdb.set_trace()

#Plots for dendograms
#plt.figure(figsize=(10, 7))  
#plt.title("Customer Dendograms")  
#dend = shc.dendrogram(shc.linkage(X, method='ward')) 