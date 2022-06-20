'''

涉及到的题目
LeetCode 131

'''
'''
leetcode 131
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
回文串 是正着读和反着读都一样的字符串。

示例 1：
输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]

示例 2：
输入：s = "a"
输出：[["a"]]

https://leetcode.cn/problems/palindrome-partitioning

'''
# 首先定义一个res用来装输出结果，定义一个path用来收集分割过的子串，然后定义一个函数来判断是否为回文串。
# 接下来就是利用回溯算法分割，由于是在单个字符串中遍历，所以需要start_index来确定起始位置
# 指针i从起始位置开始遍历，遇到回文串，就返回start_index到i中间包含的字符串，append到path里
# 最终当start_index走到头，无法继续遍历，判断如果path里有元素则将path推入到res中，然后return
'''
对于字符串abcdef而言
组合问题：选取一个字符a之后，从bcdef中选取第二个字符；选取b之后，在cedf中选取第三个字符……
分割问题：切割一个字符a之后，从bcedf中切割第二段字符，切割b之后，在cedf中切割第三段字符……
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def huiwen(t): # 定义一个函数来判断t是否为回文串
            if len(t) == 1:
                return True
            left, right = 0, len(t) - 1
            while left < right:
                if t[left] != t[right]:
                    return False
                else:
                    left += 1
                    right -= 1
            return True
        '''
        或者直接判断
                    t == t[::-1] 也可以知道t是否为回文，上面用的是双指针法
        '''

        def backtracking(s, start_index):

            if path and start_index == len(s): # 退出循环的条件
                res.append(path[:])
                return

            for i in range(start_index, len(s)): # 单循环逻辑
                if huiwen(s[start_index:i + 1]):
                    path.append(s[start_index:i + 1])
                    backtracking(s, i + 1) # 更新start_index的坐标
                    path.pop() # 回溯操作

        backtracking(s, 0)
        return res
