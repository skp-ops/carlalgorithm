'''

涉及到的题目
LeetCode 509

'''
'''
leetcode 509
509. 斐波那契数
斐波那契数 （通常用 F(n) 表示）形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
F(0) = 0，F(1) = 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
给定 n ，请计算 F(n) 。

示例 1：
输入：n = 2
输出：1
解释：F(2) = F(1) + F(0) = 1 + 0 = 1

示例 2：
输入：n = 3
输出：2
解释：F(3) = F(2) + F(1) = 1 + 1 = 2

示例 3：
输入：n = 4
输出：3
解释：F(4) = F(3) + F(2) = 2 + 1 = 3
'''
# 递归的方式可以实现，但是时间复杂的是O(2^n)，非常的耗时
class Solution:
    '''题目中已经给了我们清晰的递推公式，所以确定完首项就可以直接用递归'''
    def fib(self, n: int) -> int:
        if n <= 1: return n # 首项，同时也是结束循环的标识
        res = self.fib(n-1) + self.fib(n-2)
        return res

# 考虑迭代法
class Solution:
    '''迭代法是拿空间换时间
    假如我们n=4，我们用递归法计算会发现我们每次计算的过程是
    f4 = f3 + f2
        f3 = f2 + f1
            f2 = f1 + f0
                f1 = f1
                f0 = f0
            f1 = f1
        f2 = f1 + f0
            f1 = f1
            f0 = f0
    有非常多的重复计算，所以假如我们能用一个哈希表记录以及算过的值，就可以免去很多计算
    从而大大降低时间复杂度，但是相应的空间复杂度增加'''
    def fib(self, n: int) -> int:
        if n <= 1: return n
        dp = [0]*(n+1) # dp[i]表示第i个斐波那契数的值
        dp[0], dp[1] = 0, 1 # 初始化dp数组
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2] # 递推公式，遍历的顺序就是从前向后
        return dp[n]

class Solution:
    '''在递归中添加一个哈希表来记录已经计算过的值'''
    def __init__(self):
        self.memo = {}
    def fib(self, n: int) -> int:
        if n <= 1: return n
        if n in self.memo:
            return self.memo[n]
        else:
            self.memo[n] = self.fib(n-1) + self.fib(n-2)
        return self.memo[n]

class Solution:
    '''分析可以发现，其实整个过程只需要两个变量即可满足题目要求
    不断更新两个变量的数值，一个代表dp[i-1]一个代表dp[i-2]'''
    def fib(self, n: int) -> int:
        if n <= 1: return n
        a, b = 0, 1
        c = 0
        for i in range(1,n):
            c = a + b # 相当于dp[i] = dp[i-2] + dp[i-1]
            a, b = b, c # 将dp[i]赋值给dp[i-1]；dp[i-1]赋值给dp[i-2]
        return c