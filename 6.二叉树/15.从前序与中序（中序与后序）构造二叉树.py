'''

涉及到的题目
leetcode 105、106

'''
'''
leetcode 105
105. 从前序与中序遍历序列构造二叉树
给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。

示例 1:
输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]

示例 2:
输入: preorder = [-1], inorder = [-1]
输出: [-1]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder: # 返回None的条件，当list为空的时候，说明遍历到空节点了。将None添加到树中
            return None
        root = TreeNode(preorder[0]) #1.先找到根节点
        index = inorder.index(root.val)#2.确定根节点在inorder的index

        left_node = self.buildTree(preorder[1:index+1], inorder[:index])
        right_node = self.buildTree(preorder[index+1:],inorder[index+1:])
        # inorder中index之后的为右子树，index之前的为左子树，
        # 在inorder中：左-中，在preorder中：中-左，长度是一样的，所以在preorder中，index之前的值都是根节点+左子树
        # 所以在preorder中，0号位是根节点，1到index+1区间内都是左子树。这样能把区间锁定出来

        root.left = left_node # 定义左右节点
        root.right = right_node

        return root

'''
leetcode 106
106. 从中序与后序遍历序列构造二叉树
给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，请你构造并返回这颗 二叉树 。

示例 1:
输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
输出：[3,9,20,null,null,15,7]

示例 2:
输入：inorder = [-1], postorder = [-1]
输出：[-1]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder[-1]) # 1.获取根节点
        index = inorder.index(root.val) # 2.在inorder中获取根节点的index

        left_node = self.buildTree(inorder[:index],postorder[:index])
        right_node = self.buildTree(inorder[index+1:],postorder[index:-1])
        # 在找inorder和postorder的左右子区间时，要把握inorder中：中-后，与postorder中：后-中
        # 这两个区间长度是一样的。在inorder中从index到最后，是由中和右组成的
        #                     在postorder中从index到最后，是由右和中组成的

        root.left = left_node
        root.right = right_node
        return root