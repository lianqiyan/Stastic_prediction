import numpy as np


def update_weights(dat, w, p, k):
    error = np.tile(1000, len(dat)-p)
    while abs(error).sum() > 0.00001:
        for i in range(p, len(dat)):
            temp = dat[i-2:i]
            hat = np.around(sum(temp[::-1] * w), 0)
            error[i-p] = data[i] - hat
            w = np.around(w + p*k*error[i-p]*temp[::-1], 3)
            print(hat, w)
        print(error)
    return w


def calculate_k(dat, p):
    t_index = np.argsort(dat)
    t_max = dat[t_index[len(dat)-p:]]
    k = np.around(1.0/sum(np.power(t_max, 2)), 4)
    return k


data = np.array([43, 45, 48, 50, 53])
k = calculate_k(data, 2)
fi = np.tile(1/2, 2)
weight = update_weights(data, fi, 2, k)
predict = np.around(sum(weight * data[3:5]), 0)
print(predict)
