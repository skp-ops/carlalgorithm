'''

涉及到的题目
leetcode 110

'''
'''
leetcode 110
110. 平衡二叉树
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：true

示例 2：
输入：root = [1,2,2,3,3,null,null,4,4]
输出：false

示例 3：
输入：root = []
输出：true
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    定义一个函数g，用来求左右子树的高度，如果两者高度差的绝对值大于1，说明不平衡
    这个时候函数返回-1。主函数只要判断返回得到的结果是否为-1，就能判断True还是False
    在g函数中，求当前树的高度，就是 1+max(left,right)
    同时要验证左右子树下的子节点是否为平衡，则需要在算出left和right之后，进行一个判断
    先判断左子树是否平衡，再判断右子树是否平衡，最后判断中间节点是否平衡。
    如果平衡就返回当前高度，继续迭代
    '''
    def g(self, root):
        if not root: return 0 # 遍历到此节点为空，说明已经到最底部，其高度为0
        left = self.g(root.left) # 左
        if left == -1: return -1 # 检查左子节点下的树是否平衡
        right = self.g(root.right) # 右
        if right == -1: return -1 # 检查右子节点下的树是否平衡
        height = max(left,right) + 1
        if abs(left-right) <= 1: # 中
            return height
        else:
            return -1
    def isBalanced(self, root: TreeNode) -> bool:
        if self.g(root) == -1:
            return False
        else:
            return True

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def g(self, root):
        '''
        求出子树的最大深度
        '''
        if not root: return 0
        left = self.g(root.left)
        right = self.g(root.right)
        depth = 1 + max(left , right)
        return depth
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        # 同时判断中节点，左节点，右节点是否都是平衡的
        return abs(self.g(root.left)-self.g(root.right)) <= 1 \
               and self.isBalanced(root.left) \
               and self.isBalanced(root.right)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        '''迭代法'''
        st = []
        if not root:
            return True
        st.append(root)
        while st:
            node = st.pop()  # 中
            if abs(self.getDepth(node.left) - self.getDepth(node.right)) > 1:
                return False
            if node.right:
                st.append(node.right)  # 右（空节点不入栈）
            if node.left:
                st.append(node.left)  # 左（空节点不入栈）
        return True

    def getDepth(self, root):  # 求最大深度
        if not root: return 0
        queue = deque([root])
        res = 0
        while queue:
            size = len(queue)
            res += 1
            for _ in range(size):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return res