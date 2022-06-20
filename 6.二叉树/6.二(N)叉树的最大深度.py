'''

涉及到的题目
leetcode 104、559

'''
'''
leetcode 104
104. 二叉树的最大深度
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。
示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''递归法'''
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        res = set()
        def traversal(root, depth):
            res.add(depth)
            if root.left: traversal(root.left, depth + 1)
            if root.right: traversal(root.right, depth + 1)
        traversal(root, 0)
        return max(res) + 1 # 由于一开始depth给的默认值为0，实际表示第一层，所以最后答案加1
# 递归法二
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
利用迭代法来求，就是要计算这个树的高度，最底层为0
'''
class Solution:
    '''递归法二'''
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def get_depth(root):
            if not root: return 0 # 结束迭代的条件，遇到空节点，则树的高度为0
            left_depth = get_depth(root.left)
            right_depth = get_depth(root.right)
            # 遍历顺序是左右中，先一直不断向下寻找，直到碰到空节点，此时return0，depth变成1
            # 然后从下往上一直return最大深度，最后return到父节点，就是最大深度
            depth =1 + max(left_depth , right_depth)
            return depth
        return get_depth(root)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    '''迭代法'''
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        queue = deque([root])
        res = 0
        while queue:
            size = len(queue)
            res += 1
            for _ in range(size):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return res

'''
leetcode 559
559. N 叉树的最大深度
给定一个 N 叉树，找到其最大深度。
最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
N 叉树输入按层序遍历序列化表示，每组子节点由空值分隔（请参见示例）。

示例 1：
输入：root = [1,null,3,2,4,null,5,6]
输出：3

示例 2：
输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
输出：5
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None: return 0
        queue = deque([root])
        res = 0
        while queue:
            size = len(queue)
            res += 1
            for _ in range(size):
                node = queue.popleft()
                for chl in node.children:
                    queue.append(chl)
        return res
