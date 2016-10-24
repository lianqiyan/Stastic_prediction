import numpy as np


def cal_coef(mat):
    x1 = [None] * len(mat)
    for i in range(0, len(mat)):
        x1[i] = sum(mat[0:i+1])
    x1 = np.around(x1, decimals=3)
    csum = np.matrix(np.tile(None, [len(mat)-1, 2]))
    Yn = np.matrix(mat[1:]).transpose()
    for i in range(0, csum.shape[0]):
        csum[i, 0] = -1/2 * (x1[i] + x1[i+1])
        csum[i, 1] = 1
    B = np.asmatrix(csum)
    print(B, Yn)
    a = np.linalg.inv(B.transpose() * B)# * B.transpose() * Yn
    print(csum, type(csum), a)

data = [26.7, 31.5, 32.8, 34.1, 35.8, 37.5]
cal_coef(data)
