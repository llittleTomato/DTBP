import numpy as np


def load_data(f):
    # 读入数据0-4列输入，4-6输出
    xin = np.loadtxt(f, dtype=float, delimiter=',', skiprows=1, usecols=(0, 1, 2, 3))
    yout = np.loadtxt(f, dtype=float, delimiter=',', skiprows=1, usecols=(4, 5, 6))
    # 归一化数据
    xin = sigmoid(xin, 1)
    # 将数据格式转换成需要的格式
    training_input = [np.reshape(x, (4, 1)) for x in xin]
    training_results = [np.reshape(y, (3, 1)) for y in yout]
    training_data = zip(training_input, training_results)
    return training_data


# 归一化函数
def sigmoid(x, usestatus=1):
    if usestatus:
        return 1.0 / (1 + np.exp(x))
    else:
        return x
