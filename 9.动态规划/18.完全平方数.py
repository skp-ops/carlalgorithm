'''

涉及到的题目
leetcode 279

'''
'''
leetcode 279
279. 完全平方数
给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。
例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

示例 1：
输入：n = 12
输出：3 
解释：12 = 4 + 4 + 4

示例 2：
输入：n = 13
输出：2
解释：13 = 4 + 9
 
'''
# 本题可以换一个说法，转换成背包问题。现在有一系列平方数，1,4,9,16....
# 无限取用，凑出目标数n，返回使用平方数最少的数量
# 这里背包重量就是目标数n，每个物品的价值value是1，我们要求出最小的价值，那就是min函数
# 物品的取值范围如何确定？对n开根号，并且转换成整数，再加1，就是能取到的最大值。
class Solution:
    def numSquares(self, n: int) -> int:
        num = int(sqrt(n))+1
        num_arr = [i**2 for i in range(1,num)]
        dp = [0] + [n+1]*n
        for i in range(len(num_arr)):
            for j in range(num_arr[i], n+1):
                dp[j] = min(dp[j], dp[j-num_arr[i]]+1)
        return dp[-1]
