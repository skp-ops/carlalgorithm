'''

涉及到的题目
leetcode 516

'''
'''
leetcode 516
516. 最长回文子序列
给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。
子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。

示例 1：
输入：s = "bbbab"
输出：4
解释：一个可能的最长回文子序列为 "bbbb" 。

示例 2：
输入：s = "cbbd"
输出：2
解释：一个可能的最长回文子序列为 "bb" 。
'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        '''
        0 1 2 3 4
    0   1 2 3 3 4
    1   0 1 2 2 3
    2   0 0 1 1 3
    3   0 0 0 1 1
    4   0 0 0 0 1

    dp[i][j]表示当前字符串从i到j开始最长回文子序列的长度，遇到串问题就需要将其变成二维dp
    每一维表示其前后坐标位置
    分析当s[i] = s[j]的时候，会出现的情况是：
        i,j指同一个字符的时候，此时最长回文子序列长度就是1，dp[i][j] = 1
        i,j指的两个紧挨着的字符的时候，此时最长回文子序列长度就是2，dp[i][j] = 2
        i,j指的两个字符中间还夹杂着其他子串，那么就是夹着的字串最长回文子序列再加上一头一尾的两个
                dp[i][j] = dp[i+1][j-1] + 2
    分析当s[i] != s[j]的时候
        例如acbbbabg，当指针指向的字串为“cbbbab”时，显然c和b不一样，那么此时就考察i+1~j和i~j-1这个'子.子串'
        显然i+1~j是bbbab，dp为4； i~j-1是cbbba，dp为3，我们取最大值
            所以 dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        '''
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):
                if s[i] == s[j]:
                    if j == i:
                        dp[i][j] = 1
                    elif j - i == 1:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        return dp[0][-1]
