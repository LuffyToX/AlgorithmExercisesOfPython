# -*- coding: utf-8 -*-

""" 银行家算法

   一些数据结构：
                 可利用资源向量 Available
                 最大需求矩阵 Max
                 分配矩阵 Allocation
                 需求矩阵 Need

   (1) 如果 Request[i][j] <= Need[i][j], 便转向步骤 (2)；否则认为出错（超出自己所宣布的最大值）

   (2) 如果 Request[i][j] <= Available[j], 便转向步骤 (3)；否则需等待（尚无足够的资源）

   (3) 系统试探着把资源分配给进程 Pi，并修改下面数据结构中的数值：

       Available[j] = Available[j] - Request[i][j]
       Allocation[i][j] = Allocation[i][j] + Request[i][j]
       Need[i][j] = Need[i][j] - Request[i][j]

   (4) 系统执行安全性算法，检查此次资源分配后系统是否处于安全状态，如果安全，才将资源分配给该进程；
       否则，将本次的试探分配作废，恢复原来的资源分配状态，让进程 Pi 等待


   安全性算法

   两个向量：
            Work：  表示系统可提供给进程继续运行所需的各类资源数目，初始时 Work = Available
            Finish：表示系统是否有足够的资源分配给进程，使之运行完成，初始时 Finish[i] = False；当有足够资源分配给进程时，再令 Finish[i] = True

   (1) 从进程集合中找到一个能满足下述条件的进程，若找到，执行步骤 (2)；否则，执行步骤 (3)

       Finish[i] = False
       Need[i][j] <= Work[j]

   (2) 当进程 Pi 获得资源后，可顺利执行，直至完成，并释放分配给它的资源：

       Work[j] = Work[j] + Allocation[i][j]
       Finish[i] = True
       go to step 1

   (3) 如果所有进程的 Finish[i] = True 都满足，则表示系统处于安全状态；否则系统处于不安全状态

"""


import numpy as np


# 初始化银行家算法的数据结构（5 个进程，3 类资源）
Available = np.array([3, 3, 2])
Max = np.array([[7,5,3], [3,2,2], [9,0,2], [2,2,2], [4,3,3]])
Allocation = np.array([[0,1,0], [2,0,0], [3,0,2], [2,1,1], [0,0,2]])
Need = np.array([[7,4,3], [1,2,2], [6,0,0], [0,1,1], [4,3,1]])

safeList=[]            # 安全序列
Request=[]             # 请求向量
Request_name=""        # 进程名称


def input_Request():
    global Allocation, Available, Max, Need, safeList, Request, Request_name
    try:
        Request_name = int(input("请输入请求进程的编号：\n0   1    2    3    4\n"))
        Request_new = input("请输入进程 P{} 的请求向量:\n".format(Request_name)).split()
        for x in Request_new:
            Request.append(int(x))
        Request=np.array(Request)
    except:
        print("输入错误，请重新输入")
        input_Request()


def BankerAlgorithm():
    global Allocation, Available, Max, Need, safeList, Request, Request_name
    input_Request()

    if (Request <= Need[Request_name]).all():
        if (Request <= Available).all():
            Available -= Request
            Allocation[Request_name] += Request
            Need[Request_name] -= Request
            safeAlgorithm()
        else:
            print("尚无足够的资源，请等待")
    else:
        print("False！超出宣布的最大值")


def safeAlgorithm():
    Work = Available                                                                      #分配work向量
    Finish = [False]*5                                                                    #分配Finish向量
    cnt = 0
    while True:
        for i in range(0, 5):
            if Finish[i] == False and (Need[i] <= Work).all():
                for j in range(0, 3):
                    Work[j] += Allocation[i][j]
                Finish[i] = True
                safeList.append(i)
                cnt = 0
            else:
                cnt += 1
                continue
        if cnt >= 5:
            break

    if False in Finish:
        print("*"*45)
        print("您输入的请求资源数: {}".format(Request))
        print("您输入的请求进程是 P{}".format(Request_name))
        print("系统安全性：不安全状态")
        print("*"*45)
    else:
        print("*"*45)
        print("您输入的请求进程是 P{}".format(Request_name))
        print("您输入的请求资源数: {}".format(Request))
        print("系统安全性：系统安全")
        print("安全序列为：", safeList)
        print("*"*45)


if __name__ =="__main__":
    BankerAlgorithm()
