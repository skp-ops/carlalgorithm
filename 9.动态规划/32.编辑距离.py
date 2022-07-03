'''

涉及到的题目
leetcode 72

'''
'''
leetcode 72
72. 编辑距离
给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。
你可以对一个单词进行如下三种操作：
插入一个字符
删除一个字符
替换一个字符

示例 1：
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

示例 2：
输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
            i n t e n t i o n
        [[0,1,2,3,4,5,6,7,8,9],
    e    [1,1,2,3,3,4,5,6,7,8],
    x    [2,2,2,3,4,4,5,6,7,8],
    e    [3,3,3,3,3,4,5,6,7,8],
    c    [4,4,4,4,4,4,5,6,7,8],
    u    [5,5,5,5,5,5,5,6,7,8],
    t    [6,6,6,5,6,6,5,6,7,8],
    i    [7,6,7,6,6,7,6,5,6,7],
    o    [8,7,7,7,7,7,7,6,5,6],
    n    [9,8,7,8,8,7,8,7,6,5]]
        dp[i][j]表示word1[0:j]和word2[0:i]的最小编辑距离（即题目中需要我们求什么，dp就代表着什么）
        我们可以进行的操作就是三个，增加；删除；替换
        假设word1=rara word2=ra，当j=4,i=2的时候，指针指的都是最末尾的'a'，那么此时要判断rara与ra的最小编辑距离
        我们可以这样去思考，因为最后一个字母a都是一样的，不需要编辑，所以我们只需要考察rar与r的最小编辑距离
        所以当word1[j-1]==word2[i-1]的时候dp[i][j] = dp[i-1][j-1]
        假设word1=rarb word2=ra，当j=4,i=2的时候指针值得末尾字母一个是b，一个是a，此时不一样，如何去求出最小编辑距离？
            方法1，可以先考虑rar与r的最小编辑距离为dp[i-1][j-1]，此时将word1中的b‘替换’为a，步骤加1，所以dp[i][j] = dp[i-1][j-1] + 1
            方法2，可以先考虑rar与ra的最小编辑距离为dp[i][j-1]，此时将rarb末尾的b‘删除’，步骤加1，所以dp[i][j] = dp[i][j-1] + 1
            方法3，可以先考虑rarb与r的最小编辑距离为dp[i-1][j]，此时将ra末尾的a‘删除’，步骤加1，所以dp[i][j] = dp[i-1][j] + 1
        从以上三个方法中寻找最小的情况即可

        至于初始化，以上面二维dp数组为例，第一排是拿intention和空字符串作比较，能做的操作只有不断删除intention，所以dp从左往右递增
            第一列是拿execution和空字符串作比较，能做的操作只有不断删除execution，所以dp从上到下递增
        '''
        n1, n2 = len(word1), len(word2)
        dp = [[0 for _ in range(n1 + 1)] for _ in range(n2 + 1)]
        for a in range(n1 + 1): dp[0][a] = a
        for b in range(n2 + 1): dp[b][0] = b
        for i in range(1, n2 + 1):
            for j in range(1, n1 + 1):
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        return dp[-1][-1]
