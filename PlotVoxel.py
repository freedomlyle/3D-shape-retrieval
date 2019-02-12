import matplotlib.pyplot as plt  # 绘图用的模块
from mpl_toolkits.mplot3d import Axes3D  # 绘制3D坐标的函数
import numpy as np
import os
from matplotlib import cm


def plotVoxel(vox, boxSize):
# plot
#     x = vox[:, 0]
#     y = vox[:, 1]
#     z = vox[:, 2]
    # ax = plt.axes(projection='3d')
    # ax.scatter3D(x, y, z, cmap='Greens')
    # plt.show()
    (row, col) = vox.shape;
    P = np.zeros((8, 3))
    face = np.zeros((4, 6))
    F = np.array([[1, 2, 3, 4], [1, 2, 6, 5], [1, 4, 8, 5], [3, 4, 8, 7], [3, 2, 6, 7], [5, 6, 7, 8]])
    M = np.array([[0, 0, 0], [-1, 0, 0], [-1, -1, 0], [0, -1, 0], [0, 0, -1], [-1, 0, -1], [-1, -1, -1], [0, -1, -1]])
    X = np.array([0, 0, 0])
    Y = np.array([0, 0, 0])
    Z = np.array([0, 0, 0])
    for i in range(0, row):
        point = vox[i, :]
        P = point + M
        for j in range(0, 5):
            index = F[j, :]
            facePoint = P[index, :]
            X = np.hstack((X, facePoint[:, 1]))
            Y = np.hstack((Y, facePoint[:, 2]))
            Z = np.hstack((Z, facePoint[:, 3]))

    return;

if __name__ == '__main__':
    vox = np.array([[1,1,1]])
    plotVoxel(vox=vox, boxSize=64)