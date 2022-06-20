'''

涉及到的题目
leetcode 102、107、199、637、429、515、116、117

'''
'''
leetcode 102
102. 二叉树的层序遍历
给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]

示例 2：
输入：root = [1]
输出：[[1]]

示例 3：
输入：root = []
输出：[]
'''
######################################
'''对于二叉树的层序遍历，必须要借助双向队列的辅助
假如我们用栈来处理，由于栈的特性，先进后出，会导致父节点总是第一个入栈，而出栈总是最后一个
这个跟我们预期不一样，因为我们预期是要将每一层的父节点都收集在同一个数组中，所以栈不满足我们的需求
队列的好处就是先进先出，这样我们只需要如下规则即可满足条件：
    1、只要队列里有元素，就不断循环，直到队列没有元素，说明遍历结束（while queue is True）
    2、每次获取第i层元素val值之前，要将该元素popleft，同时必须将其对应i+1层的左右子节点入队
    3、由于第i层有x个元素，所以步骤2要执行x次，即for循环要循环当前len（queue）次'''
######################################


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    '''二叉树层序遍历的迭代法'''
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = [] # 创建一个res用来存储每一层的答案
        if not root: return res # 特殊情况单独讨论
        queue = deque([root]) # 创建一个队列，并且将父节点入队，准备开始后序循环
        while queue:
            size = len(queue) # 求出每一层元素的个数，有多少个元素，就for循环多少次，将每个元素的左右子节点append到queue中
            temp = [] # 用来临时储存每一层结果
            for _ in range(size):
                node = queue.popleft() # 把每一层的每个元素都当成父节点，提取出来，然后将其左右子节点append
                temp.append(node.val) # 收集该层的每一个元素值
                if node.left: # 如果该父节点有左子叶就入队
                    queue.append(node.left)
                if node.right: # 如果该父节点有右子叶就入队
                    queue.append(node.right)
            res.append(temp) # 把该层元素推入res中
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    '''二叉树层序遍历的递归法'''
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = [] # 创建一个res用来存储每一层的答案
        if not root: return res # 特殊情况单独讨论
        def traversal(root,depth):
            if len(res) == depth: res.append([]) # 每次递归到新的一层，为res添加一个[]用来存储当前层的结果
            res[depth].append(root.val) # 将当前父节点的值添加到答案中
            if root.left: traversal(root.left,depth+1) # 左子节点开始递归
            if root.right: traversal(root.right,depth+1) # 右子节点开始递归
        traversal(root,0)
        return res

'''
leetcode 107
107. 二叉树的层序遍历 II
给你二叉树的根节点 root ，返回其节点值 自底向上的层序遍历 。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：[[15,7],[9,20],[3]]

示例 2：
输入：root = [1]
输出：[[1]]

示例 3：
输入：root = []
输出：[]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root is None: return res
        def traversal(root, depth):
            if len(res) == depth: res.append([])
            res[depth].append(root.val)
            if root.left: traversal(root.left, depth + 1)
            if root.right: traversal(root.right, depth + 1)
        traversal(root,0)
        return res[::-1]

'''
leetcode 199
199. 二叉树的右视图
给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例 1:
输入: [1,2,3,null,5,null,4]
输出: [1,3,4]

示例 2:
输入: [1,null,3]
输出: [1,3]

示例 3:
输入: []
输出: []
'''
'''
用一个字典来保存每一层中最后一个元素的值，然后输出字典的value即可
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    '''递归法'''
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = dict()
        if root is None: return []
        def traversal(root, depth):
            if root:
                res[depth] =root.val
                traversal(root.left, depth + 1)
                traversal(root.right, depth + 1)
        traversal(root, 0)
        res_arr = list(res.values())
        return res_arr


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    '''迭代法'''
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None: return []
        queue = deque([root])
        while queue:
            size = len(queue)
            temp = []
            for _ in range(size):
                node = queue.popleft()
                temp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(temp[-1])
        return res

'''
leetcode 637
637. 二叉树的层平均值
给定一个非空二叉树的根节点 root , 以数组的形式返回每一层节点的平均值。
与实际答案相差 10-5 以内的答案可以被接受。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：[3.00000,14.50000,11.00000]
解释：第 0 层的平均值为 3,第 1 层的平均值为 14.5,第 2 层的平均值为 11 。
因此返回 [3, 14.5, 11] 。

示例 2:
输入：root = [3,9,20,15,7]
输出：[3.00000,14.50000,11.00000]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        '''迭代法'''
        res = []
        queue = deque([root])
        while queue:
            size = len(queue)
            temp_total = 0
            for _ in range(size):
                node = queue.popleft()
                temp_total += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(temp_total / size)
        return res

'''
leetcode 429
429. N 叉树的层序遍历
给定一个 N 叉树，返回其节点值的层序遍历。（即从左到右，逐层遍历）。
树的序列化输入是用层序遍历，每组子节点都由 null 值分隔（参见示例）。
 
示例 1：
输入：root = [1,null,3,2,4,null,5,6]
输出：[[1],[3,2,4],[5,6]]

示例 2：
输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
输出：[[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    '''迭代法'''
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if root is None: return res
        queue = deque([root])
        while queue:
            size = len(queue)
            temp = []
            for _ in range(size): # N叉树是由数组组成的，所以在遍历其子节点的时候要用for循环
                node = queue.popleft()
                temp.append(node.val)
                for chl in node.children:# node.children为list类
                    queue.append(chl)
            res.append(temp)
        return res

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    '''递归法'''
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if root is None: return res
        def dfs(root, depth):
            if root is None: return
            if len(res) <= depth:
                res.append([])
            res[depth].append(root.val)
            for chl in root.children:
                dfs(chl, depth + 1)
        dfs(root, 0)
        return res

'''
leetcode 515
515. 在每个树行中找最大值
给定一棵二叉树的根节点 root ，请找出该二叉树中每一层的最大值。

示例1：
输入: root = [1,3,2,5,3,null,9]
输出: [1,3,9]

示例2：
输入: root = [1,2,3]
输出: [1,3]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        '''迭代法'''
        res = []
        if root is None: return res
        queue = deque([root])
        while queue:
            size = len(queue)
            temp = -float('inf')
            for _ in range(size):
                node = queue.popleft()
                temp = max(temp,node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(temp)
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        '''递归法'''
        res = []
        if root is None: return res
        def traversal(root, depth):
            if len(res) == depth: res.append(-float('inf'))
            res[depth] = max(res[depth],root.val)
            if root.left: traversal(root.left, depth + 1)
            if root.right: traversal(root.right, depth + 1)
        traversal(root, 0)
        return res

'''
leetcode 116
116. 填充每个节点的下一个右侧节点指针
给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
初始状态下，所有 next 指针都被设置为 NULL。

示例 1：
输入：root = [1,2,3,4,5,6,7]
输出：[1,#,2,3,#,4,5,6,7,#]
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。
序列化的输出按层序遍历排列，同一层节点由 next 指针连接，'#' 标志着每一层的结束。

图详见：https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/

示例 2:
输入：root = []
输出：[]
'''
'''
本题不需要将答案append到一个res中，只是在root原本的基础上做修改
同时，如果next指针指向None则不用操作，因为next指向的默认值就是None
所以我们只需要定义有意义的next指针
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None: return
        queue = deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == size -1: # 遍历到每一层的最后一个节点时，由于next指针指向空，则直接break
                    break
                node.next = queue[0] # queue的[0]始终都是同层该节点的右边节点
        return root

'''
leetcode 117
117. 填充每个节点的下一个右侧节点指针 II
给定一个二叉树

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
初始状态下，所有 next 指针都被设置为 NULL。

进阶：
你只能使用常量级额外空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。

示例：
输入：root = [1,2,3,4,5,null,7]
输出：[1,#,2,3,#,4,5,7,#]
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。
序列化输出按层序遍历顺序（由 next 指针连接），'#' 表示每层的末尾。
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None: return None
        queue = deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                if i == size - 1:
                    break
                node.next = queue[0]
        return root