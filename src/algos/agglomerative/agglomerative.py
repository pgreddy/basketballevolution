from sklearn.cluster import AgglomerativeClustering
import numpy as np
import pandas as pd
import scipy.cluster.hierarchy as shc
import pdb

data_full = np.genfromtxt('../../../data/data_v1/final/training_data_v1_final.csv', delimiter=',')

# Remove the first two columns which include data
training = data_full[:,2:]

#Run clustering algorithm
cluster = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')  
cluster.fit_predict(training) 
print(cluster.labels_)

#pdb.set_trace()

#Plots for dendograms
#plt.figure(figsize=(10, 7))  
#plt.title("Customer Dendograms")  
#dend = shc.dendrogram(shc.linkage(X, method='ward')) 