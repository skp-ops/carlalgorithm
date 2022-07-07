'''

涉及到的题目
leetcode 236、235

'''
'''
leetcode 236
236. 二叉树的最近公共祖先
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 figure storage、q，
最近公共祖先表示为一个节点 x，满足 x 是 figure storage、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

示例 1：
输入：root = [3,5,1,6,2,0,8,null,null,7,4], figure storage = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。

示例 2：
输入：root = [3,5,1,6,2,0,8,null,null,7,4], figure storage = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。

示例 3：
输入：root = [1,2], figure storage = 1, q = 2
输出：1
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 只考虑递归函数的作用，第一个作用就是寻找p和q，如果找到了就返回p或者q
        #   第二个作用，公共祖先就是p和q在其左右，也就是说如果一个节点的左右子树有返回值，说明该节点就是祖先，返回祖先
        #   再加上其他的判断，如果一边无返回值，一边有返回值，说明公共祖先在那边，返回那条边的root
        #   最后一点点返回到树的开头，最后得出返回值
        def dfs(root, p, q):
            if not root: return None
            if root == p or root == q: return root

            left = dfs(root.left,p,q)
            right = dfs(root.right,p,q)

            if left and right: return root
            elif not left and right: return right
            else: return left
        return dfs(root,p,q)

'''
leetcode 235
235. 二叉搜索树的最近公共祖先
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 figure storage、q，
最近公共祖先表示为一个结点 x，满足 x 是 figure storage、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]

示例 1:
输入: root = [6,2,8,0,4,7,9,null,null,3,5], figure storage = 2, q = 8
输出: 6 
解释: 节点 2 和节点 8 的最近公共祖先是 6。

示例 2:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], figure storage = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 二叉树的性质：当qp都小于节点，说明qp都在左子树，搜索左子树即可
        #               当qp都大于节点，说明qp都在右子树，搜索右子树即可
        #               当qp一左一右,说明此时的节点就是公共祖先
        def dfs(root,p,q):
            if q.val < root.val and p.val < root.val:
                return dfs(root.left,p,q)
            elif q.val > root.val and p.val > root.val:
                return dfs(root.right,p,q)
            else:
                return root
        return dfs(root,p,q)