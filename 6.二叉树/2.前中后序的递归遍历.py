'''

涉及到的题目
leetcode 144、145、94

'''
'''
递归函数，也即是回溯函数，一般用三部曲，在二叉树遍历中体现出来的就是：
    1、确定递归函数的参数和返回值
        我们只需要将树传递进函数即可，所以参数为root:TreeNode

    2、确定终止条件
        当遍历到最底层的时候，说明该分支已经遍历完毕，就返回
        root == None

    3、确定单层递归的逻辑
        不同的遍历方式，左中右的顺序不同，所以单层逻辑就是按照一定顺序取左中右的值
'''
'''
leetcode 144
144. 二叉树的前序遍历
给你二叉树的根节点 root ，返回它节点值的 前序 遍历。

示例 1：
输入：root = [1,null,2,3]
输出：[1,2,3]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]

示例 4：
输入：root = [1,2]
输出：[1,2]

示例 5：
输入：root = [1,null,2]
输出：[1,2]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''递归算法'''
        res = []
        def traversal(root):
            if root == None:
                return
            res.append(root.val) # 中 先append中间值
            traversal(root.left) # 左
            traversal(root.right) # 右
        traversal(root)
        return res

'''
leetcode 145
145. 二叉树的后序遍历
给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 。

示例 1：
输入：root = [1,null,2,3]
输出：[3,2,1]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''递归算法'''
        res = []
        def traversal(root):
            if root == None:
                return
            traversal(root.left) # 左
            traversal(root.right) # 右
            res.append(root.val) # 中 最后append中间值
        traversal(root)
        return res

'''
leetcode 94
94. 二叉树的中序遍历
给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。

示例 1：
输入：root = [1,null,2,3]
输出：[1,3,2]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''递归算法'''
        res = []
        def traversal(root):
            if root == None:
                return
            traversal(root.left) # 左
            res.append(root.val) # 中 第二步append中间数值
            traversal(root.right) # 右
        traversal(root)
        return res