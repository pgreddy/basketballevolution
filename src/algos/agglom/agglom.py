from sklearn.cluster import AgglomerativeClustering
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
training = np.delete(training, [27, 28, 29, 31], 1)
pca, trans_data = pca_util.get_pca(training)

cluster = AgglomerativeClustering(n_clusters=k, affinity='euclidean', linkage='ward')
cluster.fit_predict(trans_data)
print(cluster.labels_)

score = ev.cross_validate(trans_data,
			  AgglomerativeClustering(n_clusters=k, affinity='euclidean', linkage='ward'),
			  folds = 1,
			  metric = "silhouette",
			  debug_print = "off")
print(score)

viz.visualize(trans_data, cluster.labels_, two_d = True, three_d = False, plot_name="agglom_2d")
viz.visualize(trans_data, cluster.labels_, two_d = False, three_d = True, plot_name="agglom_3d")

#Plots for dendograms
#plt.figure(figsize=(10, 7))
#plt.title("Customer Dendograms")
#dend = shc.dendrogram(shc.linkage(X, method='ward'))
