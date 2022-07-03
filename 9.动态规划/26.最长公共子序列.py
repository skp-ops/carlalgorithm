'''

涉及到的题目
leetcode 1143

'''
'''
leetcode 1143
1143. 最长公共子序列
给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。
一个字符串的 子序列 是指这样一个新的字符串：
    它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。

示例 1：
输入：text1 = "abcde", text2 = "ace" 
输出：3  
解释：最长公共子序列是 "ace" ，它的长度为 3 。

示例 2：
输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc" ，它的长度为 3 。

示例 3：
输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0 。
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        dp[i][j]就是当两个字符串的位置分别为i和j时，当前情况下的最长公共子序列
        如何确定递推公式，同样跟718题一样，需要对两个字符串进行遍历
            就两种情况，text1[i] == text2[j] 和 text1[i] != text2[j]
            如果两个字符相同，就说明此时最长公共子序列长度又可以加1了，即dp[i][j] = dp[i-1][j-1]+1
            如果两个字符不相同，因为本题是子序列，不需要连续，所以就继承之前的最长公共子序列的长度
            所以之前最长的有两种情况，即dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            初始化是初始化第一排和第一列，直接寻找两个字符串的首个字母，看他们是否存在于对方的字符串中
            如果存在，就获取那个字母的index，index以及之后的元素都为1即可
            如果不存在，则index统一变成len长，即没有一个元素需要初始化为1，保持0即可
            a b c d e f
        a   1 1 1 1 1 1
        c   1 1 2 2 2 2
        z   1 1 2 2 2 2
        d   1 1 2 3 3 3
        e   1 1 2 3 4 4
        f   1 1 2 3 4 5
        '''
        n1, n2 = len(text1), len(text2)
        dp = [[0 for _ in range(n1)] for _ in range(n2)]
        if text1[0] in text2: c_i = text2.index(text1[0])
        else: c_i = n1
        if text2[0] in text1: r_i = text1.index(text2[0])
        else: r_i = n2
        for i in range(r_i, n1): dp[0][i] = 1
        for j in range(c_i, n2): dp[j][0] = 1
        for a in range(1, n1):
            for b in range(1, n2):
                if text1[a] == text2[b]:
                    dp[b][a] = dp[b-1][a-1] + 1
                else:
                    dp[b][a] = max(dp[b-1][a], dp[b][a-1])
        return dp[-1][-1]