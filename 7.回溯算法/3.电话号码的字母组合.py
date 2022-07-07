'''

涉及到的题目
LeetCode 17

'''
'''
leetcode 17
给定一个仅包含数字2-9的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
phone_number = {
            '1':'',
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
示例 1：
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]

示例 2：
输入：digits = ""
输出：[]

示例 3：
输入：digits = "2"
输出：["a","b","c"]

https://leetcode.cn/problems/letter-combinations-of-a-phone-number

'''

# 列举法，分别考虑给定的digits长度为0,1,2,3,4的情况，然后分别写出对应的组合
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        vardict = {
            '1':'','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'
        }
        if len(digits) == 0:
            return []

        elif len(digits) == 1:
            return [i for i in vardict[digits]]

        elif len(digits) == 2:
            res = []
            for i in vardict[digits[0]]:
                for j in vardict[digits[1]]:
                    res.append(i+j)
            return res

        elif len(digits) == 3:
            res = []
            tempt = []
            for i in vardict[digits[0]]:
                for j in vardict[digits[1]]:
                    tempt.append(i+j)
            for k in vardict[digits[2]]:
                for l in tempt:
                    res.append(l+k)
            return res

        elif len(digits) == 4:
            res = []
            tempt1 =[]
            tempt2 =[]
            for i in vardict[digits[0]]:
                for j in vardict[digits[1]]:
                    tempt1.append(i+j)
            for m in vardict[digits[2]]:
                for n in vardict[digits[3]]:
                    tempt2.append(m+n)
            for x in tempt1:
                for y in tempt2:
                    res.append(x+y)
            return res

# 回溯法一

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        vardict = {
            '1':'','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'
        }
        res = []
        path = []
        def backtracking(digits,start_index):
            if len(path[:]) == len(digits):
                p = ''.join(path[:])
                res.append(p)
                return

            for i in range(start_index,len(digits)):
                if len(path) != i:
                    return # 剪枝操作，假设有三个数，一个数对应的字母只能取一个，当path里只有一个字母，但是遍历到第三个数的时候，则不满足要求，直接返回
                a = digits[i]
                for j in range(0,len(vardict[a])):
                    path.append(vardict[a][j])
                    backtracking(digits,start_index+1)
                    path.pop()

        backtracking(digits,0)
        return res

# 回溯法二

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['figure storage', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def backtrack(conbination, nextdigit):
            if len(nextdigit) == 0:
                res.append(conbination)
            else:
                for letter in phone[nextdigit[0]]:
                    n = conbination + letter
                    backtrack(n, nextdigit[1:])
        #             每循环一次，digit就往前移动一位，例如digit=23
        #             第一次循环，获得了三个备选答案 [a] [b] [c] 进入下一次循环时，digit变成3（nextdigit[1:])
        #             第二次循环，获得了九个备选答案分别是 进入下一次循环时，digit变成了空，此时满足append条件
        #                         [a,d] [a,e] [a,f]
        #                         [b,d] [b,e] [b,f]
        #                         [c,d] [c,e] [c,f],每生成一个，就append一个进入res

        res = []
        backtrack('', digits)
        return res
