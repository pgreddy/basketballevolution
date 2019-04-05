from sklearn.cluster import KMeans
import numpy as np

data_full = np.genfromtxt('../../data/data_v1/final/training_data_v1_final.csv', delimiter=',')
# Remove the first two columns which include data
training = data_full[:,2:]
kmeans = KMeans(n_clusters=10).fit(training)
print(kmeans.labels_)
print(kmeans.inertia_)
