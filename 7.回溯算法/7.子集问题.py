'''

涉及到的题目
LeetCode 78、90

'''


#################################
'''
如果把子集问题,组合问题,分割问题都抽象为一棵树,
    那么组合问题和分割问题就是收集树的叶子节点
    子集问题则是收集树的所有节点

在子集和排列组合的区别时,子集的元素没有顺序之分[1,2]与[2,1]都是一样的,所以遍历的时候,start_index要从i+1开始
但是排列组合的时候,[1,2]与[2,1]是不一样的,都要包含进去,所以遍历的时候,start_index要从0开始
'''
#################################



'''
leetcode 78
给你一个整数数组nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

示例 1：
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

示例 2：
输入：nums = [0]
输出：[[],[0]]

https://leetcode.cn/problems/subsets

'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        # res.append(path)
        def backtracking(nums,start_index):
            res.append(path[:]) # 无差别推入遍历的元素，因为树上的所有节点都需要
            if start_index == len(nums): # 终止条件就是集合为空，此时start_index就超过了列表下标
                return

            for i in range(start_index,len(nums)):
                path.append(nums[i])
                backtracking(nums,i+1) # 由于不能有重复元素，所以从start_index 从i+1开始
                path.pop()

        backtracking(nums,0)
        return res

'''
leetcode 90
给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。

示例 1：

输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]

示例 2：
输入：nums = [0]
输出：[[],[0]]

https://leetcode.cn/problems/subsets-ii

'''
# 解法一，跟78题类似，先将数组中的所有子集都求出来，然后再进行去重的操作，但是这样做会增加运行时间和内存
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        nums.sort() # 将数组排成有序数组

        def backtracking(nums,start_index):
            res.append(path[:]) # 无差别推入遍历的元素，因为树上的所有叶子节点都需要
            if start_index == len(nums): # 终止条件就是集合为空，此时start_index就超过了列表下标
                return

            for i in range(start_index,len(nums)):
                path.append(nums[i])
                backtracking(nums,i+1) # 由于不能有重复元素，所以从start_index 从i+1开始
                path.pop()

        backtracking(nums,0) # 去重操作
        b = []
        for i in res:
            if i not in b:
                b.append(i)

        return b

# 解法二
#     整体循环思路与解法一一样，只是增加了一个去重的代码
#     if i > start_index and nums[i] == nums[i - 1]
#     这个题目跟组合总和问题中类似，去除重复的项目就是要先对数组排序，例如[1,2,2,3]
#     当i遍历到第二个2的时候，这个时候就满足上面代码的条件，前后两个2是重复的，所以只考虑第一个2所组合的子集，
#     等遍历到第二个2的时候就从3开始遍历，这样就能去除重复。
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        nums.sort()

        def backtracking(nums, start_index):
            res.append(path[:])
            if start_index == len(nums): return

            for i in range(start_index, len(nums)):
                if i > start_index and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtracking(nums, i + 1)
                path.pop()

        backtracking(nums, 0)
        return res