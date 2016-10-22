import numpy as np


def exp_soomth(data, alpha):
    pre = np.tile([0.0], len(data) + 1)
    for i in range(1, len(data)):
        if i == 1:
            pre[i] = data[0]
        pre[i+1] = alpha * data[i] + (1-alpha) * pre[i]
    return pre

raw = [97, 95, 95, 92, 95, 95, 98, 97, 99, 95, 95, 96, 97, 98, 94, 95]
p1 = exp_soomth(raw, 0.1)
p2 = exp_soomth(raw, 0.3)
p3 = exp_soomth(raw, 0.9)
print(p1,'\n', p2, '\n', p3)
