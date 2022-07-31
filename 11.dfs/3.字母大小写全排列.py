'''

涉及到的题目
leetcode 784

'''
'''
leetcode 784
784. 字母大小写全排列
给定一个字符串 s ，通过将字符串 s 中的每个字母转变大小写，我们可以获得一个新的字符串。
返回 所有可能得到的字符串集合 。以 任意顺序 返回输出。

示例 1：

输入：s = "a1b2"
输出：["a1b2", "a1B2", "A1b2", "A1B2"]
示例 2:

输入: s = "3z4"
输出: ["3z4","3Z4"]
'''

# 本题考虑用dfs来做，遍历到数字直接加入
#   遍历到字母就考虑两种情况，一个是大写，一个是小写，将其变成一棵树
#   然后一直搜下去
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        l = len(s)
        def dfs(index, subletter):
            if index == l: # 搜索中止条件，index已经搜到了尽头
                res.append(subletter) # 将当前情况的答案append到数组中
                return
            if s[index].isdigit(): # 遇到数字直接加上
                dfs(index+1, subletter + s[index])

            elif s[index].islower(): # 遇到小写字母分两个支，一个是小写本身，一个是大写
                dfs(index+1, subletter + s[index])
                dfs(index+1, subletter + s[index].upper())

            elif s[index].isupper(): # 遇到大写字母分两个支，一个是大写本身，一个是小写
                dfs(index+1, subletter + s[index])
                dfs(index+1, subletter + s[index].lower())
        dfs(0, '') # 进入dfs
        return res