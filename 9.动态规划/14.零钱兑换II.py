'''

涉及到的题目
leetcode 518

'''
'''
leetcode 518
518. 零钱兑换 II
给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。
请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。
假设每一种面额的硬币有无限个。 
题目数据保证结果符合 32 位带符号整数。

示例 1：
输入：amount = 5, coins = [1, 2, 5]
输出：4
解释：有四种方式可以凑成总金额：
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

示例 2：
输入：amount = 3, coins = [2]
输出：0
解释：只用面额 2 的硬币不能凑成总金额 3 。

示例 3：
输入：amount = 10, coins = [10] 
输出：1

'''
class Solution:
    '''完全背包，要算出填满背包有多少种情况
    dp[x]表示要凑齐x元，一共有多少种方法
    因为求的是组合问题，遍历的顺序不能变，先遍历硬币，用完一种硬币再用下一种
    这样不会重复计算，如果需要求排列数，就将两个循环调换位置'''
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for i in range(len(coins)): # 先遍历物品
            for j in range(coins[i], amount + 1): # 再正向遍历背包重量
                dp[j] = dp[j] + dp[j - coins[i]]
        return dp[-1]