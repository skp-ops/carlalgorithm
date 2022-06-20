'''

涉及到的题目
leetcode 530

'''
'''
leetcode 530
530. 二叉搜索树的最小绝对差
给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
差值是一个正数，其数值等于两值之差的绝对值。

示例 1：
输入：root = [4,2,6,1,3]
输出：1

示例 2：
输入：root = [1,0,48,null,null,12,49]
输出：1
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        '''二叉搜索树是中序递增的，根据这个性质将其每个节点遍历出来，然后找出相减最小值'''
        res = []
        def traversal(root):
            if not root: return
            traversal(root.left)
            res.append(root.val)
            traversal(root.right)
        traversal(root)
        i = 0
        ans = float('inf')
        while i < len(res)-1:
            ans = min(ans,res[i+1]-res[i])
            i += 1
        return ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        '''二叉搜索树是中序递增的，根据这个性质将其每个节点遍历出来，然后找出相减最小值'''
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node:
                if node.right: stack.append(node.right)
                stack.append(node)
                stack.append(None)
                if node.left: stack.append(node.left)
            else:
                node = stack.pop()
                res.append(node.val)
        i = 0
        ans = float('inf')
        while i < len(res)-1:
            ans = min(ans, res[i+1]-res[i])
            i += 1
        return ans
