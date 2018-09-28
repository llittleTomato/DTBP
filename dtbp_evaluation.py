__author__ = 'sky'

import BP.data_loader as data_loader
import BP.network2 as network2


if __name__ == '__main__':
    # 读取训练数据
    evaluation_data = list(data_loader.load_data("data/data_evaluation_12.csv"))

    net = network2.load('dtbp_net.json')

    # 查看结果
    for i in range(0,12):
        print('*'*20)
        print(evaluation_data[i][1], net.feedforward(evaluation_data[i][0]))