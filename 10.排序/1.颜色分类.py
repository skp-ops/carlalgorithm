'''

涉及到的题目
LeetCode 75

'''
'''
leetcode 75
75. 颜色分类
给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
必须在不使用库的sort函数的情况下解决这个问题。

示例 1：
输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]

示例 2：
输入：nums = [2,0,1]
输出：[0,1,2]
'''


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        当curr指针指向0时，和最左边的数调换位置，然后缩小左边的边界，curr指针递增；
        当curr指针指向2时，和最右边的数调换位置，然后缩小右边的边界，
            但curr指针不用递增，因为还要判断一次现在的curr指针指向的是1还是0，如果是0还要再转换一次；
        当curr指针指向1时，不需操作，只用递增curr指针就行，因为所有的0都在左边，1都在中间，2都在右边；
        '''
        left_boundary, right_boundary = 0, len(nums)
        curr = 0
        if right_boundary == 1: return
        while curr < right_boundary:
            if nums[curr] == 0:
                nums[left_boundary], nums[curr] = nums[curr], nums[left_boundary]
                curr += 1
                left_boundary += 1
            elif nums[curr] == 1:
                curr += 1
            else:
                right_boundary -= 1
                nums[right_boundary], nums[curr] = nums[curr], nums[right_boundary]

