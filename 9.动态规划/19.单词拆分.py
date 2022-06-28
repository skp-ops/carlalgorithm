'''

涉及到的题目
leetcode 139

'''
'''
leetcode 139
139. 单词拆分
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。
注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。

示例 2：
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
     注意，你可以重复使用字典中的单词。
     
示例 3：
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[0] = True
        for j in range(1, len(s)+1):
            for i in range(len(wordDict)):
                if j >= len(wordDict[i]):
                    dp[j] = dp[j] or (dp[j-len(wordDict[i])] and s[j-len(wordDict[i]):j] in wordDict)
                    # 判断中第一个dp表示，如果在之前的word中dp[j]已经可以被凑出来，那么之后无论有多少个word在worddict中都无所谓，所以连接用or
                    # or之后的括号，dp[j-len(wordDict[i])]表示在s[:j]这个子串中，左半部分s[:j-len(wordDict[i]]要能够组合出来，
                    #               并且右半部分也是worddict中的一个才能证明s[:j]可以被组合
        return dp[-1]