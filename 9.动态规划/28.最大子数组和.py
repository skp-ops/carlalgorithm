'''

涉及到的题目
leetcode 53

'''
'''
leetcode 53
53. 最大子数组和
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组 是数组中的一个连续部分。

示例 1：
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

示例 2：
输入：nums = [1]
输出：1

示例 3：
输入：nums = [5,4,-1,7,8]
输出：23
'''
# 在贪心算法章节中也出现过该题目，贪心的思想就是从后向前相加，记录当前最大和数，一旦和数变为负数，那么就舍弃
# 因为负数再往后加，得到的数一定会变小，这样遍历结束后返回那个最大和数即可
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''贪心，不断向后相加，保存其最大值
        一旦和变为负数，则舍弃，从下一位开始继续向后相加
        最后返回最大值'''

        ans = -float('inf')
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            ans = max(ans, temp)
            if temp <0:
                temp = 0
        return ans

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''dp[i]表示截止到第i个元素为止，最大的子数组和是多少
        dp[i]的确定条件有两个
            1. 之前i-1的和数与第i个数相加
            2. 本身第i个数
            比较哪种情况的数更大即可'''
        dp = [-10001]*len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
        return max(dp)