'''

涉及到的题目
LeetCode 873

'''
'''
leetcode 873
873. 最长的斐波那契子序列的长度
如果序列 X_1, X_2, ..., X_n 满足下列条件，就说它是 斐波那契式 的：
n >= 3
对于所有 i + 2 <= n，都有 X_i + X_{i+1} = X_{i+2}
给定一个严格递增的正整数数组形成序列 arr ，找到 arr 中最长的斐波那契式的子序列的长度。如果一个不存在，返回  0 。
（回想一下，子序列是从原序列 arr 中派生出来的，它从 arr 中删掉任意数量的元素（也可以不删），而不改变其余元素的顺序。
例如， [3, 5, 8] 是 [3, 4, 5, 6, 7, 8] 的一个子序列）

示例 1：
输入: arr = [1,2,3,4,5,6,7,8]
输出: 5
解释: 最长的斐波那契式子序列为 [1,2,3,5,8] 。

示例 2：
输入: arr = [1,3,7,11,12,14,18]
输出: 3
解释: 最长的斐波那契式子序列有 [1,11,12]、[3,11,14] 以及 [7,11,18] 。
'''
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        '''暴力法'''
        set_arr = set(arr)
        res = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                '''先枚举出前两个值，然后再用while循环去搜索和数在不在数组中'''
                a_1, a_2 = arr[i], arr[j]
                count = 2 # 一开始a1 a2就已经占了两个位置了，所以count初始为2
                while a_1 + a_2 in set_arr:
                    count += 1
                    a_1, a_2 = a_2, a_1 + a_2 # 当和数存在于数组中，就类似斐波那契代码那样更新数据，继续搜索满足条件的
                    res = max(res, count)
        return res


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        '''dfs'''
        s = set(arr)
        def dfs(x, y):
            z = x + y
            return 1 + dfs(y, z) if z in s else 2
        res = max(dfs(x, y) for x, y in combinations(arr, 2))
        return res if res > 2 else 0


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        '''动态规划
        dp[i][j]表示的是以arr[i],arr[j]结尾的子序列中最长的斐波那契式的长度
            LEN = (..., ..., ..., ..., arr[i], arr[j])
        我们要向前寻找小于arr[i]的arr[k]，使得arr[k] = arr[j] - arr[i]
        所以dp[i][j] = max(3, dp[k][i] + 1)
        如果我们搜寻arr[k]依旧是从头到尾搜索就会超时，所以要建立一个哈希表，提前存储数据和下标
        '''
        hm = {val: idx for idx, val in enumerate(arr)}
        n = len(arr)
        res = 0
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n-1):
            for j in range(i+1, n):
                target = arr[j] - arr[i]
                if target in hm and target < arr[i]:
                    k = hm[target]
                    dp[i][j] = max(3, dp[k][i]+1)
                    res = max(res, dp[i][j])
        return res