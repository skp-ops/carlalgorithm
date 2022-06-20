'''

涉及到的题目
leetcode 144、145、94

'''
'''
在第三章的内容中，我们可以看到，只有前序和后序的遍历代码比较相似，但是对于中序来说
完全是另外一种思路，利用指针来进行节点的操作和访问
为了能够统一代码的风格和思维的方式，我们需要找到一个解决方案
    （标记法）具体方法就是 将要访问的节点放入栈，将要处理的节点也放入栈中，但是同时要做标记
        即：将要处理的节点放入栈之后，紧接着放入一个空指针作为标记
'''
'''
leetcode 144
144. 二叉树的前序遍历
给你二叉树的根节点 root ，返回它节点值的 前序 遍历。

示例 1：
输入：root = [1,null,2,3]
输出：[1,2,3]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]

示例 4：
输入：root = [1,2]
输出：[1,2]

示例 5：
输入：root = [1,null,2]
输出：[1,2]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''统一迭代算法'''
        if root is None: return []
        stack = [root] # 将父节点入栈准备进行循环
        res = []
        while stack: # 如果栈里一直有元素，则说明遍历没结束，一直循环
            node = stack.pop() # 一开始是中节点；之后就是操作结束，更新节点，开始遍历其左右节点
            if node:
                if node.right: # 右节点入栈
                    stack.append(node.right)

                if node.left: # 左节点入栈
                    stack.append(node.left)

                stack.append(node) # 中节点入栈
                stack.append(None) # 同时中节点是需要处理的节点，推入一个空指针作为判定标记

            else: # 检测到当前为空指针，则需要进行操作
                node = stack.pop() # 获取空指针前面的节点信息
                res.append(node.val) # 将元素推入res中
        return res

'''
leetcode 94
94. 二叉树的中序遍历
给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。

示例 1：
输入：root = [1,null,2,3]
输出：[1,3,2]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''统一迭代算法'''
        if root == None: return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node:
                if node.right:  # 右节点
                    stack.append(node.right)

                stack.append(node)  # 中节点
                stack.append(None)  # 中节点访问过，但是还没有处理，加入空节点做为标记。

                if node.left:  # 左节点
                    stack.append(node.left)

            else:  # 遇到空节点
                node = stack.pop()
                res.append(node.val)
        return res

'''
leetcode 145
145. 二叉树的后序遍历
给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 。

示例 1：
输入：root = [1,null,2,3]
输出：[3,2,1]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''统一迭代算法'''
        if root == None: return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node:
                stack.append(node) # 中节点
                stack.append(None)

                if node.right: # 右节点
                    stack.append(node.right)

                if node.left: # 左节点
                    stack.append(node.left)
            else: # 遇到空节点
                node = stack.pop()
                res.append(node.val)
        return res