'''

涉及到的题目
leetcode 501

'''
'''
leetcode 501
501. 二叉搜索树中的众数
给你一个含重复值的二叉搜索树（BST）的根节点 root ，找出并返回 BST 中的所有 众数（即，出现频率最高的元素）。
如果树中有不止一个众数，可以按 任意顺序 返回。
假定 BST 满足如下定义：
结点左子树中所含节点的值 小于等于 当前节点的值
结点右子树中所含节点的值 大于等于 当前节点的值
左子树和右子树都是二叉搜索树
 
示例 1：
输入：root = [1,null,2,2]
输出：[2]

示例 2：
输入：root = [0]
输出：[0]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''利用哈希表，记录每一个数出现的次数，返回出现次数最多的数'''
    def findMode(self, root: TreeNode) -> List[int]:
        hashtable = dict()
        def traversal(root):
            nonlocal hashtable
            if not root: return
            traversal(root.left)
            hashtable[root.val] = hashtable.setdefault(root.val,0) + 1
            traversal(root.right)
        traversal(root)
        keys = list(hashtable.keys())
        values = list(hashtable.values())
        max_value = max(values)
        ans = []
        for i in range(len(values)):
            if values[i] == max_value:
                ans.append(keys[i])
        return ans

# 不利用额外的空间，建立一个指针root和一个前指针pre
# 因为二叉搜索数中序遍历时递增序列，所以只需要比较相邻两个元素之间出现个数的次数即可
# 所以root指针用来一直遍历整棵树，pre指针就跟在root后面来记录每个元素出现的次数
#   当pre和root的值一样的时候，count + 1，同时跟当前最大count对比
#   当pre和root的值不一样的时候，count变成1，说明现在开始遍历新的元素了，重新计数
#       如果count跟maxcount一样，说明有不止一个元素时众数，将当前元素加入到res中
#       如果count比maxcount大，要更新maxcount，同时表示，原先res中所有的数都不是众数，将res清空，同时把当前元素加入到res中

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pre = None
        self.count = 0
        self.res = []
        self.max_count = 0

    def findMode(self, root: TreeNode) -> List[int]:
        def traversal(root):
            if not root: return None
            traversal(root.left)  # 左

            if self.pre is None:
                self.count = 1  # 循环正式开始，将count初始化为1
            elif self.pre.val == root.val:  # 前后两个指针一样的
                self.count += 1
            else:  # 当pre和root的值不一样的时候，count开始重新计数
                self.count = 1

            if self.count > self.max_count:  # 记录的数据大于当前最大count时
                self.max_count = self.count  # 更新当前最大count
                self.res = []  # 同时res中的所有元素都不是众数，清空res
                self.res.append(root.val)  # 重新将当前最频繁的元素加入到res中
            elif self.count == self.max_count:  # 假如此时count与最大count一样的，说明两者都是众数，全部加入到res中
                self.res.append(root.val)

            self.pre = root  # 中，更新pre指针，root指针的移动就时traversal函数控制的

            traversal(root.right)  # 右

        traversal(root)
        return self.res