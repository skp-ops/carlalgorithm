'''

多重背包理论基础

'''
'''
有N种物品和一个容量为V的背包
每种物品可以用的个数为[M1,M2,M3....Mi]
每种物品的价值为[V1,V2,V3....Vi]
每种物品的重量为[W1,W2,W3....Wi]
求解将哪些物品装入背包可以使这些物品耗费的空间总和不超过背包容量，且价值总和最大

多重背包和01背包非常相似
因为在多重背包中物品a有x个可以使用，转化为01背包就是有x个物品a，每个只能使用一次
转化之后多重背包问题可以转为01背包解决
'''


def test_multi_pack1():
    '''版本一：改变物品数量为01背包格式'''
    weight = [1, 3, 4]
    value = [15, 20, 30]
    nums = [2, 3, 2]
    bag_weight = 10
    for i in range(len(nums)):
        # 将物品展开数量为1
        while nums[i] > 1:
            weight.append(weight[i])
            value.append(value[i])
            nums[i] -= 1

    dp = [0] * (bag_weight + 1)
    # 遍历物品
    for i in range(len(weight)):
        # 遍历背包
        for j in range(bag_weight, weight[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

    print(" ".join(map(str, dp)))


def test_multi_pack2():
    '''版本：改变遍历个数'''
    weight = [1, 3, 4]
    value = [15, 20, 30]
    nums = [2, 3, 2]
    bag_weight = 10

    dp = [0] * (bag_weight + 1)
    for i in range(len(weight)):
        for j in range(bag_weight, weight[i] - 1, -1):
            # 以上是01背包，加上遍历个数
            for k in range(1, nums[i] + 1):
                if j - k * weight[i] >= 0:
                    dp[j] = max(dp[j], dp[j - k * weight[i]] + k * value[i])

    print(" ".join(map(str, dp)))


if __name__ == '__main__':
    test_multi_pack1()
    test_multi_pack2()