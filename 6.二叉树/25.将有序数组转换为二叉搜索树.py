'''

涉及到的题目
leetcode 108

'''
'''
leetcode 108
108. 将有序数组转换为二叉搜索树
给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。
高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。

示例 1：
输入：nums = [-10,-3,0,5,9]
输出：[0,-3,9,-10,null,5]
解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：

示例 2：
输入：nums = [1,3]
输出：[3,1]
解释：[1,null,3] 和 [3,1] 都是高度平衡二叉搜索树。
'''
'''
可以和其他构造类题目类比，方法大同小异
    从中序和后序（前序和中序）遍历序列构造二叉树
    最大二叉树
    二叉搜索树插入
    删除二叉树节点
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        '''
        此题能够保证是高度平衡二叉树的原因在于，每个父节点取的都是当前数组的中间值
        中间值的左侧形成了左子树，中间值的右侧形成了右子树
        这样左右元素的个数差永远控制在1个以内，这样左右就不会出现高度差大于1的情况
        自然而然就成为了平衡的二叉搜索树
        '''
        if not nums: return None
        index = (len(nums)-1)//2
        root = TreeNode(nums[index])
        root.left = self.sortedArrayToBST(nums[:index])
        root.right = self.sortedArrayToBST(nums[index+1:])
        return root