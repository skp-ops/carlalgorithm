'''

涉及到的题目
leetcode 238

'''
'''
leetcode 238
238. 除自身以外数组的乘积
给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
请不要使用除法，且在 O(n) 时间复杂度内完成此题。

示例 1:
输入: nums = [1,2,3,4]
输出: [24,12,8,6]

示例 2:
输入: nums = [-1,1,0,-3,3]
输出: [0,0,9,0,0]
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''dp_left[i]表示第i个数之前所有数字的乘积
        dp_right[i]表示第i个数之后所有数字的乘积
        要计算除开i其他数的乘积，就是将dp_left[i]与dp_right[i]相乘即可'''
        dp_left = [1 for _ in range(len(nums))]
        dp_right = [1 for _ in range(len(nums))]
        res = []
        for i in range(1, len(nums)):
            dp_left[i] = dp_left[i-1]*nums[i-1]
            dp_right[-i-1] = dp_right[-i]*nums[-i]
        for j in range(len(nums)):
            res.append(dp_left[j]*dp_right[j])
        return res