'''

涉及到的题目
leetcode 79

'''
'''
leetcode 79
79. 单词搜索
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，
其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例 1：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true

示例 2：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
输出：true

示例 3：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
输出：false
 
'''
'''
定义一个递归函数来判断当前棋盘对应的字母是否和word中对应位置的字母相同
    如果不相同，返回False
    如果相同，则上下左右位置开始搜索下一个字母，由于不能到达已经遍历过的位置
        所以我们需要再定义一个哈希表来存放已经遍历过的位置
    所以在递归函数开头，先将当前位置存在哈希表中，在上下左右搜索判断区判断上下左右的位置是否在哈希表中，如果不在就继续深搜
    当然不满足题目要求的位置将返回False,返回之前还要把该位置移除哈希表，以便之后可能会搜到该位置（回溯）
    最终只要有一个满足条件，我们就返回True
'''

class Solution:
    def __init__(self):
        self.hash = set()

    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(m, n, index, word):
            if board[m][n] != word[index]:
                return False # 只要当前棋盘的位置和字符串对应index的位置不一样，就返回False
            if index == len(word) - 1:
                return True # 如果遍历到最后，说明全部满足条件，返回True
            else: # 如果没有遍历到最后，则继续向四周搜索
                self.hash.add((m, n)) # 先把当前元素加入到哈希表中，防止重复
                left, right, down, top = False, False, False, False # 初始化四个方位

                if n > 0 and (m, n - 1) not in self.hash: # 如果左边有元素，且位置没有被搜过
                    left = helper(m, n - 1, index + 1, word) # 就开始搜左边
                if n < len(board[0]) - 1 and (m, n + 1) not in self.hash: # 如果右边有元素，且位置没有被搜过
                    right = helper(m, n + 1, index + 1, word) # 就开始搜右边
                if m < len(board) - 1 and (m + 1, n) not in self.hash: # 如果下面有元素，且位置没有被搜过
                    down = helper(m + 1, n, index + 1, word) # 就开始搜下面
                if m > 0 and (m - 1, n) not in self.hash: # 如果上面有元素，且位置没有被搜过
                    top = helper(m - 1, n, index + 1, word) # 就开始搜上面

            self.hash.remove((m, n)) # 四个路径的答案都搜索完之后可以得出当前位置是否满足条件，再回溯，搜索其他位置
            return left or right or down or top # 返回当前位置是否合法

        for i in range(len(board)):
            for j in range(len(board[0])):
                if helper(i, j, 0, word):
                    return True
        return False

