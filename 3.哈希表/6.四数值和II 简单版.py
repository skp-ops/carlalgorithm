'''

涉及到的题目
LeetCode 454

'''

'''
leetcode 454
给你四个整数数组 nums1、nums2、nums3 和 nums4 ，数组长度都是 n ，请你计算有多少个元组 (i, j, k, l) 能满足：
0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

示例 1：
输入：nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
输出：2
解释：
两个元组如下：
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0

示例 2：
输入：nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
输出：1

https://leetcode.cn/problems/4sum-ii

'''

# 这道题相较于四数值和，区别在于这个题给了四个单独的数组，而不是同一个数组，这样可以避免讨论重复解的问题。而且题目也只需要输出能够打成目标的解的个数就好。
# 常规思路是四个for循环，但是时间复杂度为n^4，会直接超时，所以利用哈希表来完成。
# 将1,2两个数组看成一个大组，3,4两个数组看成一个大组。为这两个大组分别创建两个哈希表dict。
# dict的key储存两个数组中元素两两相加的结果，value储存相加结果出现的次数。然后遍历其中一个dict的key值，查找0-key在不在另外一个数组中，如果在的话
# 就说明这四个数组合起来能等于0,例如dict1的key为1,出现了6次,dict2中key为-1,出现了5次,说明一共能凑成6*5=30组解,然后记录下来,最后输出所有的解

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        d12 = dict()
        d34 = dict()
        record = 0
        for i in nums1:
            for j in nums2:
                d12[i + j] = d12.setdefault(i + j, 0) + 1
        for i in nums3:
            for j in nums4:
                d34[i + j] = d34.setdefault(i + j, 0) + 1

        for key in d12.keys():
            if 0 - key in d34:
                record += (d12[key] * d34[0 - key])

        return record