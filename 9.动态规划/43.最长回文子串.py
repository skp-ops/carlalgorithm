'''

涉及到的题目
leetcode 5

'''
'''
leetcode 5
5. 最长回文子串
给你一个字符串 s，找到 s 中最长的回文子串。

示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

示例 2：
输入：s = "cbbd"
输出："bb"
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
           b      a     b      a      b
        [[True, False, True, False, False],
         [False, True, False, True, False],
         [False, False, True, False, False],
         [False, False, False, True, False],
         [False, False, False, False, True]]
            a     a    c     a    b     d     k    a    c     a    a
        [[true,true,false,false,false,false,false,false,false,false,false],
         [false,true,false,true,false,false,false,false,false,false,false],
         [false,false,true,false,false,false,false,false,false,false,false],
         [false,false,false,true,false,false,false,false,false,false,false],
         [false,false,false,false,true,false,false,false,false,false,false],
         [false,false,false,false,false,true,false,false,false,false,false],
         [false,false,false,false,false,false,true,false,false,false,false],
         [false,false,false,false,false,false,false,true,false,true,false],
         [false,false,false,false,false,false,false,false,true,false,false],
         [false,false,false,false,false,false,false,false,false,true,true],
         [false,false,false,false,false,false,false,false,false,false,true]]

        '''
        maxlen, left, right = 0, 0, 0
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for a in range(n): dp[a][a] = True
        for i in range(n-1, -1, -1):
            for j in range(i+1,n):
                if s[i] == s[j]:
                    if j-i <= 1 or dp[i+1][j-1]: # dp核心，当首位一样的时候，只用考察去头去尾的部分是否为回文串即可
                        dp[i][j] = True
                        if j-i+1 > maxlen:
                            maxlen = j-i
                            left = i
                            right = j
        return s[left:right+1]
