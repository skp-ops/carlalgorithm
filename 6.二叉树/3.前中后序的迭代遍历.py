'''

涉及到的题目
leetcode 144、145、94

'''
'''
迭代算法即是通过自己手动写入栈出栈来完成遍历的操作
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
'''
对于前序遍历，主要思想和步骤是现将中节点入栈，出栈之后将val append到res中，这样首先遍历中节点
紧接着判断右子树是否存在，存在则将右节点入栈；再判断左子树是否存在，存在则将左子树入栈
这样在之后出栈的时候，左边先出，然后右边最后出
这样就满足了 中-左-右 这个遍历顺序
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''迭代算法'''
        if root is None: return []

        stack = [root] # 将父节点推入，准备进行循环
        res = []
        while stack: # 当栈里还有元素的时候，说明树还没有遍历完，一直循环
            # 将中间节点弹出，然后把值添加到res中，首先实现对于中节点的遍历
            root = stack.pop()
            res.append(root.val)

            if root.right: # 如果右子树存在，则入栈
                stack.append(root.right)
            if root.left: # 如果左子树存在，则最后入栈
                stack.append(root.left)
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

'''
为了解释清楚，我说明一下 刚刚在迭代的过程中，其实我们有两个操作：
    处理：将元素放进result数组中
    访问：遍历节点
分析一下为什么刚刚写的前序遍历的代码，不能和中序遍历通用呢，
因为前序遍历的顺序是中左右，'先访问的元素是中间节点，要处理的元素也是中间节点'，
所以刚刚才能写出相对简洁的代码，因为要访问的元素和要处理的元素顺序'是一致的'，都是中间节点。

那么再看看中序遍历，中序遍历是左中右，先访问的是二叉树顶部的节点，
然后一层一层向下访问，直到到达树左面的最底部，再开始处理节点
（也就是在把节点的数值放进result数组中），这就造成了处理顺序和访问顺序是'不一致'的。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''迭代算法'''
        if root == None: return []
        res = []
        stack = [] # 此时不能将root入栈，因为中序遍历是 左中右
        pointer = root # 利用一个指针来确定遍历的位置

        while pointer or stack: # 当指针指在空，且栈里没有元素了，说明遍历结束，否则一直循环
            if pointer: # 指针一直在左边，向下遍历，将左子树appen到stack中
                stack.append(pointer)
                pointer = pointer.left
            else: # 遍历到空的时候，更新指针坐标为栈顶，记录当前获得的元素
                pointer = stack.pop()
                res.append(pointer.val)
                pointer = pointer.right # 左，中遍历完了，之后要遍历右子树
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
'''
前序遍历是 中-左-右，在上述的代码中是先推入中节点，再推入右节点，最后推入左节点
后序遍历是 左-右-中，反转过来就是 中-右-左，所以只需要将前序遍历里，左右节点推入的顺序变一下
                  然后将得到的答案倒序输出，就是后序遍历的结果里
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''迭代算法'''
        if root == None: return []
        res = []
        stack = [root] # 首先将父节点推入栈中
        while stack:
            root = stack.pop()
            res.append(root.val) # 首先遍历中节点的数
            if root.left: # 如果左节点存在，则优先与右节点入栈
                stack.append(root.left)
            if root.right: # 如果右节点存在，最后入栈
                stack.append(root.right)
        # 最后出栈的时候，遍历顺序是 中-右-左
        # res 反转，顺序为 左-右-中
        return res[::-1]