'''

涉及到的题目
LeetCode 20

'''
'''
leetcode 20
给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串 s ，判断字符串是否有效。

有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

示例 1：
输入：s = "()"
输出：true

示例2：
输入：s = "()[]{}"
输出：true

示例3：
输入：s = "(]"
输出：false

示例4：
输入：s = "([)]"
输出：false

示例5：
输入：s = "{[]}"
输出：true

https://leetcode.cn/problems/valid-parentheses

'''
# 解题思路：
# 假设字符串不是有效的括号，那么我们分析一下失效的原因是什么
#     1.左括号多了 {{{{{(({[]}))
#     2.右括号多了 (({[]}))}}}}}
#     3.左右括号不匹配 [)
#
# 所以我们遍历这个字符串，并且利用栈来寻找对应的括号组合。
# 每遍历一个左括号，向栈里面推入一个对应匹配的右括号，每遍历一个右括号则弹出栈里最外层的元素
#
# 这里遍历右括号会出现多种判断结果：
#     1.如果此时栈为空，没有可以弹出的元素，返回False 对应的情况是 [])，前面中括号遍历完之后，遍历 ) 时栈里没有元素了，所以FALSE
#     2.如果此时遍历的右括号与栈最外面的元素不一致，返回False，对应的情况是 [) ，此时栈里有 ],但是 ] 与 ）不符合，所以FALSE
#     3.如果遍历到最后栈里还有多余的元素，返回False，对应的情况是 (([， 这种情况没有与之匹配的括号，所以FALSE
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(':
                stack.append(')')
            elif i == '[':
                stack.append(']')
            elif i == '{':
                stack.append('}')
            elif stack == [] or stack[-1] != i:
                # 这里注意 stack == [] 和 stack[-1] != i 这两个判断不能交换位置，因为当字符串右边有多余的括号时，会造成越界
                # 例如字符串‘{}[])’ 这里匹配完{}与[]后，stack为空，假如先进行stack[-1] != i会造成index out of range
                return False
            else:
                stack.pop()
        return True if stack == [] else False

# 解法二：使用字典，空间复杂度增加。本质还是跟解法一一样。
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        vardict = {
            '(':')',
            '[':']',
            '{':'}'
        }
        for i in s:
            if i in vardict.keys():
                stack.append(vardict[i])
            elif stack == [] or stack[-1] != i:
                return False
            else:
                stack.pop()
        return True if stack == [] else False