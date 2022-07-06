'''

涉及到的题目
leetcode 152

'''
'''
leetcode 152
152. 乘积最大子数组
给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
测试用例的答案是一个 32-位 整数。
子数组 是数组的连续子序列。

示例 1:
输入: nums = [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。

示例 2:
输入: nums = [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''dp[i][0]表示当前i的数值
           dp[i][1]表示包含i在内可以组成的最大数
           dp[i][2]表示包含i在内可以组成的最小数'''
        dp = [[0,0,0] for _ in range(len(nums))]
        dp[0] = [nums[0], nums[0], nums[0]]
        for i in range(1, len(nums)):
            dp[i][0] = nums[i]
            dp[i][1] = max(nums[i], nums[i]*dp[i-1][1], nums[i]*dp[i-1][2], nums[i]*dp[i-1][0])
            dp[i][2] = min(nums[i], nums[i]*dp[i-1][1], nums[i]*dp[i-1][2], nums[i]*dp[i-1][0])
        res = -float('inf')
        for j in range(len(dp)):
            if dp[j][1] >res:
                res = dp[j][1]
        return res