'''

涉及到的题目
leetcode 111

'''
'''
leetcode 111
111. 二叉树的最小深度
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明：叶子节点是指没有子节点的节点。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：2

示例 2：
输入：root = [2,null,3,null,4,null,5,null,6]
输出：5
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
    def minDepth(self, root: TreeNode) -> int:
        if root is None: return 0
        queue = deque([root])
        depth = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node.left:queue.append(node.left)
                if node.right:queue.append(node.right)
                if not node.left and not node.right: # 这里返回depth的条件就是该子节点没有左右节点，说明已经遍历到最浅的尽头
                    return depth # 直接返回当前的深度即可
            depth += 1
        return depth

