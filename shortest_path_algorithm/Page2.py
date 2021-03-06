# -*- coding: utf-8 -*-
import   numpy  as  np

a = np.array([[0, 1, 1, 0],
           [1, 0, 0, 1],
           [1, 0, 0, 1],
           [1, 1, 0, 0]], dtype=float)  # dtype指定为float


def graphMove(a):  # 构造转移矩阵
    b = np.transpose(a)  # b为a的转置矩阵
    c = np.zeros((a.shape), dtype=float)
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            c[i][j] = a[i][j] / (b[j].sum())  # 完成初始化分配
    # print c,"\n===================================================="
    return c


def firstPr(c):  # pr值得初始化
    pr = np.zeros((c.shape[0], 1), dtype=float)  # 构造一个存放pr值得矩阵
    for i in range(c.shape[0]):
        pr[i] = float(1) / c.shape[0]
        # print pr,"\n==================================================="
    return pr


def pageRank(p, m, v):  # 计算pageRank值
    while ((v == p * np.dot(m, v) + (
        1 - p) * v).all() == False):  # 判断pr矩阵是否收敛,(v == p*dot(m,v) + (1-p)*v).all()判断前后的pr矩阵是否相等，若相等则停止循环
        v = p * np.dot(m, v) + (1 - p) * v
    return v


if __name__ == "__main__":
    M = graphMove(a)
    print(M)
    pr = firstPr(M)
    print(pr)
    p = 0.85  # 引入浏览当前网页的概率为p,假设p=0.8
    print(pageRank(p, M, pr))  # 计算pr值