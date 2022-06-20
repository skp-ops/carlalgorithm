'''

涉及到的题目
LeetCode 491

'''
'''
leetcode 491
给你一个整数数组 nums ，找出并返回所有该数组中不同的递增子序列，递增子序列中 至少有两个元素 。你可以按 任意顺序 返回答案。
数组中可能含有重复元素，如出现两个整数相等，也可以视作递增序列的一种特殊情况。

示例 1：
输入：nums = [4,6,7,7]
输出：[[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

示例 2：
输入：nums = [4,4,3,2,1]
输出：[[4,4]]

https://leetcode.cn/problems/increasing-subsequences

'''
# 创建一个新函数来判断当前字符串是否为递增数列，然后再利用字典去重，时间复杂度和空间复杂度都比较高，下面给出优化方案
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        hashtable = dict()

        def increasing(varlist):
            slow, fast = 0, 1
            while fast < len(varlist):
                if varlist[slow] > varlist[fast]:
                    return False
                else:
                    fast += 1
                    slow += 1
            return True

        def backtracking(nums, start_index):
            temp = []
            temp = [str(l) for l in path[:]]
            # 由于path里的元素都是数字，不能直接用join，所以要把他们转化成字符串

            if len(path) > 1 and increasing(path):
                hashtable['.'.join(temp[:])] = hashtable.setdefault('.'.join(temp[:]), 0) + 1
                # 哈希表优化去重，这里用一个点来join是为了防止出现[1,2,3,12,13]这样的数据，
                # 例如此时path是[1,2,13]，如果不用点来链接，哈希表的key值就是'1213'，
                # 这样在遍历[12,13]的时候，哈希表认为此时的key也是'1213'，就会被认定为重复值而舍弃。
                if hashtable['.'.join(temp[:])] > 1:  # 重复解去掉
                    return
                else:
                    res.append(path[:])

            if start_index == len(nums):  # 树遍历到最低端返回
                return

            for i in range(start_index, len(nums)):
                path.append(nums[i])
                backtracking(nums, i + 1)
                path.pop()

        backtracking(nums, 0)
        return res

# 解法二，对于判断是否为递增数列，我们只需要判断每次append进path里的元素是否大于path最后的一个元素即可
#   如果大于，就append进去，如果小于，则说明不可取，然后遍历下一个数字。
#   同时还应该去除重复解，当不适用哈希表来去重时，我们可以用集合来确定，因为本nums不是ordered，
#   所以我们不能用 i > start_index and nums[i] == nums[i-1]来判断，我们只能将每次遍历的元素add到一个集合中
#   再来判断接下来之后遍历的元素是否存在于这个集合，如果存在就继续遍历，如果不存在就append到path里，从而达到去重的效果
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtracking(nums, start_index):
            if len(path) > 1:  # 当path里的元素大于1个，就说明这个解可以被append到res里
                res.append(path[:])

            if start_index == len(nums):  # 遍历到树的最低端，开始返回
                return
            used_element = set()  # 每次在同一层搜索时，set都要clear，重新添加已经使用过的元素
            for i in range(start_index, len(nums)):  # 单循环逻辑
                if (path and nums[i] < path[-1]) or nums[i] in used_element:
                    # 如果当前元素小于前一个，或者目前遍历的元素在该层已经使用过了，就开始遍历下一个，跳过本次的append
                    continue
                used_element.add(nums[i])  # 将用过的元素添加到集合里
                path.append(nums[i])
                backtracking(nums, i + 1)
                path.pop()

        backtracking(nums, 0)
        return res

# 解法二，但是用哈希表去重。nums[i]的范围是-100 到 +100,这样我们创建一个由201个False组成的数组，
# 前100个位置留给负数，第101个位置留给0，后面100个位置留给正数，如果append进path一个数字，该数字对应的位置变为True
# 在之后append前进行判断，如果要append数字的位置为True说明该元素已经被选择了，那么就不能重复选择，从而继续接下来的循环
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtracking(nums, start_index):
            if len(path) > 1:  # 当path里的元素大于1个，就说明这个解可以被append到res里
                res.append(path[:])

            if start_index == len(nums):  # 遍历到树的最低端，开始返回
                return
            used_element = [False] * 201  # nunms[i] 的范围是-100到+100,一共有201个元素
            for i in range(start_index, len(nums)):  # 单循环逻辑
                if (path and nums[i] < path[-1]) or used_element[nums[i] + 100] is True:
                    # 如果当前元素小于前一个，或者目前遍历的元素在该层已经使用过了，就开始遍历下一个，跳过本次的append
                    continue
                used_element[nums[i] + 100] = True  # 将用过的元素添加到集合里
                path.append(nums[i])
                backtracking(nums, i + 1)
                path.pop()

        backtracking(nums, 0)
        return res
