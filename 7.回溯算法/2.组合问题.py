'''

涉及到的题目
LeetCode 77、216

'''
'''
leetcode 77
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
你可以按 任何顺序 返回答案。

示例 1：
输入：n = 4, k = 2
输出：
[  [2,4],  [3,4],  [2,3],  [1,2],  [1,3],  [1,4] ]

示例 2：
输入：n = 1, k = 1
输出：[[1]]

https://leetcode.cn/problems/combinations

'''
# 首先我们需要建立一个接收组合答案的数组，用res表示，
# 同时每次遍历完找到目标数组，需要将其append到res中，存放子组合的数组用path表示
# 紧接着建立回溯函数backtracking，需要的参数除了n，k，还需要一个起始坐标startindex
#     具体原因是，每次从集合中选取元素，可选择的范围逐渐收缩，而调整可选择的范围就需要使用startindex
#             例如在1.2.3.4中选择了1之后，下一曾递归时只能在[2,3,4]里选了，如何知道只能从2开始呢，就需要startindex

# 对于剪枝操作,分析n=4 k=4这种情况,符合条件的组合只有[1,2,3,4],那么如果没有剪枝,path的结果除了[1,2,3,4],系统还会做许多额外的操作
# 生成错误的组合包括([1][2][3][4][1,2][1,3][1,4][2,2][2,3][2,4][3,4][1,2,3][1,2,4][1,3,4][2,3,4]),这些都是白白浪费的时间
# 所以我们有必要进行剪枝操作来提高效率

# 如何减少循环次数,就需要在 for i in range里做改变,原来的range是(startindex,n+1),显然n+1的范围太大了,那么如何确定右边界的范围
#     例如在n=4,k=2中,每一个子集的循环,从第二个数开始都是没有意义的
#         (第一次取[1,],那之后回溯回来再取2,3,4([2,][3,][4,])就无意义了,因为长度肯定不够)
#     所以当前已经选择的元素个数len(path),还需要元素个数为k-len(path),
#     在集合n中,顶多遍历到n-(k-len(path))+1为止,再往后遍历长度就达不到要求了

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        def backtracking(n,k,startindex):
            if len(path) == k:
                res.append(path[:])
                # path[:]和 path.copy()才是等价的，path作为回溯的数组，
                # 是会动态改变的，如果你只将path的值加到result中，到最后会输出null或[]
                return # 循环终止条件
            last_index = n-(k-len(path)) + 1 # 剪枝过程
            for i in range(startindex,last_index + 1): # 搜索过程
                path.append(i)
                backtracking(n,k,i+1)
                path.pop() # 回溯过程

        backtracking(n,k,1) # 进入循环

        return res

'''
leetcode 216
216. 组合总和 III
找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：
只使用数字1到9
每个数字 最多使用一次 
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
'''
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []
        def backtracking(k,n,start):
            total = 0
            for i in path:
                total += i
            if total > n :
                return  # 剪枝操作
            elif total == n and len(path) == k: # 退出循环的条件
                res.append(path[:])
                return
            # 同样，在for循环范围上也可以进行剪枝，9-（k-len(path))+1
            for i in range(start,10-(k-len(path))+1): # 循环过程
                path.append(i)
                backtracking(k,n,i+1)
                path.pop()

        backtracking(k,n,1) # 进入循环
        return res