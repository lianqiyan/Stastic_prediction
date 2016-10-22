import numpy as np


def simple_move_aveage(data, n):
    pre = np.tile([0.0], [len(data) + 1])
    for i in range(0, len(data)):
        if i+n > len(data):
            break
        if i is 0:
            k = i + n
        else :
            k += 1
        pre[k] = sum(data[i:i+n])/n
    print(pre)

data = [46, 50, 59, 57, 55, 64, 55, 61, 45, 49, 46]
simple_move_aveage(data, 1)
simple_move_aveage(data, 3)
