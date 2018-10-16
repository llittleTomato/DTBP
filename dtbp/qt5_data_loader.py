import numpy as np


def load_data(f):
    xin = np.loadtxt(f, dtype=float, delimiter=',', skiprows=0, usecols=(0, 1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15,16))
    # 归一化数据
    xin = sigmoid(xin, 1)
    training_input = [np.reshape(xin, (17, 1))]
    return training_input


# 归一化函数
def sigmoid(x, usestatus=1):
    if usestatus:
        return 1.0 / (1 + np.exp(x))
    else:
        return x
