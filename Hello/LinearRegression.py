# 调包
import  numpy as np
import  pandas as pd
# 使用sklearn库的linear_model(线性回归模型)
from sklearn import datasets, linear_model
# 均方差和r方
from sklearn.metrics import mean_squared_error, r2_score
# 画图
import matplotlib.pyplot as plt

# 1. 导入数据集(糖尿病)
diabetes = datasets.load_diabetes()
print(diabetes)
# data作为自变量, 二维
print("自变量data\n", diabetes.data)
# data有442个样本，10个特征(442行，10列)
print(diabetes.data.shape)
# target作为因变量, 一维
print("因变量target\n", diabetes.target)
# 442个因变量
print(diabetes.target.shape)
# 10个特征中的第3个特征作为x(第三列作为输入)
# :代表取所有行(所有样本)，newaxis表示增加一个纬度，2表示取索引为2的列(第三列)
diabetes_X = diabetes.data[:, np.newaxis, 2]
# 此时x还是一个二维矩阵
print(diabetes_X)
# 把diabetes.data(array格式)转化为DataFrame格式，然后随机抽取5列，axis=1代表从列抽取数据，这里的列就是特征
print(pd.DataFrame(diabetes.data).sample(5, axis=1))
# 打乱自变量数组
np.random.shuffle(diabetes_X)

# 线性回归的实现
# 训练集和测试集的划分
# 后20行作为测试集，其余作为训练集
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]
# 1.将线性回归模型实例化
regr = linear_model.LinearRegression()
# 2.使用训练集训练数据
regr.fit(diabetes_X_train, diabetes_y_train)
# 3.调用predict接口，使用训练好的模型对测试集的自变量进行预测
diabetes_y_pred = regr.predict(diabetes_X_test)

# 查看线性回归的系数
print("线性回归系数：", regr.coef_)
# 查看均方误差
print("均方误差：", mean_squared_error(diabetes_y_test, diabetes_y_pred))
# 查看r2, 越接近1表示模型越好
print("r2:", r2_score(diabetes_y_test, diabetes_y_pred))

# 查看分布
plt.scatter(diabetes_X_test, diabetes_y_test, color='black')
plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)
plt.xticks(())
plt.yticks(())
plt.show()