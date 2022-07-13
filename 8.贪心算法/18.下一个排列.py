'''

涉及到的题目
LeetCode 31

'''
'''
31. 下一个排列
整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。
例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。
整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。
更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。
如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。

例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。
给你一个整数数组 nums ，找出 nums 的下一个排列。

必须 原地 修改，只允许使用额外常数空间。

示例 1：
输入：nums = [1,2,3]
输出：[1,3,2]

示例 2：
输入：nums = [3,2,1]
输出：[1,2,3]

示例 3：
输入：nums = [1,1,5]
输出：[1,5,1]

'''


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 从后向前遍历，如果遇到第一个非升序的元素，记录下来
        # 再次从后向前遍历，寻找大于这个元素的最小元素，交换位置
        # 再对该元素之后的元素进行排序
        # 与leetcode 556 下一个更大元素 III 思想类似
        i = j = len(nums) - 1
        target = -1
        while i > 0:
            if nums[i - 1] < nums[i]:
                target = nums[i - 1]
                idx = i - 1
                break
            i -= 1

        if target == -1:
            self.reverse(nums)
        else:
            while j > 0:
                if nums[j] > target:
                    break
                j -= 1
            nums[idx], nums[j] = nums[j], nums[idx]
            nums[idx + 1:] = sorted(nums[idx + 1:])

    def reverse(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
