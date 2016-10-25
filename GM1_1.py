import numpy as np
import numpy.matlib


def GM(mat):
    x1 = np.cumsum(mat)
    B = np.matlib.zeros([len(mat)-1, 2])
    Yn = np.matrix(mat[1:]).transpose()
    for i in range(0, B.shape[0]):
        B[i, 0] = -1/2 * (x1[i] + x1[i+1])
        B[i, 1] = 1
    a = np.linalg.inv(B.transpose() * B) * B.transpose() * Yn
    n1 = data[0] - a[1]/a[0]
    n2 = a[1]/a[0]
    print(n1, n2)
    predict = lambda x: n1 * np.exp(-a[0]*x) + n2
    p = predict(np. linspace(0, 5, 6))
    print(p)
    print(np.diff(p))
    # return a

data = [26.7, 31.5, 32.8, 34.1, 35.8, 37.5]
GM(data)
