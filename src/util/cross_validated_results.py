import numpy as np
import sys
import pandas as pd 
import matplotlib.pyplot as plt

sys.path.append('./src/util/')

import visualizer as viz
import evaluator as cross_val
import pca_util

kmeans_path = "./output/kmeans_scores.csv"
data_kmeans = np.genfromtxt(kmeans_path, delimiter=',')

agglom_path = "./output/agglom_scores.csv"
data_agglom = np.genfromtxt(agglom_path, delimiter=',')

mixmod_path = "./output/mixmod_scores.csv"
data_mixmod = np.genfromtxt(mixmod_path, delimiter=',')

df = pd.DataFrame({
	'Clusters':list(range(2, 18)),
    'KMeans':data_kmeans,
    'Agglomerative':data_agglom,
    'Mixture':data_mixmod
})

print(df)

ax = plt.gca()

df.plot(kind='line',x='Clusters',y='KMeans',ax=ax)
df.plot(kind='line',x='Clusters',y='Agglomerative', color='red', ax=ax)
df.plot(kind='line',x='Clusters',y='Mixture', color='green', ax=ax)
plt.ylabel('Silhouette Metric')

plt.plot(4, df['KMeans'].max(), marker='o', markersize=8, color="gray")
plt.plot(3, df['Agglomerative'].max(), marker='o', markersize=8, color="gray")
plt.plot(4, df['Mixture'].max(), marker='o', markersize=8, color="gray")

plt.savefig("cv_scores.png")
plt.show()
