'''

涉及到的题目
leetcode 377

'''
'''
leetcode 377
377. 组合总和 Ⅳ
给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。请你从 nums 中找出并返回总和为 target 的元素组合的个数。
题目数据保证答案符合 32 位整数范围。

示例 1：
输入：nums = [1,2,3], target = 4
输出：7
解释：
所有可能的组合为：
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
请注意，顺序不同的序列被视作不同的组合。

示例 2：
输入：nums = [9], target = 3
输出：0
'''
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        '''target相当于背包重量，求能够装满背包的排列数
        排列和组合不一样，排列就有顺序了，应该先遍历背包重量，再遍历物品'''
        dp = [1] + [0] * target
        for i in range(target+1): # 先遍历背包重量
            for j in range(len(nums)): # 再遍历物品
                if i >= nums[j]:
                    dp[i] = dp[i] + dp[i - nums[j]]
        return dp[-1]