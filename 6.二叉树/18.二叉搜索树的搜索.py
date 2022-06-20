'''

涉及到的题目
leetcode 700

'''
'''
leetcode 700
700. 二叉搜索树中的搜索
给定二叉搜索树（BST）的根节点 root 和一个整数值 val。
你需要在 BST 中找到节点值等于 val 的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 null 。

示例 1:
输入：root = [4,2,7,1,3], val = 2
输出：[2,1,3]

示例 2:
输入：root = [4,2,7,1,3], val = 5
输出：[]
'''
'''
这道题要考虑二叉搜索树的性质
二叉搜索树性质是：
    若它的左子树不空，那么左子树上所有的节点值都小于其根节点的值
    若它的右子树不空，那么右子树上所有节点的值都大于其根节点的值
        同时其左右子树也是二叉搜索树

我们就要利用这个性质来剪枝，降低时间复杂度
假如当前遍历的节点node.val > val，说明我们要找的值在左子树上，那么只用搜索左子树即可
同理假如node.val < val，说明我们要找的值在右子树上，那么只用搜索右子树即可
假设刚好相等，那说明我们搜索到来，就直接返回这个节点
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        '''迭代法'''
        queue = collections.deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.val == val: # 找到了存在这个元素，直接返回该节点
                    return node
                if node.left and node.val > val : queue.append(node.left)
                if node.right and node.val < val : queue.append(node.right)
        return None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        '''迭代法精简写法'''
        while root:
            if root.val > val: root = root.left
            elif root.val < val: root = root.right
            else: return root
        return None
    


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        '''递归法'''
        if not root: return None
        if root.val > val:
            return self.searchBST(root.left,val)
        elif root.val < val:
            return self.searchBST(root.right,val)
        else:
            return root
        # 由于我们不需要遍历完所有的树，找到符合要求的就return，所以不需要return值