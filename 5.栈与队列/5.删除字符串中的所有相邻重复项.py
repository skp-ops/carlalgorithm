'''

涉及到的题目
LeetCode 1047

'''
'''
leetcode 1047

给出由小写字母组成的字符串S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
在 S 上反复执行重复项删除操作，直到无法继续删除。
在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。

示例：
输入："abbaca"
输出："ca"
解释：
例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。
之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。

https://leetcode.cn/problems/remove-all-adjacent-duplicates-in-string

'''
# 常规解法，利用栈来解决这个问题，当有两个相接触的元素时，抵消，就正好类似于栈的append与pop
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for item in s:
            if not stack or stack[-1] != item: # 判断如果stack是空的，或者stack最外面的元素与item不一样，就append进去
                stack.append(item)
            else:
                stack.pop() # 如果栈最外层的元素与item一样，就说明有相邻的重复元素，然后就pop出去
        return ''.join(stack) # 最后合并列表成字符串

#  假如不让用栈，就用双指针来操作
class Solution:
    def removeDuplicates(self, s: str) -> str:
        '''
        双指针解法
        '''
        res = list(s)
        fast = slow = 0
        while fast < len(res):
            res[slow] = res[fast]
            '''
            快指针一直向前走，慢指针假如经过两个相邻重复项，即res[slow] == res[slow-1]，慢指针就会回退一格
            同时将快指针的值赋值给当前的慢指针。
            如何理解这个操作：慢指针之后的值都是需要舍弃的，所以遇到要舍弃的重复项时，慢指针回退一格。
            但是不可避免当前保留的值可以与快指针值的地方组成相邻重复项，所以把快指针的值搬运到慢指针这里进行判断
            同时，快指针之后可能有需要我们保留的值，所以需要把待保留的值给搬运到慢指针里面，所以res[slow] = res[fast] 很重要。
            '''

            if slow > 0 and res[slow] == res[slow-1]:
                slow -= 1
            else:
                slow += 1
            fast += 1
        return ''.join(res[0:slow])