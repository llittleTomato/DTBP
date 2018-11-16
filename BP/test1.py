import numpy as np
import BP.data_loader as data_loader
import BP.network2 as network2
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # 读取训练数据
    training_data = data_loader.load_data1("Fisher's Iris Data.csv")
    training_data = list(training_data)

    # 创建神经网络模型，输入为模型结构 [Neural_Number_Input，Neural_Number_Hidden，Neural_Number_Output],
    # cost为损失函数QuadraticCost类或者CrossEntropyCost类
    net = network2.Network([4, 15, 3], cost=network2.CrossEntropyCost)

    # 训练神经网络（训练数据，迭代次数，每组训练数据数量，学习速率（在network中，实际学习速率=学习速率/每组训练数据数量））
    traincost = net.SGD(training_data, 300, 1, 0.1, lmbda=0.0, monitor_training_cost=True)

    # 保存神经网络模型
    net.save('test1.json')

    # 查看结果
    # print(training_data[128][1], net.feedforward(training_data[128][0]))
    x = np.linspace(1, 300, 300)
    y = np.array(traincost[2])
    plt.plot(x, y)
    plt.show()