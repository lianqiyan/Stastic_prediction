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
    predict = lambda x: n1 * np.exp(-a[0]*x) + n2
    p = (predict(np. linspace(0, mat.shape[0]-1, mat.shape[0]))).A1
    p_data = np.hstack((np.array(p[0]), np.diff(p)))
    p_data = np.around(p_data, 6)
    return p_data, predict


def get_std(dat):
    m = np.around(np.mean(dat), 5)
    s = np.sqrt(np.sum(np.power(dat - m, 2))/(dat.shape[0]-1))
    return s


def test_model(pdat, dat, pho):
    # Residual test
    abs_er = np.abs(pdat - dat)
    rel_er = abs_er/dat
    if np.max(rel_er) < 0.05:
        print("The model passed Residual Test, The accuracy of the model is high!")
    else:
        print("Residual Test failed, the accuracy of the model is not good enough")
    amin = np.min(abs_er)
    amax = np.max(abs_er)
    p = lambda x: (amin + pho*amax)/(x + pho*amax)
    # test r: the value of r should be bigger than 0.6 when pho is 0.5
    eta = p(abs_er)  # correlation coefficient
    r = np.sum(eta) / eta.shape[0]  # correlation degree
    if r > 0.6:
        print("The model passed Correlation Degree Test!")
    else:
        print("The degree of correlation is not good enough")
    p_std = get_std(dat)  # std of raw data
    abs_std = get_std(abs_er)  # std of absolute error
    c = abs_std/p_std
    S0 = 0.6745*p_std
    ei = np.abs(abs_er - np.mean(abs_er))
    p = np.sum(ei < np.tile(S0, len(ei)))/len(ei)
    if p > 0.95 and c < 0.35:
        print()
    # if np.sum(ei > np.tile(S0, len(ei))) == 0 and c < 0.35:
    #     print("The model was tested well")
    # else:
    #     print("Oh...It seems like not good enough")
    # print('C:', c, '\n', 'S0:', S0, '\n', 'ei:', ei)


data = np.array([26.7, 31.5, 32.8, 34.1, 35.8, 37.5])
pre, pr = GM(data)
test_model(pre, data, 0.5)
N8 = pr(7) - pr(6)
print('The prediction of No.8 is ', N8)
