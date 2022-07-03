'''

涉及到的题目
leetcode 115

'''
'''
leetcode 115
115. 不同的子序列
给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。
字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。
（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）
题目数据保证答案符合 32 位带符号整数范围。

示例 1：
输入：s = "rabbbit", t = "rabbit"
输出：3
解释：
如下图所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
rabbbit
rabbbit
rabbbit

示例 2：
输入：s = "babgbag", t = "bag"
输出：5
解释：
如下图所示, 有 5 种可以从 s 中得到 "bag" 的方案。 
babgbag
babgbag
babgbag
babgbag
babgbag
'''


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        '''
                    b a b g b a g
                  1 1 1 1 1 1 1 1
                b 0 1 1 2 2 3 3 3
                a 0 0 1 1 1 1 4 4
                g 0 0 0 0 1 1 1 5

                    r a b b b i t
                  1 1 1 1 1 1 1 1
                r 0 1 1 1 1 1 1 1
                a 0 0 1 1 1 1 1 1
                b 0 0 0 1 2 3 3 3
                b 0 0 0 0 1 3 3 3
                i 0 0 0 0 0 0 3 3
                t 0 0 0 0 0 0 0 3

        dp[i][j]表示字符串t[0:i-1]（闭区间）在s[0:j-1]（闭区间）中的子序列个数
        先抛开初始化，双串的题目基本上都是这样一个二维dp数组，自然而然，最重要的点就在于s[j-1] 与 t[i-1]大小是否相同
        当s[j-1] == t[i-1]，对应于dp就是dp[i][j]，为什么状态方程是dp[i][j] = dp[i-1][j-1]+dp[i][j-1]?
            举个例子，s='rara', t='ra',当j=4，i=2的时候，这个时候都对应着'a'
            如果我们用s的最后一位a，那么t的最后一位a也要被消耗掉，能够组成的子序列实际上等于rar与r组成的子序列，所以这个情况数量为dp[i-1][j-1]
            如果我们不用s的最后一位，那么此时情况就变成求rar与ra组成的子序列个数，所以这个情况数量为dp[i][j-1]
        当s[j-1] != t[i-1]，例如s='rarb', t='ra',显然当j=4,i=2的时候，b和a不一样，不一样的话，那我们就要将s退回一位，判断rar与ra能组成的子序列个数
        所以dp[i][j] = dp[i][j-1]

        至于初始化,为了能让第一个字符匹配的时候能够开始计算，第一排全部变为1，例如babgbab和bag这个例子，当第一个b相等的时候，右上角有1可以使用
        同时在bag的b匹配之后第2个第3个b的时候，右上角始终能有1可以与之相加。
        具体一样就是当t为空字符串的时候t不管怎么分都只能分出一个空字符串与之匹配
        '''
        n1, n2 = len(s), len(t)
        dp = [[0 for _ in range(n1 + 1)] for _ in range(n2 + 1)]
        for k in range(n1 + 1): dp[0][k] = 1
        for i in range(1, n2 + 1):
            for j in range(i, n1 + 1):
                if s[j - 1] == t[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]
