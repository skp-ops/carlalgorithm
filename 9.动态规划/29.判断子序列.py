'''

涉及到的题目
leetcode 392

'''
'''
leetcode 392
392. 判断子序列
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。
（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
进阶：
如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？
 
示例 1：
输入：s = "abc", t = "ahbgdc"
输出：true

示例 2：
输入：s = "axc", t = "ahbgdc"
输出：false
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
            a h b g d c
          t t t t t t t
    a     f t t t t t t
    x     f f f f f f f
    c     f f f f f f f
        dp[i][j]表示当前字符串s[:i]在字符串t[:j]里是否为子序列
        如果是的话就看i-1和j-1是不是，如果是子序列，那么i,j也是子序列
        否则的话就要看左边和上边的dp的tf状态
        '''
        n1, n2 = len(s), len(t)
        dp = [[False for _ in range(n2+1)] for _ in range(n1+1)]
        for k in range(n2+1): dp[0][k] = True

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j] and dp[i][j-1]
        # print(dp)
        return dp[-1][-1]

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''double pointer'''
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(s)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''FIND function'''
        location = -1
        for char in s:
            location = t.find(char, location + 1)
            # 从location之后的位置开始查找，如果找到了就将位置重新赋值给location，如果没找到就返回False
            if location == -1: return False
        return True