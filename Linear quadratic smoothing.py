import numpy as np


def simple_move_average(data, n):
    if data[0] == 0.0:
        for i in range(0, len(data)):
            if data[i] != 0:
                mark = i
                break
        temp = data[mark:]
    else:
        temp = data
    pre = np.tile([0.0], len(temp))
    for i in range(0, len(temp) - n + 1):
        if i is 0:
            k = i + n - 1
        else :
            k += 1
        pre[k] = sum(temp[i:i+n])/n
    if data[0] == 0.0:
        pred = list(data[0:mark]) + list(pre)
        pred = np.around(pred, decimals=3)
        return pred
    else:
        pre = np.around(pre, decimals=3)
        return pre


def cal_a_b(dat1, dat2, N):
    at = np.tile([0.0], dat1.shape[0])
    bt = np.tile([0.0], dat1.shape[0])
    for i in range(0, len(dat1)):
        if dat1[i] != 0 and dat2[i] != 0:
            at[i] = 2 * dat1[i] - dat2[i]
            bt[i] = (2/(N - 1)) * (dat1[i] - dat2[i])
    return at, bt


def predict(a, b, T):
    Ft = np.tile([0.0], a.shape[0]+1)
    for i in range(0, len(a)):
        if a[i] != 0.0:
            Ft[i+1] = a[i] + b[i] * T
    return Ft


pure = [125, 135, 195, 197, 186, 175, 155, 190, 220,219, 226, 198, 260, 245]
S1 = simple_move_average(pure, 3)
print(S1)
S2 = simple_move_average(S1, 3)
print(S2)
at, bt = cal_a_b(S1, S2, 3)
print(at, '\n', bt)
f = predict(at, bt, 1)
print(f)
