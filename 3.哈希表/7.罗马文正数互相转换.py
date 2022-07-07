'''

涉及到的题目
leetcode 12、13

'''
'''
leetcode 12
12. 整数转罗马数字
罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，
例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。
同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给你一个整数，将其转为罗马数字。

示例 1:
输入: num = 3
输出: "III"

示例 2:
输入: num = 4
输出: "IV"

示例 3:
输入: num = 9
输出: "IX"

示例 4:
输入: num = 58
输出: "LVIII"
解释: L = 50, V = 5, III = 3.

示例 5:
输入: num = 1994
输出: "MCMXCIV"
解释: M = 1000, CM = 900, XC = 90, IV = 4.
 
'''
class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''
        while num > 0:
            if num >= 1000:
                num -= 1000
                res += 'M'
            if 900 <= num < 1000:
                num -= 900
                res += 'CM'
            if 500 <= num < 900:
                num -= 500
                res += 'D'
            if 400 <= num < 500:
                num -= 400
                res += 'CD'
            if 100 <= num < 400:
                num -= 100
                res += 'C'
            if 90 <= num < 100:
                num -= 90
                res += 'XC'
            if 50 <= num < 90:
                num -= 50
                res += 'L'
            if 40 <= num < 50:
                num -= 40
                res += 'XL'
            if 10 <= num < 40:
                num -= 10
                res += 'X'
            if 9 <= num < 10:
                num -= 9
                res += 'IX'
            if 5 <= num < 9:
                num -= 5
                res += 'V'
            if 4 <= num < 5:
                num-= 4
                res += 'IV'
            if 1 <= num < 4:
                num -= 1
                res += 'I'
        return res

class Solution:
    '''数字转罗马'''
    THOUSANDS = ["", "M", "MM", "MMM"]
    HUNDREDS = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    TENS = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    ONES = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    def intToRoman(self, num: int) -> str:
        return Solution.THOUSANDS[num // 1000] + \
            Solution.HUNDREDS[num % 1000 // 100] + \
            Solution.TENS[num % 100 // 10] + \
            Solution.ONES[num % 10]


'''
leetcode 13
13. 罗马数字转整数
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1 。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，
例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。
同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。

示例 1:
输入: s = "III"
输出: 3

示例 2:
输入: s = "IV"
输出: 4

示例 3:
输入: s = "IX"
输出: 9

示例 4:
输入: s = "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.

示例 5:
输入: s = "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.
'''
class Solution:
    def RomanToint(self, strs: str) -> int:
        '''罗马转数字
        两个指针一前一后，存在的六种特殊情况都是’大数的左边安插小数，得到的结果再做减法‘
        所以我们只需要判断前后两个字母谁大谁小即可
        如果后面的大于前面的，说明涉及到了特殊情况，处理完后指针向后移动两位
        否则就单个处理'''
        res = 0
        hash_table = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        if len(strs) == 1: return hash_table[strs]
        i, j = 0, 1
        while j < len(strs):
            pre = hash_table[strs[i]]
            post = hash_table[strs[j]]
            if pre < post:
                res += post-pre
                j += 2
                i += 2
            else:
                res += pre
                i += 1
                j += 1
            if i == len(strs) -1:
                res += hash_table[strs[i]]
        return res

