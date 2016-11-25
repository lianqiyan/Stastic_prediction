import numpy as np
import numpy.matlib


def GM(mat, n):
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
    p = (predict(np. linspace(0, n-1, n))).A1
    p_data = np.hstack((np.array(p[0]), np.diff(p)))
    p_data = np.around(p_data, 6)
    return p_data, predict


def get_std(dat):
    m = np.around(np.mean(dat), 5)
    s = np.sqrt(np.sum(np.power(dat - m, 2))/(dat.shape[0]-1))
    return s


def test_model(pdat, dat, pho):
    print()
    # Residual test
    abs_er = np.abs(pdat - dat)
    rel_er = abs_er/dat
    if np.max(rel_er) < 0.05:
        print("The model passed Residual Test, The accuracy of the model is high!")
    else:
        print("Residual Test failed, The accuracy of the model is not good enough")
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
        print("The model passed Posterior Difference Tests very well!")
    elif 0.8 < p < 0.95 and 0.35 < c < 0.5:
        print("The model passed Posterior Difference Tests1")
    elif 0.7 < p < 0.8 and 0.5 < c < 0.65:
        print("The model barely passed  Difference Tests！")
    elif p < 0.6 and c > 0.65 :
        print("The model failed  Difference Tests ")


data = np.array([2.430, 3.560, 2.780, 3.560, 4.560, 4.10,  5.40, 6.50, 8.450, 9, 10.20, 10.50, 9.890, 10.40, 11.3, 13.50, 12.8, 15.4, 14.3, 16.80])

pre, pr = GM(data, len(data) + 10)
# print('Prediction: ', pre)
test_model(pre[0:len(data)], data, 0.5)
