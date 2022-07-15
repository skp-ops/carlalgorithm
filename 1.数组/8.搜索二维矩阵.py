'''

涉及到的题目
leetcode 240

'''
'''
leetcode 240
240. 搜索二维矩阵 II
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
 
示例 1：
输入：matrix = [[1,4,7,11,15],
               [2,5,8,12,19],
               [3,6,9,16,22],
               [10,13,14,17,24],
               [18,21,23,26,30]], 
     target = 5
输出：true

示例 2：
输入：matrix = [[1,4,7,11,15],
               [2,5,8,12,19],
               [3,6,9,16,22],
               [10,13,14,17,24],
               [18,21,23,26,30]], 
     target = 20
输出：false
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''Z字搜索
        从右上角开始搜，如果当前值大于目标数，说明要向左慢慢逼近
        如果当前值小于目标数，说明要向下慢慢逼近
        最终如果找到target返回True，否则返回False'''
        rows, cols = len(matrix), len(matrix[0])
        r, c = 0, cols-1
        while 0 <= r <= rows-1 and 0 <= c <= cols-1:
            if target == matrix[r][c]:
                return True
            elif target > matrix[r][c]:
                r += 1
            else:
                c -= 1
        return False