'''

涉及到的题目
leetcode 226

'''
'''
leetcode 226
226. 翻转二叉树
给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。

示例 1：
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]

示例 2：
输入：root = [2,1,3]
输出：[2,3,1]

示例 3：
输入：root = []
输出：[]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    '''迭代法'''
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None: return None
        queue = deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                node.left, node.right = node.right, node.left # 此题的关键在于翻转，所以左右节点交换位置即可
                if node.right: queue.append(node.right)
                if node.left: queue.append(node.left)
        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    '''递归法'''
    def invertTree(self, root: TreeNode) -> TreeNode:
        '''中-左-右的遍历顺序'''
        def swap(root):
            if root is None: return None # 终止循环条件：如果碰到空节点就返回None
            root.left, root.right = root.right, root.left # 先交换，交换完来再向下遍历寻找
            if root.left: swap(root.left)
            if root.right: swap(root.right)
            return root
        return swap(root)