'''

涉及到的题目
leetcode 98

'''
'''
leetcode 98
98. 验证二叉搜索树
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
有效 二叉搜索树定义如下：
节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

示例 1：
输入：root = [2,1,3]
输出：true

示例 2：
输入：root = [5,1,4,null,null,3,6]
输出：false
解释：根节点的值是 5 ，但是右子节点的值是 4 。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        递归法
        中序遍历时，判断当前节点是否大于中序遍历的前一个节点，
        如果大于，说明满足 BST，继续遍历；否则直接返回 false。
        '''
        cur = -float('inf')
        def check(root):
            nonlocal cur
            if not root: return True # 遍历到头，返回True

            left_check = check(root.left) # 左

            if root.val <= cur: return False # 不是递增序列
            else:cur = root.val

            right_check = check(root.right) # 右

            return left_check and right_check
        return check(root)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''利用数组来判断，中序遍历，看数组是否不重复且单调递增'''
        res = []
        def traversal(root):
            nonlocal res
            if not root:
                return
            traversal(root.left)
            res.append(root.val)
            traversal(root.right)
        traversal(root)
        for i in range(1,len(res)):
            if res[i] <= res[i-1]:
                return False
        return True