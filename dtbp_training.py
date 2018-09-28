import BP.data_loader as data_loader
import BP.network2 as network2


if __name__ == '__main__':
    # 读取训练数据
    training_data = list(data_loader.load_data("data/dadta100.csv"))


    # 创建神经网络模型，输入为模型结构 [Neural_Number_Input，Neural_Number_Hidden，Neural_Number_Output],
    # cost为损失函数QuadraticCost类或者CrossEntropyCost类
    net = network2.Network([17, 35, 3], cost=network2.CrossEntropyCost)

    # 训练神经网络（训练数据，迭代次数，每组训练数据数量，学习速率（在network中，实际学习速率=学习速率/每组训练数据数量））
    # net.SGD(training_data, 200, 10, 0.2, lmbda=0.5, evaluation_data=validation_data, monitor_evaluation_accuracy=True)
    net.SGD(training_data, 200, 1, 0.1, lmbda=0.000001, monitor_training_cost=True)

    # 保存神经网络模型
    net.save('dtbp_net.json')
