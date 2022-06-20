'''

涉及到的题目
LeetCode 150

'''
'''
leetcode 150
根据 逆波兰表示法，求表达式的值。
有效的算符包括+、-、*、/。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
注意两个整数之间的除法只保留整数部分。
可以保证给定的逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。

示例1：
输入：tokens = ["2","1","+","3","*"]
输出：9
解释：该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9

示例2：
输入：tokens = ["4","13","5","/","+"]
输出：6
解释：该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6

示例3：
输入：tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
输出：22
解释：该算式转化为常见的中缀算术表达式为：
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

https://leetcode.cn/problems/evaluate-reverse-polish-notation

'''
# 解题思路，利用栈的思想，遍历表达式，判断是否是运算符号，
#       如果不是就append到栈里，如果是运算符号，就弹出两个栈里的元素，first 和 second，
# 通过例子我们可以看出来，先弹出的元素放在后面运算。然后将运算完的结果推入栈，继续等待之后的运算。
# 直到遍历结束，输出栈的最后一位即是结果
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in ['+','-','*','/']:
                stack.append(i)
            else:
                a , b = int(stack.pop()) , int(stack.pop())
                res = int(eval(f'{b}{i}{a}')) # 注意这里用了eval函数，同时先弹出的a要放在运算符后面运算，在减法和除法中至关重要
                '''
                eval() 函数用来执行一个字符串表达式，并返回表达式的值。
                >>>x = 7
                >>> eval( '3 * x' ) ------21
                >>> eval('pow(2,2)') ------4
                >>> eval('2 + 2') ------4
                >>> n=81
                >>> eval("n + 4") ------85
                '''
                stack.append(res)
        return int(stack[-1])

# 利用lambda表达式和字典来实现eval函数
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        plus = lambda a,b:a+b
        minus = lambda a,b:a-b
        time = lambda a,b:a*b
        divide = lambda a,b:int(a/b)
        vardict = {
            '+':plus,
            '-':minus,
            '*':time,
            '/':divide
        }
        stack = []
        for i in tokens:
            if i not in vardict:
                stack.append(i)
            else:
                a , b = int(stack.pop()) , int(stack.pop())
                res = vardict[i](b,a)
                stack.append(res)
        return int(stack[-1])