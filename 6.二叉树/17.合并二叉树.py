'''

涉及到的题目
leetcode 617

'''
'''
leetcode 617
617. 合并二叉树
给你两棵二叉树： root1 和 root2 。
想象一下，当你将其中一棵覆盖到另一棵之上时，两棵树上的一些节点将会重叠（而另一些不会）。
你需要将这两棵树合并成一棵新二叉树。合并的规则是：如果两个节点重叠，那么将这两个节点的值相加作为合并后节点的新值；
否则，不为 null 的节点将直接作为新二叉树的节点。
返回合并后的二叉树。
注意: 合并过程必须从两个树的根节点开始。

示例 1：
输入：root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
输出：[3,4,5,5,4,null,7]

示例 2：
输入：root1 = [1], root2 = [1,2]
输出：[2,2]
'''
'''
在递归的时候，始终要返回一个节点类型的值
而且在这个题中，我们只在原本root1上做修改，这样可以省空间
所以在函数最后返回的时候返回root1
中节点数值处理完之后，就要对左右子节点进行递归
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:

        if not root1: return root2 # 遇到一个为空，就返回另外一个
        if not root2: return root1

        root1.val += root2.val # 中
        root1.left = self.mergeTrees(root1.left,root2.left) # 左
        root1.right = self.mergeTrees(root1.right,root2.right) # 右
        return root1
'''
递归其他写法
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2 :
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
            return t1
        return t1 or t2
'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        '''迭代法，一个队列储存两个节点的信息'''
        if not root1 :return root2
        if not root2: return root1
        queue = collections.deque()
        queue.append(root1)
        queue.append(root2)
        while queue:
            node1 = queue.popleft()
            node2 = queue.popleft()

            node1.val += node2.val # 处理中节点的值
            if node1.left and node2.left: # 统一append左节点
                queue.append(node1.left)
                queue.append(node2.left)
            if node1.right and node2.right: # 统一append右节点
                queue.append(node1.right)
                queue.append(node2.right)
            if not node1.left and node2.left: # root1无左节点，就直接用root2的左节点
                node1.left = node2.left
            if not node1.right and node2.right: # root2无右节点，就直接用root2的右节点
                node1.right = node2.right
        return root1