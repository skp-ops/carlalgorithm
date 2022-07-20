'''

涉及到的题目
leetcode 198、213、337

'''
'''
leetcode 198
198. 打家劫舍
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

示例 1：
输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。4
     
示例 2：
输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
 
'''

'''
一开始的思路是先分情况，如果只有一家或者两家，那么取价值最大的一家即可
如果超过两家，开始dp
dp[i]代表的是偷到第i家时，能偷的最大价值。由于不能偷紧挨着的一家，所以只有两个选择
    1.偷第i家，第i-1家不偷，那么此时的价值就是value[i]+dp[i-2]
    2.不偷第i家，价值仍然是偷第i-1家时的价值，此时价值就是dp[i-1]
两者取最大值就好，公式就是dp[i] = max(dp[i-1], nums[i]+dp[i-2])

class Solution:
    """错误解答"""
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2: return max(nums)
        n = len(nums)
        dp = [0]*(n)
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i]+dp[i-2])
        return dp[-1]
        
写出的代码有case通不过，[2,1,1,2]
打印出dp数组为 [2, 1, 3, 3]，说明最高只能偷到3，但是答案是4，第0个房子和第3个房子总和为4

'''

'''
之后开始解决问题，我发现在遍历第i个房子的时候，我只要搜索i-1之前的最大价值即可
但是这样时间复杂度会大大增加，所以继续思考有没有更好的方法
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2: return max(nums)
        n = len(nums)
        dp = [0]*(n)
        dp[0] = nums[0]
        dp[1] = nums[1] # dp[1] 存在bug
        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i]+max(dp[:i-1])) # 找出之前的最大价值
        return dp[-1]

'''
然后再次review代码，发现是dp[1]这个地方写错了，dp[1]所偷的价值并不是nums[1]，因为有可能0号房子的价值更大
所以dp[1] = max(nums[0],nums[1]),这样才是正确的dp[1]，出错的原因是因为没有正确理解dp的含义
dp初始化时，含义仍然是偷到该房子所能获得的最大价值，所以偷第0个房子没有选择，只能偷到nums[0]
但是从偷到第1个房子开始，就要和之前所偷的房子进行判断，判断怎么偷价值最大
debug后按照第一个解题思路顺利AC
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2: return max(nums)
        n = len(nums)
        dp = [0]*(n)
        dp[0] = nums[0]
        dp[1] = max(nums[1],nums[0])
        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i]+dp[i-2])
        return dp[-1]

'''
leetcode 213
213. 打家劫舍 II
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。
这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。
同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。

示例 1：
输入：nums = [2,3,2]
输出：3
解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。

示例 2：
输入：nums = [1,2,3,1]
输出：4
解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。
     
示例 3：
输入：nums = [1,2,3]
输出：3
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        这道题告诉你就是偷首就不能偷尾，偷尾就不能偷首
        那怎么才能知道最佳方案是偷首还是偷尾呢？
        偷首算一次dp，偷尾算一次dp，两个求最大值就好
        '''
        n = len(nums)
        if n <= 3: return max(nums)
        dp_1 = [0]*(n-1)
        dp_2 = [0]*(n)
        dp_1[0], dp_2[1] = nums[0], nums[1] # 初始化dp首项
        dp_1[1], dp_2[2] = max(nums[0],nums[1]), max(nums[1],nums[2]) # 初始化dp第二项
        for i in range(2,n):
            if i == 2: # 偷首，即算dp_1
                dp_1[i] = max(dp_1[i-1], nums[i]+dp_1[i-2])
            elif i == n-1: # 偷尾，即算dp_2
                dp_2[i] = max(dp_2[i-1], nums[i]+dp_2[i-2])
            else: # 其他时候正常计算
                 dp_1[i] = max(dp_1[i-1], nums[i]+dp_1[i-2])
                 dp_2[i] = max(dp_2[i-1], nums[i]+dp_2[i-2])
        return max(dp_1[-1], dp_2[-1])

'''
leetcode 337
337. 打家劫舍 III
小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为 root 。
除了 root 之外，每栋房子有且只有一个“父“房子与之相连。
一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
如果 两个直接相连的房子在同一天晚上被打劫 ，房屋将自动报警。
给定二叉树的 root 。返回 在不触动警报的情况下 ，小偷能够盗取的最高金额 。

示例 1:
输入: root = [3,2,3,null,3,null,1]
输出: 7
解释: 小偷一晚能够盗取的最高金额 3 + 3 + 1 = 7

示例 2:
输入: root = [3,4,5,1,3,null,1]
输出: 9
解释: 小偷一晚能够盗取的最高金额 4 + 5 = 9
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''本题的思路就是遍历树的每一个节点的时候返回值为一个元组，元组0表示偷当前节点可以获得的最大价值，
    元组1表示不偷当前节点可以获得的最大价值。那么树的遍历方式一定是后序遍历，因为树的最底层一定是0，因为从最底层开始偷，
    树的最上层一定是偷钱最多的地方，因为从下往上偷，价值不断累加。所以必须要用返回值来做下一步的计算，故要后序遍历
    假设遇到空节点，说明这一分支遍历到头，返回(0,0)，说明偷或者不偷，都只能得到0元
    再开始左-右-中遍历。因为之后遍历需要用到左右分枝返回的结果，所以我们用left和right来接收左右分枝获利最大值
    这个时候处理中节点的单循环逻辑，先计算偷取父节点所获的最大价值，
        value0 = root.val + left[1] + right[1]， left1和right1代表着左右不偷获得的最大价值，再加上父节点的价值
    再计算不偷父节点的最大价值，这个时候就没有root.val了，但是我们左右子节点就可以选择偷或者不偷，取决于哪个价值最大
    最后返回当前节点偷与不偷的价值元组'''
    def rob(self, root: TreeNode) -> int:
        res = self.c(root)
        return max(res)
    def c(self, root):
        if not root: return (0,0) # 0 偷root， 1不偷root
        left = self.c(root.left)
        right = self.c(root.right)
        value0 = root.val + left[1] + right[1] # 偷root节点，再加上不偷左右子节点的钱
        value1 = max(left[0], left[1]) + max(right[0], right[1])
        return (value0, value1)