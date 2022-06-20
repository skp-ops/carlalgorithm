'''

涉及到的题目
leetcode 257

'''
'''
leetcode 257

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        temp = []
        def backtracking(node):
            if node is None:  # 退出循环的条件，遇到空节点说明此路不同，要退出
                return

            temp.append(str(node.val)) # 每次遇到一个节点都将其值推入到temp里
            if not node.left and not node.right: # 假设这个节点的左右两个子节点都是空，说明该路径走到头
                res.append('->'.join(temp[:])) # 将目前得到的答案添加到res中

            backtracking(node.left) # 对左边进行递归
            backtracking(node.right) # 对右边进行递归
            temp.pop() # 回溯
        backtracking(root)
        return res