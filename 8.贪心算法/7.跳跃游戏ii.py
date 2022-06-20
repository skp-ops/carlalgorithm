'''

涉及到的题目
leetcode 45

'''
'''
45. 跳跃游戏 II
给你一个非负整数数组 nums ，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。
假设你总是可以到达数组的最后一个位置。

示例 1:
输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
     
示例 2:
输入: nums = [2,3,0,1,4]
输出: 2
'''
# 思路，首选计算出每个位置上能够覆盖的最远位置，即i+nums[i]
# 然后我们又知道终点的位置是len-1，所以从头开始找最先能到达终点的位置为j
# 然后将终点位置更新为j的坐标，继续从头开始找最先能到达j的位置
# 再次更新坐标，直到该坐标为0，返回循环的次数。
# 局部最优：每次都找到离起点最近的位置，并记录查找次数
# 全局最优；到达起点停止查找，记录的次数是最少的


class Solution:
    def jump(self, nums: List[int]) -> int:
        def find_min(index):
            for j in range(len(a)):
                if a[j] >= index: # 如果j位置能覆盖到终点
                    return j # 返回j的坐标
        a = [i+nums[i] for i in range(len(nums)-1)]
        count = 0
        index = len(nums) - 1 # 初始化终点坐标
        while True:
            if index == 0: # 结束循环的条件
                return count
            index = find_min(index) # 更新终点坐标位置：为j的坐标
            count += 1