'''

涉及到的题目
leetcode 669

'''
'''
leetcode 669
669. 修剪二叉搜索树
给你二叉搜索树的根节点 root ，同时给定最小边界low 和最大边界 high。通过修剪二叉搜索树，使得所有节点的值在[low, high]中。
修剪树 不应该 改变保留在树中的元素的相对结构 (即，如果没有被移除，原有的父代子代关系都应当保留)。 可以证明，存在 唯一的答案 。
所以结果应当返回修剪好的二叉搜索树的新的根节点。注意，根节点可能会根据给定的边界发生改变。

示例 1：
输入：root = [1,0,2], low = 1, high = 2
输出：[1,null,2]

示例 2：
输入：root = [3,0,4,null,2,null,null,1], low = 1, high = 3
输出：[3,2,null,1]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        '''low和hgih的值可能都不会出现在树里面，所以要分情况只能分root.val < low, root.val > high 和root.val 在low与high的闭区间内
        只处理当前节点root的情况，如果root值小于最小值了，说明肯定要被剪掉，开始向root.right寻找符合题目的要求，
        但是又无法保证root.right一定是答案，所以要调用本身这个函数进行递归。同理如果当前节点root的值太大了，大到超过了范围
        就需要找root.left缩小范围，当然不清楚需要缩小几次，可能缩小完之后还是不符合要求，所以也要递归
        最终当前root的值在范围内了，就将其root.left 和 root.right用递归函数连接起来'''
        if not root: return None

        if root.val < low:
            right = self.trimBST(root.right, low, high)
            return right
        if root.val > high:
            left = self.trimBST(root.left, low, high)
            return left
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    迭代法
    '''
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root: return None

        while root and (root.val < low or root.val > high):
            if root.val < low:
                root = root.right
            else:
                root = root.left

        # 此时找到了在区间范围内的root点
        # 开始处理root的左右节点，因为其左右节点可能不在范围内
        cur = root # root作为头部不能动，借用current指针进行操作，剪枝左节点
        while cur:
            while cur.left and cur.left.val < low:
                cur.left = cur.left.right # 不断剔除不满足要求的子节点
            cur = cur.left # 不断向下寻找, 把所有可能符合要求的节点都搜一遍
        cur = root # 重新从头开始剪枝右节点
        while cur:
            while cur.right and cur.right.val > high:
                cur.right = cur.right.left
            cur = cur.right
        return root