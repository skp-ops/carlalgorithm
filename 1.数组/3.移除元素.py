'''

涉及到的题目
LeetCode 27、26、283、977

'''

'''
leetcode 27移除元素
给你一个数组 nums和一个值 val，你需要 原地 移除所有数值等于val的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
示例 1：
输入：nums = [3,2,2,3], val = 3
输出：2, nums = [2,2]
解释：函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。你不需要考虑数组中超出新长度后面的元素。例如，函数返回的新长度为 2 ，
而 nums = [2,2,3,3] 或 nums = [2,2,0,0]，也会被视作正确答案。

示例 2：
输入：nums = [0,1,2,2,3,0,4,2], val = 2
输出：5, nums = [0,1,4,0,3]
解释：函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。
注意这五个元素可为任意顺序。你不需要考虑数组中超出新长度后面的元素。

https://leetcode-cn.com/problems/remove-element

'''

# 暴力解法，直接remove
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        for i in range(nums.count(val)):
            nums.remove(val)
        return len(nums)

# 解法二，双指针法
#       通过一快，一慢两个指针在一个for循环里面完成两个for循环的工作
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        fast, slow = 0, 0  # 首先将快慢指针下标都初始化为0
        while fast < len(nums):
            if nums[fast] != val:  # 快指针先移动，如果不等于val，则慢指针跟上
                nums[slow] = nums[fast]  # 快指针不等于val，快慢指针同步运动
                slow += 1  # 记录慢指针的位置，慢指针指的位置永远不是val
            fast += 1  # 假如快指针等于val，则继续向右移动
        return slow

'''
leetcode 26
给你一个 升序排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，
返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。
由于在某些语言中不能改变数组的长度，所以必须将结果放在数组nums的第一部分。
更规范地说，如果在删除重复项之后有 k 个元素，那么nums的前 k 个元素应该保存最终结果。
将最终结果插入nums 的前 k 个位置后返回 k 。
不要使用额外的空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

示例 1：
输入：nums = [1,1,2]
输出：2, nums = [1,2,_]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。

示例 2：
输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。

https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array

'''
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != nums[slow]:  # 判断快指针指的和慢指针指的是否不一样
                slow += 1
                nums[slow] = nums[fast]  # 假如不一样，则慢指针向右移动，并且把快指针赋值给慢指针
            fast += 1
        return slow + 1

'''
leetcode 283
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
请注意 ，必须在不复制数组的情况下原地对数组进行操作。

示例 1:
输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]

示例 2:
输入: nums = [0]
输出: [0]
'''
# 思路：快指针走在前面，如果判断不是0，则快慢同时向前走。快指针一但碰到0，慢指针停止。
#       直到快指针指向下一个不为0的元素，调换快慢指针当前所指的元素，然后慢指针向右移动，重复操作，直到遍历结束
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] == 0:
                fast += 1
            else:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
                fast += 1

'''
leetcode 977

给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

示例 1：
输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]

示例 2：
输入：nums = [-7,-3,2,3,11]
输出：[4,9,9,49,121]

https://leetcode-cn.com/problems/squares-of-a-sorted-array

'''
# 暴力解法，将所有元素平方，然后排序
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # 暴力解法
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        nums.sort()
        return nums

# 第二种解法，观察nums可以知道，这个非降序排列的数组，里面的元素平方后最大值一定出现在最左边或者最右边
# 所以，我们设置左右两个指针，同时生成一个res数组来接收最大值，每比较一次，将最大值放在res的最右边
# 同时更新nums的左右两指针位置，每填充一次res，更新res指针的位置。
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left, right = 0, len(nums) - 1  # nums的指针，一个在左边，一个在右边
        res = [1]*len(nums)  # 生成一个与原数组容量一样的数组，用来接收比较的最大值
        site = len(res) - 1  # 新数组的指针，从右向左移动，每次填充完最大值，向左移动一个
        while right >= left:
            if nums[right] ** 2 > nums[left] ** 2:
                res[site] = nums[right] ** 2  # 如果nums右边数值平方更大，则把该值填入res的site处
                right -= 1  # 更新nums的右指针
            else:
                res[site] = nums[left] ** 2  # 如果nums左边数值平方更大，或者左右相等，则把该值填入res的site处
                left += 1  # 更新nums的左指针
            site -= 1  # 更新res的指针
        return res