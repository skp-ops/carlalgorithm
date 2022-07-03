'''

涉及到的题目
leetcode 583

'''
'''
leetcode 583
583. 两个字符串的删除操作
给定两个单词 word1 和 word2 ，返回使得 word1 和  word2 相同所需的最小步数。
每步 可以删除任意一个字符串中的一个字符。

示例 1：
输入: word1 = "sea", word2 = "eat"
输出: 2
解释: 第一步将 "sea" 变为 "ea" ，第二步将 "eat "变为 "ea"

示例  2:
输入：word1 = "leetcode", word2 = "etco"
输出：4
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        l e e t c o d e
      0 0 0 0 0 0 0 0 0
    e 0 0 1 1 1 1 1 1 1
    t 0 0 1 1 2 2 2 2 2
    c 0 0 1 1 2 3 3 3 3
    o 0 0 1 1 2 3 4 4 4
        求出最长公共子序列后，将两字符串长度分别减去公共子序列的长度，
        得到的总和就是需要删除的步数
        '''
        n1, n2 = len(word1), len(word2)
        dp = [[0 for _ in range(n1+1)] for _ in range(n2+1)]
        for i in range(1,n2+1):
            for j in range(1,n1+1):
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return n1+n2-2*dp[-1][-1]

'''
编辑距离的思想
1.确定dp数组（dp table）以及下标的含义
dp[i][j]：以i-1为结尾的字符串word1，和以j-1位结尾的字符串word2，想要达到相等，所需要删除元素的最少次数。
这里dp数组的定义有点点绕，大家要撸清思路。

2.确定递推公式
当word1[i - 1] 与 word2[j - 1]相同的时候
当word1[i - 1] 与 word2[j - 1]不相同的时候

当word1[i - 1] 与 word2[j - 1]相同的时候，dp[i][j] = dp[i - 1][j - 1];

当word1[i - 1] 与 word2[j - 1]不相同的时候，有三种情况：

    情况一：删word1[i - 1]，最少操作次数为dp[i - 1][j] + 1

    情况二：删word2[j - 1]，最少操作次数为dp[i][j - 1] + 1

    情况三：同时删word1[i - 1]和word2[j - 1]，操作的最少次数为dp[i - 1][j - 1] + 2

那最后当然是取最小值，所以当word1[i - 1] 与 word2[j - 1]不相同的时候，
递推公式：dp[i][j] = min({dp[i - 1][j - 1] + 2, dp[i - 1][j] + 1, dp[i][j - 1] + 1});

3.dp数组如何初始化
从递推公式中，可以看出来，dp[i][0] 和 dp[0][j]是一定要初始化的。
dp[i][0]：word2为空字符串，以i-1为结尾的字符串word1要删除多少个元素，才能和word2相同呢，很明显dp[i][0] = i。
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(len(word1)+1):
            dp[i][0] = i
        for j in range(len(word2)+1):
            dp[0][j] = j
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1] + 2, dp[i-1][j] + 1, dp[i][j-1] + 1)
        return dp[-1][-1]