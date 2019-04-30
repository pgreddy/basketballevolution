import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def _get_title(graph_type):
    print('Please input title for the ' + graph_type + ' graph: ')
    return input()

def visualize(data, clusters, two_d = True, three_d = False, plot_name="matplot"):
    num_pcs = data.shape[1];
    fig = plt.figure()

    file_name = plot_name + ".png"
    if (two_d and (num_pcs >= 2)):
        plt.scatter(data[:,0], data[:,1], c = clusters)

        plt.xlabel('PC 1')
        plt.ylabel('PC 2')
        plt.title(_get_title('2D'))
    elif(three_d and (num_pcs >= 3)):
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(data[:,0], data[:,1], data[:,3], c = clusters)

        ax.set_xlabel('PC 1')
        ax.set_ylabel('PC 2')
        ax.set_zlabel('PC 3')
        plt.title(_get_title('3D'))
    else:
        return


    plt.savefig(file_name)
    plt.show()

    return

def visualize_year(data, year1=2001, year2=2016, color1='r', color2='b', plot_name="matplot"):
    training = data[:, 1:]
    trainingyear1 = training[data[:,0] == year1]
    trainingyear2 = training[data[:,0] == year2]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    #ax.scatter(training[:,0], training[:,1], training[:,3], color = '0.75')
    ax.scatter(trainingyear1[:,0], trainingyear1[:,1], trainingyear1[:,3], facecolor = 'g')
    ax.scatter(trainingyear2[:,0], trainingyear2[:,1], trainingyear2[:,3], facecolor = 'b')

    ax.set_xlabel('PC 1')
    ax.set_ylabel('PC 2')
    ax.set_zlabel('PC 3')

    plt.title(_get_title('year'))

    plt.savefig(file_name)
    plt.show()

def visualize_player(data, playerid1=1713, playerid2=201939, playerid3=101106, playercolor1='b', playercolor2='g', playercolor3='r', plot_name="matplot"):
    training = data[:, 1:]
    trainingplayer1 = training[data[:,0] == playerid1]
    trainingplayer1 = np.sort(trainingplayer1, 0)
    trainingplayer2 = training[data[:,0] == playerid2]
    trainingplayer2 = np.sort(trainingplayer2, 0)
    trainingplayer3 = training[data[:,0] == playerid3]
    trainingplayer3 = np.sort(trainingplayer3, 0)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    #ax.scatter(training[:,0], training[:,1], training[:,3], color = '0.75')
    #ax.scatter(training[:,0], training[:,1], training[:,3], color = '0.75')
    ax.plot(trainingplayer1[:,0], trainingplayer1[:,1], trainingplayer1[:,3], color = playercolor1)
    ax.plot(trainingplayer2[:,0], trainingplayer2[:,1], trainingplayer2[:,3], color = playercolor2)
    ax.plot(trainingplayer3[:,0], trainingplayer3[:,1], trainingplayer3[:,3], color = playercolor3)

    ax.set_xlabel('Year')
    ax.set_ylabel('PC 1')
    ax.set_zlabel('PC 2')

    plt.title(_get_title('player'))

    plt.savefig(file_name)
    plt.show()
