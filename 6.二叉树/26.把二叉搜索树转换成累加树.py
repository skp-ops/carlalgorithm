'''

涉及到的题目
leetcode 538

'''
'''
leetcode 538
538. 把二叉搜索树转换为累加树
给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），
使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。

提醒一下，二叉搜索树满足下列约束条件：
节点的左子树仅包含键 小于 节点键的节点。
节点的右子树仅包含键 大于 节点键的节点。
左右子树也必须是二叉搜索树。
注意：本题和 1038: https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/ 相同

示例 1：
输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

示例 2：
输入：root = [0,null,1]
输出：[1,null,1]

示例 3：
输入：root = [1,0,2]
输出：[3,3,2]

示例 4：
输入：root = [3,2,4,1]
输出：[7,9,4,10]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''构造树的方法，先将二叉树的元素全部保存在一个列表中
    再从列表中累加，获得每个节点的元素值'''
class Solution:
    def get_list(self, root, container):
        if not root: return container
        self.get_list(root.left, container)
        container.append(root.val)
        self.get_list(root.right, container)
        return container

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = self.get_list(root, [])
        def dfs(root):
            if not root: return

            index = res.index(root.val)
            root.val = sum(res[index:])

            root.left = dfs(root.left)
            root.right = dfs(root.right)

            return root
        return dfs(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''由于是二叉搜索树，中序遍历是递增序列，那么右-中-左就是一个递减序列
每次在处理中间节点的时候加上前面所有节点的值即可'''
class Solution:
    def __init__(self):
        self.temp = 0
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traversal(root):
            if not root: return None
            traversal(root.right)
            root.val += self.temp
            self.temp = root.val # 更新累加temp的值
            traversal(root.left)
            return root
        return traversal(root)