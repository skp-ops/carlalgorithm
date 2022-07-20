'''

涉及到的题目
leetcode 543

'''
'''
leetcode 543
543. 二叉树的直径
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

示例 :
给定二叉树

          1
         / \
        2   3
       / \     
      4   5    
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
'''
'''
对于每个节点而言，以该节点为父节点能组成的直径长度是左子节点深度加上右子节点深度的和
例如对于1而言，左深度为2（2,4） 右深度为1（3）， 此时直径为2+1 = 3
对于2而言，左深度为1（4），右深度为1（5），此时直径为1+1 = 2
并且最长的直径可以能不会穿过头结点，所以要把每个节点当做父节点来计算一遍，从而获得最长直径
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root):
            nonlocal res
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)
            return max(left,right) + 1
        dfs(root)
        return res