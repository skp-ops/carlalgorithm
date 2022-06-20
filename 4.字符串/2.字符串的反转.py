'''

涉及到的题目
LeetCode 344、541、151
剑指 Offer 58 - II. 左旋转字符串

'''

'''
leetcode 344
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

示例 1：
输入：s = ["h","e","l","l","o"]
输出：["o","l","l","e","h"]

示例 2：
输入：s = ["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]

https://leetcode.cn/problems/reverse-string

'''
# 一般来说这种题目考察的是对于字符串的操作，而非对库的调用，所以利用左右指针，调换字符的位置，然后更新指针，直到两个指针相遇结束循环
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left , right = 0, len(s)-1
        while left<right:
            s[left],s[right] = s[right],s[left]
            left += 1
            right -= 1

# 如果用库函数来写的话,解法如下
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse() # 列表倒叙输出
        # 注意：a.sort(reverse = True)表示，先将列表排序，再倒叙输出。

'''
leetcode 541
给定一个字符串 s 和一个整数 k，从字符串开头算起，每计数至 2k 个字符，就反转这 2k 字符中的前 k 个字符。
如果剩余字符少于 k 个，则将剩余字符全部反转。
如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。

示例 1：
输入：s = "abcdefg", k = 2
输出："bacdfeg"

示例 2：
输入：s = "abcd", k = 2
输出："bacd"

https://leetcode.cn/problems/reverse-string-ii

'''
# 首先计算出字符串s的长度，算出需要经历多少个循环，每次循环翻转前k个字符的位置。
# 等到循环结束之后再计算剩下的长度为多少，与k进行比较。假如小于k，则剩下的字符全部翻转，否则就翻转前k个字符

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        loop = len(s) // (2 * k)
        a = list(s)

        for n in range(loop):
            left, right = 2 * n * k, (2 * n + 1) * k - 1
            while left < right:
                a[left], a[right] = a[right], a[left]
                left += 1
                right -= 1

        if len(s) - 2 * k * loop < k:
            left, right = 2 * k * loop, len(a) - 1
        else:
            left, right = 2 * k * loop, 2 * k * loop + k - 1

        while left < right:
            a[left], a[right] = a[right], a[left]
            left += 1
            right -= 1

        return ''.join(a)
# 解法二   1. 使用range(start, end, step)来确定需要调换的初始位置
#         2. 对于字符串s = 'abc'，如果使用s[0:999] ===> 'abc'。
#               字符串末尾如果超过最大长度，则会返回至字符串最后一个值，这个特性可以避免一些边界条件的处理。
#         3. 用切片整体替换，而不是一个个替换.
class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        def reverse_substring(text):
            left, right = 0, len(text) - 1
            while left < right:
                text[left], text[right] = text[right], text[left]
                left += 1
                right -= 1
            return text

        res = list(s)

        for cur in range(0, len(s), 2 * k):
            res[cur: cur + k] = reverse_substring(res[cur: cur + k])

        return ''.join(res)

'''
leetcode 151
给你一个字符串 s ，颠倒字符串中 单词 的顺序。
单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。
返回 单词 顺序颠倒且 单词 之间用单个空格连接的结果字符串。
注意：输入字符串 s中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。

示例 1：
输入：s = "the sky is blue"
输出："blue is sky the"

示例 2：
输入：s = " hello world "
输出："world hello"
解释：颠倒后的字符串中不能存在前导空格和尾随空格。

示例 3：
输入：s = "a good  example"
输出："example good a"
解释：如果两个单词间有多余的空格，颠倒后的字符串需要将单词间的空格减少到仅有一个。

https://leetcode.cn/problems/reverse-words-in-a-string

'''
# 调库方法
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1]) # 其中s.split()返回一个列表，将所有空格清除掉

# 不使用库函数
# 分三步:
#   先翻转整个数组
#   再翻转单个单词
#   清除多余空格
class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        lens = len(s)

        # 翻转一个数组
        def reverse(a: list, l, r):
            while l < r:
                a[l], a[r] = a[r], a[l]
                l += 1
                r -= 1

        # 翻转一个单词
        def reverse_single_word(a: list):
            i = j = 0
            while i < lens:
                while i < lens and a[i] == ' ':  # 寻找一个单词的首字母
                    i += 1
                j = i  # 找到单词的首字母之后将i的值赋给j，使得ij在同一个地方
                while j < lens and a[j] != ' ':  # 寻找一个单词的末位置
                    j += 1
                reverse(a, i, j - 1)
                i = j

        # 清除前后包括单词中间多余空格
        def remove_space(a: list):
            slow, fast = 0, 0
            lens = len(s)
            while fast < lens:
                while fast < lens and s[fast] == ' ':  # 寻找一个单词的开头
                    fast += 1
                while fast < lens and s[fast] != ' ':  # 找到了一个单词的开头，将该单词移动到slow的位置
                    s[slow] = s[fast]
                    slow += 1
                    fast += 1
                while fast < lens and s[fast] == ' ':  # 遍历完该单词之后继续向后过滤空格，寻找第二个单词的开头
                    fast += 1
                if fast < lens:  # 第一个单词填充完之后与第二个单词之间要填充一个空格
                    s[slow] = ' '
                    slow += 1
            return ''.join(s[:slow])  # 将i之前的元素组合起来

        reverse(s, 0, lens - 1)
        reverse_single_word(s)
        return remove_space(s)

'''
剑指 Offer 58
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。
比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

示例 1：
输入: s = "abcdefg", k = 2
输出:"cdefgab"

示例 2：
输入: s = "lrloseumgh", k = 6
输出:"umghlrlose"

https://leetcode.cn/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof

'''
# 将原来的字符串转化为数组，然后添加k个空位。
# 利用双指针,将前k个元素复制到后k个空位中,然后输出后半部分就行
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        lens = len(s)
        s = list(s) + [' ']*n
        l , r = 0 , lens
        while r < len(s):
            s[r] = s[l]
            r += 1
            l += 1
        return ''.join(s[n:])

# 方法二,直接利用切片
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[0:n]

# 方法三,如果不能用方法二,并且不能申请额外的空间,可以先将0-n个元素翻转，再将n个之后的元素翻转。最后整个列表一起翻转
# 例如 字符串abcdefg，n=2
# 前2个翻转一次为 bacdefg
# 后面5个翻转一次为 bagfedc
# 最后整个一起翻转 cdefgab
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        s = list(s)
        s[:n] = list(reversed(s[:n]))
        # 这里reversed(s)输出的是一个迭代器，需要用list()转换成数组
        s[n:] = list(reversed(s[n:]))
        s.reverse()
        return ''.join(s)