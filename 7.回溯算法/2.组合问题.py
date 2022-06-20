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

