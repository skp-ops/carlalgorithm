'''

涉及到的题目
leetcode 322

'''
'''
leetcode 322
322. 零钱兑换
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
你可以认为每种硬币的数量是无限的。

示例 1：
输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1

示例 2：
输入：coins = [2], amount = 3
输出：-1

示例 3：
输入：coins = [1], amount = 0
输出：0
'''
# 这道题可以看出，求的不是最大值，是最小值。但是同样都是最值，且都有amount作为限制条件
# 我们类比到背包问题就是每个硬币的value是1，重量就是coins，要装满背包需要的最小硬币个数
# 假如是求最大硬币个数，那就是很传统的一个背包问题，求最大价值，dp[j] = max(dp[j], dp[j-weight[i]] + value[i]]
# 那么要求最小价值，就是把max变成min即可。
# 初始化条件需要变一下，求最大值时初始成0没问题，但是求最小值，需要将dp数组初始化成amount + 1，理论最大值就是全部装1元的硬币，能装下最多，
# 那么数量就是amount，初始化为amount+1就可以在之后运算当中被函数min覆盖
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp =[0] + [amount+1]*(amount) # 最坏的情况就是全部拿1来凑，这里初始化一个最大值，在后面比较min时可以被覆盖掉
        for i in range(len(coins)):
            for j in range(coins[i], amount+1): # 完全背包正向遍历
                dp[j] = min(dp[j], dp[j-coins[i]]+1)
                # 如果改成max就是获得背包物品的价值最大，这里改成min就是价值最小
                # 价值对应的就是硬币的个数，价值最小说明所使用的硬币数最少
        return dp[-1] if dp[-1] < amount+1 else -1