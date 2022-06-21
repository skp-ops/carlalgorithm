'''

0-1 背包理论基础

'''
'''
0-1背包的描述
有N件物品和一个最多能承受重量为W的背包，第i件物品的重量是weight[i]，得到的价值是value[i]
每件物品只能用一次，求解将哪些物品装入背包后物品价值的总和最大

对于暴力解法，每个物品都有两个状态取或者不取，利用回溯算法可以求出物品价值的最大总和
但是这种解法的时间复杂度为2^n,n为物品的数量，是一个指数级别的算法，需要用动态规划来优化
'''
############################################
#
#       背包承重： 4
#                 重量          价值
#   物品0           1            15
#   物品1           3            20
#   物品2           4            30
#
############################################
'''
利用dp五部曲来解决这个问题
1、确定dp数组以及下标的含义
二维数组 dp[i][j]  其中i为物品index，j为背包的重量
    则dp[i][j]的含义就是你当前能取的物品只有0-i，当前你只有一个小背包，所能拿到的最大价值（先解决这些小问题，再解决最终的大问题）
    而此时你就会作出两个不一样的选择，为了确定dp[i][j]的值，此时我已经有了dp[i-1][j]的价值
    那我其中一个选择就是不拿i，我当前的价值和上一个状态相比不变
           另外一个选择就是拿i，拿i就代表着我要腾出一部分的空间来放i，因为我拿了i，背包的价值肯定有一部分是value[i]
            现在背包还剩下的空间是[j-weight[i]]，那么剩下的空间最多能装多大的价值呢，那就是dp[i-1][j-weight[i]]
            此时我们就推导出了递推公式
                dp[i][j] = max(dp[i-1][j], value[i] + dp[i-i][j-weight[i]])
    初始化的操作，当背包空间为0的时候，不管i为多少，价值都为0，因为一个也装不了
                当一开始i为0的时候，说明只能拿这一件，再容量允许的范围内，价值都是该物品i本身的价值
                初始化的两个for循环可以替换位置
'''
# 二维数组代码：
def two_dimensional_vector(bag_size, weight, value):
    rows, cols = len(weight), bag_size + 1
    dp = [[0 for _ in range(cols)] for _ in range(rows)] # 创建一个二维矩阵

    # 初始化dp数组
    for i in range(rows): dp[i][0] = 0 # 第一列背包重量为0，价值总和为0
    first_item_weight, first_item_value = weight[0], value[0]
    for j in range(1,cols): # 第一行只有物品0，如果背包容量足够装下物品0，其价值就是该物品本身
        if first_item_weight <= j:
            dp[0][j] = first_item_value

    # 更新dp数组，先遍历物品，再遍历背包
    for i in range(1, len(weight)):
        for j in range(1,cols):
            if j < weight[i]: # 说明此时背包全部的容量都装不下i，只能不装i
                dp[i][j] = dp[i-1][j]
            else: # 说明此时装得下i，那么我们尝试装下i之后再计算当前价值哪个最大
                dp[i][j] = max(dp[i-1][j], value[i] + dp[i-1][j-weight[i]])
    print(dp)

if __name__ == '__main__':
    bag_size = 4
    weight = [1,3,4]
    value = [15,20,30]
    two_dimensional_vector(bag_size, weight, value)
#     [[0, 15, 15, 15, 15],
#     [0, 15, 15, 20, 35],
#     [0, 15, 15, 20, 35]]

'''                
用一维数组来记录dp[j]表示当前背包重量为j能装下价值最大的东西
    为什么能用一维数组来记录，因为我们分析二维数组的时候可以发现，在递推公式中 dp[i][j] = max(dp[i-1][j]......
    这里实际上就是将原来的值重新赋值给当前的值，所以滚动数组就可以用一个变量来维护
        即 dp[j] = max(dp[j], value[i] + dp[j-weight[i]])
        类似于斐波那契数列那样，a = f1, b = f2 ===> c = a+b , a, b = b, c
    初始化一维数组，dp[0] = 0，如果题目中给的'价值'都为正整数，则初始化都可以为0，一旦有负数
    在取最大值的时候，很有可能会把0给取到，这个时候初始化的数就不能为0，这点要注意
    同时遍历的顺序也变了，只能先遍历物品i，再遍历背包容量j
        且背包容量j要从后向前遍历，原因在于 dp[j-weight[i] 这个值的位置始终在dp[j]之前，我们在算 dp[j-weight[i] + value[i]的
        时候会重复计算。所以滚动数组的遍历方式为：
            先取物品0，从大背包开始算出当前最大价值，一直算到小背包
            再取物品1，从大背包开始，由于有了先前的记录值，再开始重新计算最大值
'''
# 一维数组代码
def one_dimensional_vector(bag_size, weight, value):
    # 创建并初始化数组
    dp = [0] * (bag_size + 1)
    # 先遍历物品，再遍历背包容量
    for i in range(len(weight)):
        for j in range(bag_size,weight[i]-1,-1): # 重要! 从最大容量bag_size,反向遍历到当前能装下物品i的最大容量
            dp[j] = max(dp[j], value[i] + dp[j-weight[i]])
    print(dp)
one_dimensional_vector(bag_size=4, weight=[1,3,4], value=[15,20,30])
# [0, 15, 15, 20, 35]