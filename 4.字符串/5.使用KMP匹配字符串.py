'''

涉及到的题目
leetcode 28

'''
'''
实现strStr()函数。
给你两个字符串haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回 -1 。

说明：
当needle是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当needle是空字符串时我们应当返回 0 。这与 C 语言的strstr()以及 Java 的indexOf()定义相符。

示例 1：
输入：haystack = "hello", needle = "ll"
输出：2

示例 2：
输入：haystack = "aaaaa", needle = "bba"
输出：-1

示例 3：
输入：haystack = "", needle = ""
输出：0

https://leetcode.cn/problems/implement-strstr

'''
# 首先getnext函数可以看4.KMP算法理论基础，其中有解释如何得到next这个前缀表的
# 接下来就是要看如何利用这个前缀表来进行字符串的匹配。
# 在strStr这个函数中，haystack是文本串，needle是模式串，
#   我们先获取两个串的长度，分别为lens1和lens2，依据题目意思，假如lens2为0，直接返回0。
#   然后就是调用getnext函数，我们将模式串的前缀表生成出来，存储在next数组里。
#   初始化两个指针，i指针用来指文本串，j指针用来指模式串，这样while这个大循环下要满足i不超过lens1，j不超过lens2。
#       这里开始两个判断：
#           1.假如j==-1，说明j在next列表中已经处于最开始的位置，j不能再往后退了，所以ij两个指针同时向前走，开始从头进行匹配
#              假如haystack[i] == needle[j]，说明此时两者匹配成功，将ij往后移动一位，继续进行匹配
#           2.假如此时两者匹配不成功，并且j也没有回到next列表的原位，则j移动到next[j]的位置，开始尽最大可能寻找公共串以减少匹配时间
class Solution:
    def getnext (self, n:int, moshichuan:list) -> list:
        next = ['' for i in range(n)]
        j, k = 0, -1
        next[0] = k
        while j < n-1:
            if k == -1 or moshichuan[j] == moshichuan[k]:
                j += 1
                k += 1
                next[j] = k
            else:
                k = next[k]
        return next
    def strStr(self, haystack: str, needle: str) -> int:
        lens1 = len(haystack)
        lens2 = len(needle)
        if lens2 == 0:
            return 0
        next = self.getnext(lens2,needle)
        i = j = 0
        while i < lens1 and j < lens2:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        if j == lens2:
            return i-j
        return -1