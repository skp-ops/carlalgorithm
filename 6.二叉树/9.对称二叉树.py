'''

涉及到的题目
leetcode 101、100、572

'''
'''
leetcode 101
101. 对称二叉树
给你一个二叉树的根节点 root ， 检查它是否轴对称。

示例 1：
输入：root = [1,2,2,3,4,4,3]
输出：true

示例 2：
输入：root = [1,2,2,null,3,null,3]
输出：false
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    '''
    迭代法
    主要思路就是一层一层遍历，将每一层的值都保存在一个res中，最后判断每一层的值是否是对称的
    如果遇到Null的值就将'#'填入，这样可以检测出['#',a,'#',a]这样不符合要求的非对称二叉树
    '''
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        res = []
        queue = deque([root])
        while queue:
            size = len(queue)
            temp = []
            for _ in range(size):
                node = queue.popleft() # 父节点的值不需要append，因为单个父节点就是对称的
                if node.left:
                    queue.append(node.left)
                    temp.append(node.left.val) # 假如有左子节点，就将值加入到temp中
                else:
                    temp.append('#') # 为空节点就加入井字号做标记
                if node.right:
                    queue.append(node.right)
                    temp.append(node.right.val) # 与左节点一样，右节点同理
                else:
                    temp.append('#') # 记录空节点，加入井字号做标记
            res.append(temp)
        for i in res:
            if i != i[::-1]: # 判断每一层是否为对称的
                return False
        return True


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''递归的难点在于：找到可以递归的点 为什么很多人觉得递归一看就会，一写就废。 或者说是自己写无法写出来，关键就是你对递归理解的深不深。
对于此题： 递归的点怎么找？从拿到题的第一时间开始，思路如下：
1.怎么判断一棵树是不是对称二叉树？ 答案：如果所给根节点，为空，那么是对称。如果不为空的话，当他的左子树与右子树对称时，他对称
2.那么怎么知道左子树与右子树对不对称呢？在这我直接叫为左树和右树 
答案：如果左树的左孩子与右树的右孩子对称，左树的右孩子与右树的左孩子对称，那么这个左树和右树就对称。
仔细读这句话，是不是有点绕？怎么感觉有一个功能A我想实现，但我去实现A的时候又要用到A实现后的功能呢？
当你思考到这里的时候，递归点已经出现了： 递归点：我在尝试判断左树与右树对称的条件时，发现其跟两树的孩子的对称情况有关系。
想到这里，你不必有太多疑问，上手去按思路写代码，函数A（左树，右树）功能是返回是否对称
def 函数A（左树，右树）： 
左树节点值等于右树节点值 且 函数A（左树的左子树，右树的右子树），函数A（左树的右子树，右树的左子树）均为真 才返回真
实现完毕。。。'''
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def s(left, right):
            if not left and not right: return True
            elif not left or not right: return False
            elif left.val != right.val: return False
            #
            # 上面三行代码全部都是退出循环的条件
            # 当左右节点全空，说明是对称的，有一个空就不对称
            # 当左右节点值不一样，则说明不对称
            # 然后下面再讨论假如左右节点一样，其左右节点的左右节点是否对称，这样就进行了递归

            return s(left.left,right.right) and s(left.right,right.left)

            # 其中我们要判断外层是否对称，同时也要判断内层是否对称
            # s(left.left,right.right)就是判断外层是否对称
            # s(left.right,right.left)就是判断内层是否对称
            # 假如内外都对称，则整个树对称

        return s(root,root)

'''
leetcode 100
100. 相同的树
给你两棵二叉树的根节点 figure storage 和 q ，编写一个函数来检验这两棵树是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1：
输入：figure storage = [1,2,3], q = [1,2,3]
输出：true

示例 2：
输入：figure storage = [1,2], q = [1,null,2]
输出：false

示例 3：
输入：figure storage = [1,2,1], q = [1,1,2]
输出：false
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q: return True # 遍历到尽头，返回True
        elif not p and q or not q and p: return False # 如果p，q有一个存在一个不存在，说明不同
        return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
    # 返回值就是判断其值是否一样，同时左节点，右节点是否都相同

'''
leetcode 572
572. 另一棵树的子树
给你两棵二叉树 root 和 subRoot 。检验 root 中是否包含和 subRoot 具有相同结构和节点值的子树。
如果存在，返回 true ；否则，返回 false 。
二叉树 tree 的一棵子树包括 tree 的某个节点和这个节点的所有后代节点。
tree 也可以看做它自身的一棵子树。

示例 1：
输入：root = [3,4,5,1,2], subRoot = [4,1,2]
输出：true

示例 2：
输入：root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
输出：false
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root and not subRoot: return True
        elif not root and subRoot or not subRoot and root: return False
        return self.isSametree(root,subRoot) \
               or self.isSubtree(root.left,subRoot) \
               or self.isSubtree(root.right,subRoot)
        # 判断当前是否为相同的树，如果不相同，那么判断root的左右子树是否相同，只要有一个相同即输出True。

    def isSametree(self,root,subRoot): # 判断是否为相同的树，与100题一样
        if not root and not subRoot: return True
        elif not root and subRoot or not subRoot and root: return False
        return root.val == subRoot.val \
               and self.isSametree(root.left,subRoot.left) \
               and self.isSametree(root.right,subRoot.right)