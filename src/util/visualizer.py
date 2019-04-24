import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visualize(data, clusters, two_d = True, three_d = False):
    if (two_d):
        plt.scatter(data[:,0], data[:,1], c = clusters)
    
        plt.xlabel('PC 1')
        plt.ylabel('PC 2')
    
        plt.title("Data")
    
        plt.show()
    
        plt.savefig("matplotlib_2d.png")
    elif(three_d):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(data[:,0], data[:,1], data[:,3], c = clusters)
    
        ax.set_xlabel('PC 1')
        ax.set_ylabel('PC 2')
        ax.set_zlabel('PC 3')
    
        plt.title("Data")
    
        plt.show()
    
        plt.savefig("matplotlib_3d.png")
    else:
        return

    return
