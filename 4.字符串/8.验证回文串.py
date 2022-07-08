'''

涉及到的题目
LeetCode 125

'''
'''
leetcode 125
125. 验证回文串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true
解释："amanaplanacanalpanama" 是回文串

示例 2:
输入: "race a car"
输出: false
解释："raceacar" 不是回文串
'''
'''
思路很简单，一种是排除所有其他杂字符，只保留数字和字母，判断是否为回文
        一种是用双指针，一左一右，遇到数字或者字母就判断是否一样。
        如果出现一次不一样就返回False，否则遍历结束返回True
        
这里总结三个可以方便使用的函数:
str.isdigit()
    Python isdigit() 方法检测字符串是否只由数字组成，只对 0 和 正数有效。
    如果字符串只包含数字则返回 True 否则返回 False。
    
str.isalpha()
    Python isalpha() 方法检测字符串是否只由字母或文字组成。
    如果字符串至少有一个字符并且所有字符都是字母或文字则返回 True，否则返回 False。

str.isalnum()
    isalnum() 方法检测字符串是否由字母和数字组成。
    如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        store = []
        for cha in s:
            if cha.isalnum():
                store.append(cha.lower())
        res = ''.join(store)
        return res == res[::-1]

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right =0, len(s)-1
        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
            elif s[left].isalnum() is False: left += 1
            elif s[right].isalnum() is False: right -= 1
        return True