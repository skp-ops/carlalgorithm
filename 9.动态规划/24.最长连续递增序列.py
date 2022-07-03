'''

涉及到的题目
leetcode 674

'''
'''
leetcode 674
674. 最长连续递增序列
给定一个未经排序的整数数组，找到最长且 连续递增的子序列，并返回该序列的长度。
连续递增的子序列 可以由两个下标 l 和 r（l < r）确定，如果对于每个 l <= i < r，都有 nums[i] < nums[i + 1] ，
那么子序列 [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] 就是连续递增子序列。

示例 1：
输入：nums = [1,3,5,4,7]
输出：3
解释：最长连续递增序列是 [1,3,5], 长度为3。
尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为 5 和 7 在原数组里被 4 隔开。 

示例 2：
输入：nums = [2,2,2,2,2]
输出：1
解释：最长连续递增序列是 [2], 长度为1。
'''
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        '''动态规划
        由于是要求连续的递增序列，所以每次判断状态的时候只需要跟前一个元素比较即可
        初始化都为1，因为一个元素的长度为1
        如果后面的数大于前面的数，则dp[后] = dp[前] + 1
        否则就不改变，保持初始值1，说明遇到不是递增的元素了，长度变为初始'''
        dp = [1]*len(nums)
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = max(dp[i], dp[i-1]+1)
        return max(dp)

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        '''贪心or指针
        遍历一次数组，记录当前最长递增序列的长度
        遇到不合法的元素，count就变为1，重新开始计数
        维护res始终是最大值即可'''
        count = 1
        res = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count += 1
            else:
                res = max(res, count)
                count = 1
        res = max(res, count)
        return res