from sklearn.decomposition import PCA

# Use PCA to get 95% of the variance of passed in data
def get_pca (data):

    pca = PCA(n_components=0.95, svd_solver='full')
    trans_data = pca.fit_transform(data)

    print('PCA components: ')
    print(pca.components_)
    print('PCA explained variance: ')
    print(pca.explained_variance_ratio_)

    return pca, trans_data
