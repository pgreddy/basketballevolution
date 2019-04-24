from sklearn.mixture import GaussianMixture
import numpy as np

data_full = np.genfromtxt('../../../data/data_v1/final/training_data_v1_final.csv', delimiter=',')
# Remove the first two columns which include data
training = data_full[:,2:]

mixtures = GaussianMixture(n_components=3).fit(training)
print(mixtures.weights_)
