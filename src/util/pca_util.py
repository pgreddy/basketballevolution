from sklearn.decomposition import PCA

def get_pca(n_components, data):

    pca = PCA(n_components)
    trans_data = pca.fit_transform(data)

    print('PCA components: ')
    print(pca.components_)
    print('PCA explained variance: ')
    print(pca.explained_variance_ratio_)

    return pca, trans_data
