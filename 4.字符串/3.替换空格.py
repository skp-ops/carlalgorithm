'''

涉及到的题目
剑指 Offer 05. 替换空格

'''

'''
剑指 Offer 05
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1：
输入：s = "We are happy."
输出："We%20are%20happy."

https://leetcode.cn/problems/ti-huan-kong-ge-lcof

'''
# 这道题最优的解就是利用双指针来完成。题目中有n个空格，我们就要适当扩展数组，扩展的个数刚好能容纳n个'%20'。
# 然后利用两个指针，从后向前替换空格，
# 为什么不能从前向后填充？因为从前向后填充就是O(n^2)的算法了，每次添加元素都要将添加元素之后的所有元素向后移动。
# 其实很多数组填充类的问题，都可以先预先给数组扩容带填充后的大小，然后在从后向前进行操作。
#   这么做有两个好处：
#       不用申请新数组。
#       从后向前填充元素，避免了从前先后填充元素要来的 每次添加元素都要将添加元素之后的所有元素向后移动。
class Solution:
    def replaceSpace(self, s: str) -> str:
        a = list(s)
        b = a + ['']*2*a.count('*') #  也可以用函数a.extend([' ']*2*a.count('*'))

        if len(a) == len(b):
            return s # 假设没有空格，直接返回 s
        fast,slow = len(b)-2,len(b)-1
        while fast >= 0:
            if b[fast] == '':
                pass
            elif b[fast] != '*':
                b[slow] = b[fast]
                slow -= 1
            elif b[fast] == '*':
                b[slow],b[slow-1],b[slow-2] = '0','2','%'
                slow -= 3
            fast -= 1
        return ''.join(b)