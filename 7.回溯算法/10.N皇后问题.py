'''

涉及到的题目
LeetCode 51

'''
'''
leetcode 51
按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
n皇后问题 研究的是如何将 n个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给你一个整数 n ，返回所有不同的n皇后问题 的解决方案。
每一种解法包含一个不同的n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例 1：
输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。

示例 2：
输入：n = 1
输出：[["Q"]]

https://leetcode.cn/problems/n-queens

'''
# 这道题我们需要自己创建一个棋盘，将这个棋盘看做一棵树上的各个叶子，所以在回溯函数循环中，不仅需要把n带上，board这个参数也要带上
# 同时每次for循环找的是column值，找完第一排的column值跳到第二排，所以还需要再添加一个row参数，来控制row的遍历

# 对于验证函数而言，只需要验证同一列，左上角，和右上角就行了。具体思路就是在验证列时，直接一个for循环过去，如果在该列存在Q则返回False
#   对于左上角和右上角而言，我们需要将row 和 col复制到新的临时参数里面，为了防止他们在循环的时候数值发生改变

#   为什么不对同一行继续验证，因为在验证函数之外，我们用for循环每次选择一个column进行'.'的替换，如果不符合要求，我们要回溯，回溯完
#   会发现这一行又没有Q了,所以同一行只可能存在一个Q.

# 在二维矩阵中，矩阵的高就代表着这棵树的高度，矩阵的宽代表的树形结构的宽度
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0: return []
        res, board = [], [['.'] * n for _ in range(n)] # 初始化result和棋盘

        def validation(board, row, col):
            # 检测同一列
            for row_index in range(n):
                if board[row_index][col] == 'Q':
                    return False
            # 检测右上角
            temp_row, temp_col = row - 1, col + 1
            while temp_row >= 0 and temp_col < n:
                if board[temp_row][temp_col] == 'Q':
                    return False
                temp_row -= 1
                temp_col += 1
            # 检测左上角
            temp_row, temp_col = row - 1, col - 1
            while temp_row >= 0 and temp_col >= 0:
                if board[temp_row][temp_col] == 'Q':
                    return False
                temp_col -= 1
                temp_row -= 1
            return True

        def backtracking(board, row, n):
            if row == n: # 结束循环的条件,row == n 说明已经循环到了最底层,Q全部添加完了
                temp_res = [] # 我们需要把board中的子数列转变成字符串添加到临时答案中
                for i in board:
                    temp_str = ''.join(i) # 将board里每一行变成一个字符串
                    temp_res.append(temp_str) # 将所有字符串添加进临时答案中
                res.append(temp_res) # 将临时答案添加进最终答案中
                return

            for col in range(n): # 我们循环遍历column的位置
                if not validation(board, row, col): # 如果该位置不满足条件就continue继续循环
                    continue
                board[row][col] = 'Q' # 假设满足validation的条件，就将该位置变成Q
                backtracking(board, row + 1, n) # row+1 进入下一行开始重新寻找这一行Q的位置
                board[row][col] = '.' # 回溯，将Q的位置调整回原来的'.'

        backtracking(board, 0, n)
        return res