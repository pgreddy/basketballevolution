from sklearn.mixture import GaussianMixture
import numpy as np

data_full = np.genfromtxt('../../../data/data_v1/final/training_data_v1_final.csv', delimiter=',')
# Remove the first two columns which include data
training = data_full[0:20,2:]
test = data_full[21:40,2:]

mixtures = GaussianMixture(n_components=3).fit(training)
mixutures_labels = mixtures.predict(test)

print(mixutures_labels)
