'''

涉及到的题目
LeetCode 46、47

'''
'''
leetcode 46
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

示例 1：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

示例 2：
输入：nums = [0,1]
输出：[[0,1],[1,0]]

示例 3:
输入：nums = [1]
输出：[[1]]

https://leetcode.cn/problems/permutations

'''
# 此题是排列问题，所以不需要start_index，但是需要注意的是，他能重复取同一个元素，所以我们要依赖哈希表去重
class Solution:
    def permute(self,nums):
        res = []
        path = []
        used_element = [False] * 21 # 创建一个哈希表来控制每次纵向遍历的时候是否选择了重复的元素
        def backtracking(nums):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in nums:
                if used_element[i + 10] is True:
                    continue
                used_element[i + 10] = True
                path.append(i)
                backtracking(nums)
                path.pop()
                used_element[i + 10] = False
                #  由于是纵向遍历，所以回溯的时候，哈希表的记录值也要变化
                #  这个地方与横向遍历的哈希表去重不一样，横向遍历不需要回溯时发生变化，因为在每次for循环之前，哈希表统一格式化

        backtracking(nums)
        return res

# 不用哈希表去重的方法，就是添加一个判断，假如此时遍历的元素存在于path里面，则continue，如果不存在就append到path里
# 但是该方法用时比哈希表去重要多
class Solution:
    def permute(self,nums):
        res = []
        path = []

        def backtracking(nums):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in nums:
                if i in path: # 去重的过程
                    continue
                path.append(i)
                backtracking(nums)
                path.pop()
        backtracking(nums)
        return res

'''
leetcode 47
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

示例 1：
输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
 
示例 2：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

https://leetcode.cn/problems/permutations-ii

'''
# 建立两个哈希表，一个来控制循环树时横向重复的问题，一个来控制循环树时纵向重复的问题
# 横向的哈希表不需要回溯，每次循环都清零
# 纵向的哈希表需要回溯，每次回溯都是更新状态的行为
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        index_record = [False] * len(nums)
        # 这个表是用来控制坐标不重复，在遍历树的纵向方向不重复
        # 举个例子nums = [1,1,2]，其全排列是[[1,1,2],[1,2,1],[2,1,1]]
        # 如果没有控制坐标重复，那么他会出现[1,1,1] [2,2,2]以及其他的重复解的情况
        # 同时，为什么不能用start_index来控制，因为这个是排列问题，例如在选取了2当作path的首数字时
        # 我们需要返回到前面继续遍历[1,1]，如果利用start_index来约束，则会漏掉这些解

        def backtracking(nums):
            if len(nums) == len(path):
                res.append(path[:])
                return
            used_element = set()
             # 这个set用来控制同一层中重复选取的元素，在同一层中不能重复选取
             # 如果重复选了，则会出现多个解的问题，例如在nums = [1,1,2]中，path的首字母为1的情况有两种
             # 一种是path[0]=nums[0],第二种是path[0]=nums[1],如果不限制,则会产生两组重复解
            for i in range(len(nums)):
                if index_record[i] is True or nums[i] in used_element:
                    # 假设纵向遍历有重复或者横向遍历有重复,就继续循环
                    continue
                used_element.add(nums[i])  # 改变横向遍历哈希表状态
                index_record[i] = True  # 改变纵向遍历哈希表状态

                path.append(nums[i])
                backtracking(nums)
                path.pop() # path回溯
                index_record[i] = False # 控制纵向不重复的哈希表要记得回溯,调整其TF的关系

        backtracking(nums)
        return res