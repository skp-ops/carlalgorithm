'''

涉及到的题目
leetcode 264、313

'''
'''
leetcode 264
264. 丑数 II
给你一个整数 n ，请你找出并返回第 n 个 丑数 。
丑数 就是只包含质因数 2、3 和/或 5 的正整数。

示例 1：
输入：n = 10
输出：12
解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。

示例 2：
输入：n = 1
输出：1
解释：1 通常被视为丑数。
'''

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        '''
        三指针法，每个指针代表着该位置需要乘以2or3or5
        初始时指针都指向0，同时乘上2.3.5，取最小的值（即乘上2的指针）
        那么指向2的指针index2需要向前移动一位，3,5指针不动，在后续乘的过程中3,5可能是最优解
        所以总体思路是，一旦哪个指针被选用，被乘了，那么指针就向前移动一位

        '''
        dp = [float('inf') for _ in range(n)]
        dp[0] = 1
        i_1, i_2, i_3 = 0, 0, 0
        for i in range(1,n):
            dp[i] = min(2*dp[i_1], 3*dp[i_2], 5*dp[i_3])
            if 2*dp[i_1] == dp[i]:
                i_1 += 1
            if 3*dp[i_2] == dp[i]:
                i_2 += 1
            if 5*dp[i_3] == dp[i]:
                i_3 += 1
        return dp[-1]

'''
leetcode 313
313. 超级丑数
超级丑数 是一个正整数，并满足其所有质因数都出现在质数数组 primes 中。
给你一个整数 n 和一个整数数组 primes ，返回第 n 个 超级丑数 。
题目数据保证第 n 个 超级丑数 在 32-bit 带符号整数范围内。

示例 1：
输入：n = 12, primes = [2,7,13,19]
输出：32 
解释：给定长度为 4 的质数数组 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。

示例 2：
输入：n = 1, primes = [2,3,5]
输出：1
解释：1 不含质因数，因此它的所有质因数都在质数数组 primes = [2,3,5] 中。
'''

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [float('inf') for _ in range(n)]
        dp[0] = 1
        pointers = [0 for _ in range(len(primes))] # 记录k个质数的指针
        for j in range(1,n): # 遍历dp数组
            change_index = -1
            for i in range(len(pointers)): # 遍历质数指针
                c = primes[i]*dp[pointers[i]]
                # 如果当前质因子乘它的丑数小于当前的丑数，更新当前丑数并更新变化坐标
                # i指针指的质数乘以当前已经遍历过的dp数组中的数，就是之后需要填写到dp表下一个位置的数
                if c < dp[j]: # 不断寻找最小的c以满足丑数的要求
                    change_index = i # 寻找到了当前最小的c，就记录下来之后需要更新的坐标
                    dp[j] = c # 同时填写当前的dp数组
                elif c == dp[j]: # 如果不同质数指针相乘之后遇到相等的情况，那么就去重，将该指针后移一位
                    pointers[i] += 1
            pointers[change_index] += 1 # 更新记录下来的质数指针
        return dp[-1]