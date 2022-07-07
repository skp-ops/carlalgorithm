'''

涉及到的题目
leetcode 32

'''
'''
leetcode 32
32. 最长有效括号
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

示例 1：
输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"

示例 2：
输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"

示例 3：
输入：s = ""
输出：0
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1] # 栈只记录左括号坐标，给一个初始值-1
        max_len = 0
        if not s: return 0
        for i in range(len(s)):
            if s[i] == '(': # 遇到右括号就记录下坐标
                stack.append(i)
            else: # 遇到左括号先弹栈
                stack.pop()
                if not stack: # 假设弹的就是最后一个元素，说明之前就没有左括号
                    stack.append(i) # 将当前右括号的位置当成初始值推入栈
                else:
                    # 如果弹完栈之后还有元素，说明先前已经获取到了左括号，
                    # 直接记录当前i到左括号的距离就是有效括号长度。
                    # 初始值-1就说明了如果一开始就能匹配上 如()
                    # 栈的变化是[-1] -> i=0, [-1,0] -> i=1, [-1], max_len = 1-(-1)=2
                    max_len = max(max_len, i-stack[-1])
        return max_len