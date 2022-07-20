'''

涉及到的题目
leetcode 287

'''
'''
leetcode 287
287. 寻找重复数
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。
假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。
你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。

示例 1：
输入：nums = [1,3,4,2,2]
输出：2

示例 2：
输入：nums = [3,1,3,4,2]
输出：3
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        我们不要考虑数组,只需要考虑 数字都在 1 到 n 之间
        示例 1:
        arr = [1,3,4,2,2] 此时数字在 1 — 5 之间
        mid = (1 + 5) / 2 = 3 arr小于等于的3有4个(1,2,2,3)，1到3中肯定有重复的值
        mid = (1 + 3) / 2 = 2 arr小于等于的2有3个(1,2,2)，1到2中肯定有重复的值
        mid = (1 + 2) / 2 = 1 arr小于等于的1有1个(1)，2到2中肯定有重复的值
        所以重复的数是 2 '''
        left, right = 1, len(nums)
        while left < right:
            count = 0
            mid = left + (right-left)//2
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                right = mid
            else:
                left = mid + 1
        return right