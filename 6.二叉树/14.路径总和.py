'''

涉及到的题目
leetcode 112

'''
'''
leetcode 112
112. 路径总和
给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。判断该树中是否存在 根节点到叶子节点 的路径，
这条路径上所有节点值相加等于目标和 targetSum 。如果存在，返回 true ；否则，返回 false 。
叶子节点 是指没有子节点的节点。

示例 1：
输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
输出：true
解释：等于目标和的根节点到叶节点路径如上图所示。

示例 2：
输入：root = [1,2,3], targetSum = 5
输出：false
解释：树中存在两条根节点到叶子节点的路径：
(1 --> 2): 和为 3
(1 --> 3): 和为 4
不存在 sum = 5 的根节点到叶子节点的路径。

示例 3：
输入：root = [], targetSum = 0
输出：false
解释：由于树是空的，所以不存在根节点到叶子节点的路径。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        '''回溯法'''
        total = []
        YorN = []
        def backtracking(root):
            if not root: return
            total.append(root.val)
            if not root.left and not root.right:
                if sum(total) == targetSum: # 遍历到叶子节点，开始计算是否满足target
                    YorN.append(1) # 如果满足就将1append到YorN里
            backtracking(root.left)
            backtracking(root.right)
            total.pop()
        backtracking(root)
        if not YorN:
            return False
        else:
            return True

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        '''递归法'''
        if not root: return False # 空节点则不满足要求
        if not root.left and not root.right :
            return root.val == targetSum
        # 每次向左或向右进行递归的时候，targetSum都要减去当前父节点的值，左右路径中只要找出一条满足题目要求的目标值即可，所以用or连接
        return self.hasPathSum(root.left,targetSum-root.val) or self.hasPathSum(root.right,targetSum-root.val)


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        '''迭代法'''
        if not root: return False
        queue = collections.deque()
        queue.append((root, root.val))
        while queue:
            size = len(queue)
            for _ in range(size):
                node, value = queue.popleft()
                if not node.left and not node.right and value == targetSum:
                    return True
                if node.left:
                    queue.append((node.left,value + node.left.val))
                if node.right:
                    queue.append((node.right,value + node.right.val))
        return False

'''
leetcode 113
113. 路径总和 II
给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
叶子节点 是指没有子节点的节点。

示例 1：
输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：[[5,4,11,2],[5,8,4,5]]

示例 2：
输入：root = [1,2,3], targetSum = 5
输出：[]

示例 3：
输入：root = [1,2], targetSum = 0
输出：[]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        temp = []
        def backtracking(root,rest):
            if not root: return # 退出循环的条件

            temp.append(root.val) # 单循环逻辑
            if not root.left and not root.right:
                if rest == root.val:
                    res.append(temp[:])

            backtracking(root.left,rest-root.val) # 左节点递归
            backtracking(root.right,rest-root.val) # 右节点递归
            temp.pop() # 回溯
        backtracking(root,targetSum) # 进入递归
        return res
