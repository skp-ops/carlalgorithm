'''

涉及到的题目
leetcode 404

'''
'''
leetcode 404
404. 左叶子之和
给定二叉树的根节点 root ，返回所有左叶子之和。

示例 1：
输入: root = [3,9,20,null,null,15,7] 
输出: 24 
解释: 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24

示例 2:
输入: root = [1]
输出: 0
'''
# 此题中只有处于叶子节点的左节点才能被相加，所以在代码中要创建一个函数来判断是否为叶子节点

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''递归法'''
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def sum_left(root):
            if root is None: return 0
            left = sum_left(root.left)
            right = sum_left(root.right)
            cur = 0
            if root.left and not root.left.left and not root.left.right:
                cur = root.left.val # 该节点有左节点，且左节点为叶子节点，那么就记录其值
            return cur + left + right
        return sum_left(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_leaf(self, root):
        if not root.left and not root.right:
            return True
        else:
            return False
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        '''迭代法'''
        queue = collections.deque([root])
        res = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    if self.is_leaf(node.left): # 如果是叶子节点，记录值
                        res += node.left.val
                    else:
                        queue.append(node.left) # 如果不是叶子节点，继续append
                if node.right:
                    if not self.is_leaf(node.right): # 如果不是叶子节点，继续append
                        queue.append(node.right)
                    else:
                        continue # 如果是叶子节点，但是是右子树，我们不记录值
        return res