'''

涉及到的题目
LeetCode 216、39、40

'''


###########################################################
'''
组合问题：什么时候需要start_index呢？
    如果在一个集合中求元素组合，那么就需要start_index。如果时在多个集合中求元素组合，各个集合之间相互不影响，那么就不需要start_index.
'''
###########################################################


'''
leetcode 216
找出所有相加之和为n 的k个数的组合，且满足下列条件：
只使用数字1到9
每个数字最多使用一次
返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。

示例 1:
输入: k = 3, n = 7
输出: [[1,2,4]]
解释:
1 + 2 + 4 = 7
没有其他符合的组合了。

示例 2:
输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]
解释:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
没有其他符合的组合了。

示例 3:
输入: k = 4, n = 1
输出: []
解释: 不存在有效的组合。
在[1,9]范围内使用4个不同的数字，我们可以得到的最小和是1+2+3+4 = 10，因为10 > 1，没有有效的组合。

https://leetcode.cn/problems/combination-sum-iii

'''
# 树的宽度就是1,2,3,4,5,6,7,8,9. 所以在for循环中,右边区间是10,左边区间是start,每次从里面取一个,然后start+1
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []
        def backtracking(k,n,start):
            total = 0
            for i in path:
                total += i # 计算当前path一共相加起来等于多少
            if total > n :
                return  # 剪枝操作,加入超过n直接返回
            elif total == n and len(path) == k: # 找到目标path退出循环的条件
                res.append(path[:]) # 注入答案到res集合
                return

            # 同样，在for循环范围上也可以进行剪枝，9-（k-len(path))+1
            for i in range(start,10-(k-len(path))+1): # 循环过程
                path.append(i)
                backtracking(k,n,i+1)
                path.pop() # 回溯过程

        backtracking(k,n,1) # 进入循环
        return res

'''
leetcode 39
给你一个 无重复元素 的整数数组candidates 和一个目标整数target，
找出candidates中可以使数字和为目标数target 的 所有不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。
对于给定的输入，保证和为target 的不同组合数少于 150 个。

示例1：
输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。

示例2：
输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]

示例 3：
输入: candidates = [2], target = 1
输出: []

https://leetcode.cn/problems/combination-sum

'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res , path = [] , []
        if target == 0:
            return []
        def backtracking(candidates,target,start):
            temp = 0
            for i in path:
                temp += i # 计算path里各个数相加的总和
            if temp ==target: # 循环结束的判断
                res.append(path[:])
                return

            elif temp > target: # 剪枝操作，如果总和超过了target就返回
                return

            for i in range(start,len(candidates)): # 单循环的逻辑
                path.append(candidates[i])
                backtracking(candidates,target,i) # 由于元素可以重复，所以start就从i开始，如果不能重复，则start变成i+1
                path.pop()

        backtracking(candidates,target,0)
        return res

'''
leetcode 40
给定一个候选人编号的集合candidates和一个目标数target，找出candidates中所有可以使数字和为target的组合。
candidates中的每个数字在每个组合中只能使用一次。

注意：解集不能包含重复的组合。

示例1:
输入: candidates =[10,1,2,7,6,1,5], target =8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

示例2:
输入: candidates =[2,5,2,1,2], target =5,
输出:
[
[1,2,2],
[5]
]

https://leetcode.cn/problems/combination-sum-ii

'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []
        def backtracking(candidates,target,start):
            temp = 0
            for i in path:
                temp += i
            if temp == target: # 如果总和等于target，append结果
                res.append(path[:])
                return
            elif temp > target: # 剪枝操作，如果当前总和大于target，直接返回
                return

            for i in range(start,len(candidates)): # 单循环逻辑
                if candidates[i] > target: # 剪枝操作，如果单个元素i都大于target了，也直接返回
                    return
                if i > start and candidates[i] == candidates[i-1]:
                    # 剪枝操作，以candidates[1,1,2,5,6,7,10] 为例，当第一个1遍历完之后
                    # i指针走向第二个1，此时i如果大于start，说明开始进入第二个大循环了，因为在第一个大循环中
                    # i始终等于start，通过i>start就能判断出是否进入了第二个大循环，然后此时再判断i与i-1位置的元素是否一样
                    # 如果一样则会出现重复解，那么就用continue，继续for循环移动i的位置，直到i与i-1位置的元素不一样
                    # 这样子就有了新的元素进入，开始重新循环
                    continue
                path.append(candidates[i])
                backtracking(candidates,target,i+1)
                path.pop()
        backtracking(candidates,target,0)
        return res

# 其他思路的代码
'''
s 表示再candidates数组中遍历的起始位置
use 表示已经取到的数 组成的列表
remain 表示距离target还差的值

39.组合总和代码

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def find(s, use, remain):
            for i in range(s, len(candidates)):
                c = candidates[i]
                if c == remain:
                    ans.append(use + [c])
                    return
                if c < remain:
                    find(i, use + [c], remain - c)
                if c > remain:
                    return
        find(0, [], target)
        return ans
        
        
40.组合总和II代码

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def find(s,use,remain):
            for i in range(s,len(candidates)):
                c = candidates[i]
                if i>s and candidates[i-1]==candidates[i]:
                    continue
                if c == remain:
                    ans.append(use + [c])
                    return              
                if c < remain:
                    find(i+1,use + [c], remain - c)
                if c > remain:
                    return
        find(0,[], target)
        return ans

'''