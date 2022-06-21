'''

涉及到的题目
leetcode 62、63

'''
'''
leetcode 62
62. 不同路径
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？

示例 1：
输入：m = 3, n = 7
输出：28

示例 2：
输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下

示例 3：
输入：m = 7, n = 3
输出：28

示例 4：
输入：m = 3, n = 3
输出：6
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''数论方法，机器人肯定走m+n-2步，肯定有m-1步向下走，
        就是排列组合问题，计算C(m+n-2, m-1 or n-1)'''
        a = m+n-2
        b = min(m,n)-1
        top, down = 1, 1
        for i in range(b):
            top *= (a - i)
            down *= (i + 1)
        return int(top/down)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''深度优先搜索算法
        把机器人走的路程转换成一棵树，向右走就是右节点，向下走就是左节点
        走到头就是向右走的步数等于m，或者向下走的步数等于n，到达节点的时候计数器加1，表示一种方法
        这样遍历完所有子叶就可以知道答案
        但是时间复杂度是2^(m+n)级的，非常大,直接超时'''
        right = m-1
        down = n-1
        def dfs(right,down):
            if right < 0 or down < 0: return 0
            if right == 0 and down == 0: return 1
            return dfs(right-1,down) + dfs(right, down-1)
        return dfs(right,down)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''考虑动态规划的算法
        dp[i][j]表示从0,0开始到当前i,j位置有几种走法'''
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for a in range(1,n): dp[0][a] = 1
        for b in range(1,m): dp[b][0] = 1 # 初始化数组，只横着走与只竖着走都只有一种方法
        for j in range(1,n):
            for i in range(1,m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # 测试用例 m=3, n=7 与 m=3, n=2
        #   [[1,1,1, 1, 1, 1, 1],
        #    [1,2,3, 4, 5, 6, 7],
        #    [1,3,6,10,15,21,28]]
        #   [[1,1],
        #    [1,2],
        #    [1,3]]
        return dp[m-1][n-1]

'''
leetcode 63
63. 不同路径 II
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
网格中的障碍物和空位置分别用 1 和 0 来表示。

示例 1：
输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2
解释：3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右

示例 2：
输入：obstacleGrid = [[0,1],[0,0]]
输出：1
'''
# 这道题与62题不一样的点就在于棋盘中出现了石头，那么就说明从坐标原点出发，无论如何也到不了石头
# 故，石头坐标下的步数就为0 然后再按照状态方程一点点算出到达终点的坐标
# 有一些特殊情况就是，当石头挡在第一行或者第一列的时候，石头之后的坐标都变成0，因为永远也到不了那里（不能回退）
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1: return 0
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        dp = [[1 for _ in range(n)] for _ in range(m)] # 初始化步数都为1
        for a in range(m):
            for b in range(n):
                if obstacleGrid[a][b] == 1: # 遇见了石头，步数变为0
                    dp[a][b] = 0
        need_change = False
        for c in range(1,n): # 假设石头出现在第一行，石头以及石头后面的步数都为0
            if dp[0][c] == 0:
                need_change = True
            if need_change:
                dp[0][c] = 0
        need_change = False
        for d in range(1,m): # 假设石头出现在第一列，石头以及石头后面的步数都为0
            if dp[d][0]  == 0:
                need_change = True
            if need_change:
                dp[d][0] = 0

        for i in range(1,m):
            for j in range(1,n):
                if dp[i][j] == 0:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]