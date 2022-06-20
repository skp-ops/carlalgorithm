'''

涉及到的题目
LeetCode 59

'''

'''
leetcode 59
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
示例 1：
1->2->3
      |
8->9  4
|     |
7<-6<-5
输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]

示例 2：
输入：n = 1
输出：[[1]]

https://leetcode-cn.com/problems/spiral-matrix-ii/

'''
# 一定要遵循变量不变原则，区间始终是左闭右开，这样就不会出错。
# 首先找规律，n=1的时候有中心点，转0圈
#           n=2的时候无中心点，转1圈
#           n=3的时候有中心点，转1圈
#           n=4的时候无中心点，转2圈
#           n=5的时候有中心点，转2圈
#     所以可以发现，n为奇数的时候要考虑中心点，n为偶数则不用考虑中心点。
#     同时转的圈数等于 n // 2 记为loop
# 记起始位置为startx，starty x代表着row，y代表着column，每经过一个循环，两者都增加1，从而进入下一个新的循环
# 再建立一个offset变量，每次循环一次，offset增加1，这样是为了防止第二个循环的过程中，把外圈的元素给修改了。 初始offset=1，之后每次循环加1
# 以n=5为例，第一次循环中:
#                     第一步填充[0][0] [0][1] [0][2] [0][3] (左闭右开原则)，循环区间[starty,n-offset)，即[0,4)，坐标为[startx][i]
#                     第二步填充[0][4] [1][4] [2][4] [3][4] (左闭右开原则)，循环区间[startx,n-offset)，即[0,4)，坐标为[i][n-offset]
#                     第三步填充[4][4] [4][3] [4][2] [4][1] (左闭右开原则)，循环区间[n-offset,starty,-1)，即[4,0)，坐标为[n-offset][i]
#                     第四步填充[4][0] [3][0] [2][0] [1][0] (左闭右开原则)，循环区间[n-offset,startx,-1)，即[4,0)，坐标为[i][starty]
# 第一次循环完了之后，startx starty 都变为1， 起点就是[1][1], offset=2， n-offset = 3。开始第二轮循环
# ………………
# 循环结束，此时当n为偶数的时候，count被加到n+1，但是没有填充到矩阵中，直接输出原矩阵即可
#             当n为奇数的时候，count被加到n+1，需要将count赋值给中心点，matrix[mid][mid]，然后再输出矩阵

class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0]*n for i in range(n)]
        startx, starty = 0, 0
        mid, loop = n//2, n//2
        count = 1

        for offset in range(1, loop + 1):
            for i in range(starty, n - offset):
                matrix[startx][i] = count
                count += 1
            for i in range(startx, n - offset):
                matrix[i][n - offset] = count
                count += 1
            for i in range(n - offset, starty,-1):
                matrix[n-offset][i] = count
                count += 1
            for i in range(n - offset, startx,-1):
                matrix[i][starty] = count
                count += 1
            startx += 1
            starty += 1

        if n % 2 != 0:
            matrix[mid][mid] = count
        return matrix

'''
leetcode 54
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

示例 2：
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]

https://leetcode-cn.com/problems/spiral-matrix

'''

# 对于m n矩阵，分别讨论m是否等于1，n是否等于1，mn是否相等，以及他们相等时mn是奇数还是偶数
# 然后根据左闭右开区间不变原则写循环。

class Solution:
    def spiralOrder(self, matrix: list[List[int]]) -> list[int]:
        nums = []
        m = len(matrix)
        n = len(matrix[0])
        lens = m * n
        offset = 1
        startx, starty = 0, 0

        if m == 1:
            return matrix[0]

        if n == 1:
            return [matrix[i][0] for i in range(m)]

        if m != 1 and n != 1:
            if m == n and m % 2 == 0:
                while len(nums) < lens:
                    for i in range(starty, n - offset):
                        nums.append(matrix[startx][i])
                    for i in range(startx, m - offset):
                        nums.append(matrix[i][n - offset])
                    for i in range(n - offset, starty, -1):
                        nums.append(matrix[m - offset][i])
                    for i in range(m - offset, startx, -1):
                        nums.append(matrix[i][starty])

                    offset += 1
                    startx += 1
                    starty += 1
                return nums

            if m == n and m % 2 != 0:
                while len(nums) + 1 < lens:
                    for i in range(starty, n - offset):
                        nums.append(matrix[startx][i])
                    for i in range(startx, m - offset):
                        nums.append(matrix[i][n - offset])
                    for i in range(n - offset, starty, -1):
                        nums.append(matrix[m - offset][i])
                    for i in range(m - offset, startx, -1):
                        nums.append(matrix[i][starty])

                    offset += 1
                    startx += 1
                    starty += 1
                mid = n // 2
                nums.append(matrix[mid][mid])
                return nums

            if m != n:
                while len(nums) < lens:
                    for i in range(starty, n - offset):
                        nums.append(matrix[startx][i])
                        if lens == len(nums):
                            return nums
                    for i in range(startx, m - offset):
                        nums.append(matrix[i][n - offset])
                        if lens == len(nums):
                            return nums
                    for i in range(n - offset, starty, -1):
                        nums.append(matrix[m - offset][i])
                        if lens == len(nums):
                            return nums
                    for i in range(m - offset, startx, -1):
                        nums.append(matrix[i][starty])
                        if lens == len(nums):
                            return nums

                    offset += 1
                    startx += 1
                    starty += 1
                return nums

