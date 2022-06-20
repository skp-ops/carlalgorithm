'''

涉及到的题目
LeetCode 349、350

'''

'''
leetcode 349
给定两个数组nums1和nums2 ，返回 它们的交集。输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序 。

示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]

示例 2：
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]
解释：[4,9] 也是可通过的

https://leetcode.cn/problems/intersection-of-two-arrays
'''
# 解法一，用python自带的求交集的位运算符
#           补充：交集 &； 并集 |； 补集 -； 全交除去交集 ^
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

# 解法二
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        record = []
        if len(nums1) >= len(nums2):
            for i in range(len(nums2)):
                if nums2[i] in nums1:
                    record.append(nums2[i])
        else:
            for i in range(len(nums1)):
                if nums1[i] in nums2:
                    record.append(nums1[i])

        return list(set(record))


'''
leetcode 350
给你两个整数数组nums1 和 nums2 ，请你以数组形式返回两数组的交集。返回结果中每个元素出现的次数，应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。可以不考虑输出结果的顺序。

示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]

示例 2:
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]

https://leetcode.cn/problems/intersection-of-two-arrays-ii
'''
# 普通解法
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        record = []
        if len(nums1) >= len(nums2):
            for i in range(len(nums2)):
                if nums2[i] in nums1:
                    record.append(nums2[i])
                    nums1.remove(nums2[i])
        else:
            for i in range(len(nums1)):
                if nums1[i] in nums2:
                    record.append(nums1[i])
                    nums2.remove(nums1[i])
        return record

# 双指针，官方解法
# 如果两个数组是有序的，则可以使用双指针的方法得到两个数组的交集。
# 首先对两个数组进行排序，然后使用两个指针遍历两个数组。
# 初始时，两个指针分别指向两个数组的头部。每次比较两个指针指向的两个数组中的数字，如果两个数字不相等，则将指向较小数字的指针右移一位，
# 如果两个数字相等，将该数字添加到答案，并将两个指针都右移一位。当至少有一个指针超出数组范围时，遍历结束。
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        length1, length2 = len(nums1), len(nums2)
        intersection = list()
        index1 = index2 = 0
        while index1 < length1 and index2 < length2:
            if nums1[index1] < nums2[index2]:
                index1 += 1
            elif nums1[index1] > nums2[index2]:
                index2 += 1
            else:
                intersection.append(nums1[index1])
                index1 += 1
                index2 += 1

        return intersection
