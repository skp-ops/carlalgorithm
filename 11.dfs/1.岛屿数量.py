'''

涉及到的题目
leetcode 200

'''
'''
leetcode 200
200. 岛屿数量
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。

示例 1：
输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1

示例 2：
输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''经过一个"1"，就将1替换为0，防止dfs又搜回去了，导致死循环'''
        if not grid: return 0
        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]): return
            if grid[row][col] == '1':
                grid[row][col] = '0'
                dfs(row-1, col)
                dfs(row+1, col)
                dfs(row, col+1)
                dfs(row, col-1)

        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    res += 1
                    dfs(r,c)
        return res