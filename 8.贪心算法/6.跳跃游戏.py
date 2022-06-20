'''

涉及到的题目
leetcode 55

'''
'''
55. 跳跃游戏
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标。

示例 1：
输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。

示例 2：
输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
'''
# 跳几步无所谓，关键在于可跳的覆盖范围是多少。
# 每次进入可跳区域，就算出最大能覆盖的范围。
# 判定结束的条件是：
#     最大覆盖范围无法覆盖到终点，返回Fales
    # 最大覆盖范围覆盖到终点并且，当前最大覆盖范围不会跳到0上面去，返回True
# 局部最优：每次取最大跳跃覆盖范围，且落点不为0
# 全局最优：最后得到总体的最大跳跃覆盖范围，判断是否能到终点
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        step = 0 # 记录最大覆盖范围
        zero = 0 # 记录0的位置
        if n == 1: return True
        for i in range(n-1):
            if nums[i] != 0:
                step = max(step,nums[i] + i) # 取当前覆盖的最大范围
            else:
                zero = max(zero,i) # 更新当前0的最大位置
            if zero >= step: # [0,2,2] [1,0,1,0]
                return False
        if step < n-1 :
            return False
        else:
            return True