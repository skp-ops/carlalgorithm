'''

涉及到的题目
leetcode 647

'''
'''
leetcode 647
647. 回文子串
给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。
回文字符串 是正着读和倒过来读一样的字符串。
子字符串 是字符串中的由连续字符组成的一个序列。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

示例 1：
输入：s = "abc"
输出：3
解释：三个回文子串: "a", "b", "c"

示例 2：
输入：s = "aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        dp[i] 表示字符串s的前i个元素有多少个回文子串
        如何确定dp[i],当指针指向i的时候，需要考虑dp[i]的公式
        首先除去第i个元素，肯定有dp[i-1]个回文子串，第i个元素本身也是回文子串
        所以dp[i]至少等于dp[i-1]+1，再考虑第i个元素与之前其他元素组成回文子串
        例如 aabba,当i=5的时候，指针指的是最后一个a，再次遍历之前的字符串，会发现当指针为1和2的时候
        所指的元素都为a，与最后一个a相同，那么我们就要判断这两个元素之间夹杂的子串是否为回文串
        如果是的，计数器加1，最终统计完之后再加回原来的结果。
        '''
        if len(s) <= 1 : return len(s)
        dp = [0 for _ in range(len(s))]
        dp[0] = 1
        for j in range(1, len(s)):
            temp = 0
            for k in range(0, j):
                if s[k] == s[j]:
                    if j - k == 1 : temp += 1 # 如果前后指针碰巧挨在一起，也能组成一个回文子串 bba a，最后一个a与倒数第二个a也能组合成回文串
                    elif s[k+1:j] == s[j-1:k:-1]: temp += 1 # abb a, 最后一个a与第一个a之间夹住的bb是回文串
            dp[j] = dp[j-1] + temp + 1
        return dp[-1]

'''
1.确定dp数组（dp table）以及下标的含义
布尔类型的dp[i][j]：表示区间范围[i,j] （注意是左闭右闭）的子串是否是回文子串，如果是dp[i][j]为true，否则为false。

2.确定递推公式
在确定递推公式时，就要分析如下几种情况。

整体上是两种，就是s[i]与s[j]相等，s[i]与s[j]不相等这两种。
    当s[i]与s[j]不相等，那没啥好说的了，dp[i][j]一定是false。
    当s[i]与s[j]相等时，这就复杂一些了，有如下三种情况
        情况一：下标i 与 j相同，同一个字符例如a，当然是回文子串
        情况二：下标i 与 j相差为1，例如aa，也是回文子串
        情况三：下标：i 与 j相差大于1的时候，例如cabac，此时s[i]与s[j]已经相同了，
        我们看i到j区间是不是回文子串就看aba是不是回文就可以了，那么aba的区间就是 i+1 与 j-1区间，
        这个区间是不是回文就看dp[i + 1][j - 1]是否为true。

result就是统计回文子串的数量。
注意这里我没有列出当s[i]与s[j]不相等的时候，因为在下面dp[i][j]初始化的时候，就初始为false。

3.dp数组如何初始化
dp[i][j]可以初始化为true么？ 当然不行，怎能刚开始就全都匹配上了。
所以dp[i][j]初始化为false。

4.确定遍历顺序
遍历顺序可有有点讲究了。
首先从递推公式中可以看出，情况三是根据dp[i + 1][j - 1]是否为true，在对dp[i][j]进行赋值true的。
dp[i + 1][j - 1] 在 dp[i][j]的左下角,所以一定要从下到上，从左到右遍历，这样保证dp[i + 1][j - 1]都是经过计算的。

'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]
        result = 0
        for i in range(len(s)-1, -1, -1): #注意遍历顺序
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 1: #情况一 和 情况二
                        result += 1
                        dp[i][j] = True
                    elif dp[i+1][j-1]: #情况三
                        result += 1
                        dp[i][j] = True
        return result