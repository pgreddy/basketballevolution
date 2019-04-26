import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visualize(data, clusters, two_d = True, three_d = False, plot_name="matplot"):
    num_pcs = data.shape[1];
    fig = plt.figure()

    file_name = plot_name + ".png"
    if (two_d and (num_pcs >= 2)):
        plt.scatter(data[:,0], data[:,1], c = clusters)
    
        plt.xlabel('PC 1')
        plt.ylabel('PC 2')
    elif(three_d and (num_pcs >= 3)):
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(data[:,0], data[:,1], data[:,3], c = clusters)
    
        ax.set_xlabel('PC 1')
        ax.set_ylabel('PC 2')
        ax.set_zlabel('PC 3')
    else:
        return

    plt.title("Data")

    plt.savefig(file_name)
    plt.show()

    return
