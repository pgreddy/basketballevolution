from sklearn.cluster import KMeans
import numpy as np
import sys

sys.path.append('./src/util/')

import visualizer as viz
import evaluator as cross_val
import pca_util

data_path = sys.argv[1]
print(data_path)
data_full = np.genfromtxt(data_path, delimiter=',')

# Remove the first two columns which include data
training = data_full[:,2:]
training = np.delete(training, [27, 28, 29, 31], 1)

pca, trans_data = pca_util.get_pca(training)

best_score = 0
ideal_k = 0
scores = [0] * 16 
for k in range(2, 18): # 2 - 25
    score = cross_val.cross_validate(trans_data, 
    			  KMeans(n_clusters=k), 
    			  folds = 5, 
    			  metric = "silhouette",
    			  debug_print = "off")			
    print(str(k) + " k: " + str(score))
    if score > best_score:
        best_score = score
        ideal_k = k;
    scores[k-2] = score

print("ideal k: " + str(ideal_k))

kmeans = KMeans(n_clusters=ideal_k).fit(trans_data)
print(kmeans.labels_)
print(kmeans.inertia_)

viz.visualize(trans_data, kmeans.labels_, two_d = True, three_d = False, plot_name="kmeans_2d")
viz.visualize(trans_data, kmeans.labels_, two_d = False, three_d = True, plot_name="kmeans_3d")

np.savetxt("./output/kmeans_scores.csv", scores, delimiter=",")
