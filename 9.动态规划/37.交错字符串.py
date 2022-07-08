'''

涉及到的题目
LeetCode 97

'''
'''
leetcode 97
97. 交错字符串
给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。
两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：
s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
注意：a + b 意味着字符串 a 和 b 连接。


示例 1：
输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出：true

示例 2：
输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出：false

示例 3：
输入：s1 = "", s2 = "", s3 = ""
输出：true
'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        '''
        dp[i][j]表示s1的前i个元素和s2的前j个元素能否由s3的前i+j个元素拼凑出来
        若s1[i] = s3[i+j],如果要满足拼凑出来的条件，
            那么s1的前i-1个元素和s2的前i个元素一定能被s3的前i+j-1个元素拼凑出来
        若s2[j] = s3[i+1],如果要满足拼凑出来的条件，
            那么s2的前j-1个元素和s1的前i个元素一定能被s3的前i+j-1个元素拼凑出来
        初始化 dp[0][0]为True
            d b b c a
          t
        a
        a
        b
        c
        c
        s3: aadbbcbcac

        [[True,  False, False, False, False, False],
         [True,  False, False, False, False, False],
         [True,  True,  True,  True,  True,  False],
         [False, True,  True,  False, True,  False],
         [False, False, True,  True,  True,  True],
         [False, False, False, True,  False, True]]

        '''
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n3 != n1 + n2: return False
        dp = [[False for _ in range(n2+1)] for _ in range(n1+1)]
        dp[0][0] = True
        for i in range(n1+1):
            for j in range(n2+1):
                if i > 0 and s1[i-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j]
                if j > 0 and s2[j-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j] or dp[i][j-1]
        # print(dp)
        return dp[-1][-1]