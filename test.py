'''

涉及到的题目
LeetCode 20

'''


def exist(board, word: str) -> bool:
    def helper(m, n, index, word):
        if index == len(word) - 1:
            return board[m][n] == word[index]
        if board[m][n] != word[index]:
            return False
        else:
            if n > 0:
                left = helper(m, n - 1, index + 1, word)
            else:
                left = False
            if n < len(board[0]) - 1:
                right = helper(m, n + 1, index + 1, word)
            else:
                right = False
            if m < len(board) - 1:
                down = helper(m + 1, n, index + 1, word)
            else:
                down = False
            return left or right or down

    ans = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                res = helper(i, j, 0, word)
                ans.append(res)
    return ans
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCB"))