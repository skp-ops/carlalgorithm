'''

涉及到的题目
leetcode 496、503

'''

'''
leetcode 496
496. 下一个更大元素 I
nums1 中数字 x 的 下一个更大元素 是指 x 在 nums2 中对应位置 右侧 的 第一个 比 x 大的元素。
给你两个 没有重复元素 的数组 nums1 和 nums2 ，下标从 0 开始计数，其中nums1 是 nums2 的子集。
对于每个 0 <= i < nums1.length ，找出满足 nums1[i] == nums2[j] 的下标 j ，
并且在 nums2 确定 nums2[j] 的 下一个更大元素 。如果不存在下一个更大元素，那么本次查询的答案是 -1 。
返回一个长度为 nums1.length 的数组 ans 作为答案，满足 ans[i] 是如上所述的 下一个更大元素 。

示例 1：
输入：nums1 = [4,1,2], nums2 = [1,3,4,2].
输出：[-1,3,-1]
解释：nums1 中每个值的下一个更大元素如下所述：
- 4 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。
- 1 ，用加粗斜体标识，nums2 = [1,3,4,2]。下一个更大元素是 3 。
- 2 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。

示例 2：
输入：nums1 = [2,4], nums2 = [1,2,3,4].
输出：[3,-1]
解释：nums1 中每个值的下一个更大元素如下所述：
- 2 ，用加粗斜体标识，nums2 = [1,2,3,4]。下一个更大元素是 3 。
- 4 ，用加粗斜体标识，nums2 = [1,2,3,4]。不存在下一个更大元素，所以答案是 -1 。
'''
'''
本题可以这样去理解，因为num1中所有的元素一定会出现在nums2中，那么我们就只需要去研究nums2即可
把nums2中每个元素的下一个更大元素求出来，再映射回num1的坐标，得出最后的答案即可
将res初始化为[-1,-1,-1,-1....]
例如示例1： 
    对于nums2来说，1右边更大元素是3 》》 查找nums1中是否有1 》》 存在1 》》 更新res[-1,3,-1]
                  3右边更大的元素是4 》》 查找nums1中是否有3 》》 不存在3 》》 不更新res
                  4右边没有更大的元素 》》不更新res
                  2右边没有更大的元素 》》 不更新res
    最终返回[-1,3,-1]

例如示例2：
    对于num2来说，1右边更大的元素是2 》》 查找nuns1中是否有1 》》 不存在1 》》 不更新res
                 2右边更大的元素是3 》》 查找nums1中是否有2 》》 存在2 》》更新res[3,-1]
                 3右边更大的元素是4 》》 查找nums1中是否有3 》》 不存在3 》》 不更新res
                 4右边没有更大的元素 》》 不更新res
    最终返回[3,-1]
'''
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = [0]
        res = [-1 for _ in range(len(nums1))]
        for i in range(1, len(nums2)): # 对nums2写单调栈
            if nums2[i] <= nums2[stack[-1]]:
                stack.append(i)
            else:
                while stack and nums2[i] > nums2[stack[-1]]:
                    target_index = stack.pop()
                    if nums2[target_index] in nums1: # 假如被pop的元素出现在nums1中
                        res[nums1.index(nums2[target_index])] = nums2[i] # 更新答案
                stack.append(i)
        return res

'''
leetcode 503
503. 下一个更大元素 II
给定一个循环数组 nums （ nums[nums.length - 1] 的下一个元素是 nums[0] ），返回 nums 中每个元素的 下一个更大元素 。
数字 x 的 下一个更大的元素 是按数组遍历顺序，这个数字之后的第一个比它更大的数，
这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1 。

示例 1:
输入: nums = [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数； 
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。

示例 2:
输入: nums = [1,2,3,4,3]
输出: [2,3,4,-1,4]
'''
'''
将nums再重复一遍，变成newnums，这样再进行查找下一个更大的元素时，可以将整个环形数组全部查到
然后在修改答案列表的时候，长度仍然是nums数组的长度，所以只有当stack[-1]的坐标小于len(nums)的时候才修改
'''
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        new_nums = nums + nums
        res = [-1 for _ in range(len(nums))]
        stack = [0]
        for i in range(1, len(new_nums)):
            if new_nums[i] <= new_nums[stack[-1]]:
                stack.append(i)
            else:
                while stack and new_nums[i] > new_nums[stack[-1]]:
                    if stack[-1] < len(nums):
                        res[stack[-1]] = new_nums[i]
                    stack.pop()
                stack.append(i)
        return res