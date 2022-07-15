'''

涉及到的题目
leetcode 221、1277

'''
'''
leetcode 221
221. 最大正方形
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。

示例 1：
输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：4

示例 2：
输入：matrix = [["0","1"],["1","0"]]
输出：1

示例 3：
输入：matrix = [["0"]]
输出：0
'''
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        '''动态规划
        dp[i][j]表示：必须以matrix[i][j]为右下角所组成最大正方形的边长
        这样我们就知道了如果matrix中单个格子的值为0，对应到dp里也一定为0
            因为组成正方形必须要全部是1，有0存在说明无法形成正方形
        对于其递推公式可以这样考虑
        matrix                  dp                  location
        1 1 1                   1 1 1               1 2 3
        1 1 1                   1 2 2               4 5 6
        1 1 1                   1 2 3               7 8 9
        我们要在dp中得到2，一定要考察其位置的上边，左边，和斜上方是否为1，都为1，那么说明可以组成2*2的正方形
        我们要在dp中得到3，一个要考察这9个location是否都为1，那么我们如何知道这9个位置都为1呢？
        实际上也是查看其位置的上边，左边和斜上方。
            dp中3的上边为2,说明2356四个位置肯定都为1
            dp中3的左边为2,说明4578四个位置肯定都为1
            dp中3的斜上方为2,说明1245四个位置肯定都为1
            从而我们得知123456789都是1，那么此时可以构成3*3的正方形
        一旦上、左、斜中有一个位置为0，说明此时只能构成一个1*1的正方形（location 9），就是该位置本身
        一旦上、左、斜中有一个位置为1，说明此时只能构成一个2*2的正方形（location 5689）
        所以可以得到递推公式
            如果matrix[i][j] == 1:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1],[j-1]) + 1
        '''
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        # 初始化
        res = 0
        for a in range(len(matrix)):
            dp[a][0] = int(matrix[a][0])
            res = max(res, dp[a][0])
        for b in range(len(matrix[0])):
            dp[0][b] = int(matrix[0][b])
            res = max(res, dp[0][b])
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    res = max(res, dp[i][j])
        return res*res # 返回面积

'''
leetcode 1277
1277. 统计全为 1 的正方形子矩阵
给你一个 m * n 的矩阵，矩阵中的元素不是 0 就是 1，请你统计并返回其中完全由 1 组成的 正方形 子矩阵的个数。

示例 1：
输入：matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
输出：15
解释： 
边长为 1 的正方形有 10 个。
边长为 2 的正方形有 4 个。
边长为 3 的正方形有 1 个。
正方形的总数 = 10 + 4 + 1 = 15.

示例 2：
输入：matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
输出：7
解释：
边长为 1 的正方形有 6 个。 
边长为 2 的正方形有 1 个。
正方形的总数 = 6 + 1 = 7.
'''
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        # 初始化
        res = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    res += dp[i][j] # 将每一个dp中的数字累加起来
        return res