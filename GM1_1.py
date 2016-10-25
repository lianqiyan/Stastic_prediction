import numpy as np
import numpy.matlib


def cal_coef(mat):
    x1 = np.cumsum(mat)
    B = np.matlib.zeros([len(mat)-1, 2])
    Yn = np.matrix(mat[1:]).transpose()
    for i in range(0, B.shape[0]):
        B[i, 0] = -1/2 * (x1[i] + x1[i+1])
        B[i, 1] = 1
    a = np.linalg.inv(B.transpose() * B) * B.transpose() * Yn
    return a

data = [26.7, 31.5, 32.8, 34.1, 35.8, 37.5]
cal_coef(data)
