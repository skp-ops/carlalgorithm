'''

涉及到的题目
LeetCode 242、383、438

'''

'''
leetcode 242
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
注意：若s 和 t中每个字符出现的次数都相同，则称s 和 t互为字母异位词。


示例1:
输入: s = "anagram", t = "nagaram"
输出: true

示例 2:
输入: s = "rat", t = "car"
输出: false

https://leetcode-cn.com/problems/valid-anagram

'''

# 解法1，直接比较每个字母出现的次数是否相同，都相同则返回True，有一个不相同就返回False
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = set(list(s))
        b = set(list(t))

        if a > b:
            return False
        else:
            for i in b:
                if list(s).count(i) != list(t).count(i):
                    return False
            return True

# 解法2，因为题目中给的元素都是26个小写字母，所以将小写字母映射到数组上，即哈希表的索引上，遍历s的时候，每有一个字母，则对应哈希表的value加1
#       遍历t的时候，每有一个字母，则对应哈希表的value减1，最后如果哈希表所有values等于0则返回True，否则返回False

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26 # 将26个字母的初始个数设置为0
        for i in range(len(s)):
            record[ord(s[i])-ord('a')] += 1 # s中每有一个元素，对应位置加1

        for j in range(len(t)):
            record[ord(t[j])-ord('a')] -= 1 # t中每有一个元素，对应位置减1

        for k in range(26):
            if record[k] != 0: # 假如有一个位置的数不为0，则返回flase，否则返回true
                return False
                break
        return True

# 解法3，用defaultdict创建字典来解决
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict

        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for i in range(len(s)):
            s_dict[s[i]] += 1

        for i in range(len(t)):
            t_dict[t[i]] += 1

        if s_dict == t_dict:
            return True
        else:
            return False

'''
leetcode 383
给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。
如果可以，返回 true ；否则返回 false 。
magazine 中的每个字符只能在 ransomNote 中使用一次。

示例 1：
输入：ransomNote = "a", magazine = "b"
输出：false

示例 2：
输入：ransomNote = "aa", magazine = "ab"
输出：false

示例 3：
输入：ransomNote = "aa", magazine = "aab"
输出：true

https://leetcode-cn.com/problems/ransom-note

'''

# 直接replace方法
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in range (len(ransomNote)):
            if ransomNote[i] in magazine:
                magazine = magazine.replace(ransomNote[i],'',1)

            else:
                return False
        return True

# 解法二，利用字典存放目标元素个数
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import defaultdict
        record1 = defaultdict(int)
        record2 = defaultdict(int)

        if len(ransomNote) > len(magazine):
            return False

        for i in ransomNote:
            if i not in magazine:
                return False
            else:
                record1[i] = ransomNote.count(i)
                record2[i] = magazine.count(i)

        for j in record1:
            if record1[j] > record2[j]:
                return False
                break
        return True

# 解法三，用哈希表
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        arr = [0] * 26

        for x in magazine:
            arr[ord(x) - ord('a')] += 1

        for x in ransomNote:
            if arr[ord(x) - ord('a')] == 0:
                return False
            else:
                arr[ord(x) - ord('a')] -= 1

        return True
'''
leetcode 49
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。

示例 1:
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

示例 2:
输入: strs = [""]
输出: [[""]]

示例 3:
输入: strs = ["a"]
输出: [["a"]]

https://leetcode-cn.com/problems/group-anagrams
'''
# 解法一，利用字典的键值对，看做是一个哈希表。将strs中的每一个元素排序，当成字典的键，排序一样说明是字母异位词，
#           再将这些排序一样的值添加进同一个列表，当做该键的值。最后输出所有的值在一个列表里面就能达到要求
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in strs:
            keys = ''.join(sorted(i))
            if keys not in res:
                res[keys] = [i] # 一定要转化为列表， 这样之后才能够用append函数
            else:
                res[keys].append(i)
        return list(res.values())

# 解法二，同解法一，只是将strs中元素上的每一个字符转换成hash值相加，当成字典的key值，然后输出最后所有values
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in strs:
            key = sum(hash(j) for j in i)
            res[key] = res.setdefault(key,[]) + [i]
        return list(res.values())

'''
leetcode 438
给定两个字符串s和 p，找到s中所有p的异位词的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。

示例1:
输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。

示例 2:
输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。

https://leetcode-cn.com/problems/find-all-anagrams-in-a-string

'''
#  这道题的解法类比 数组4.长度最小的子数组中 leetcode76题的第二个解法。主要思路就是将p字符串的各个值存储在数组哈希表中，
#  每遍历一个字母，对应value加1。同时需要一个need记录所需要的元素个数。在字符串s中创建一个滑动窗口，快指针每划过一个字母，对应value减1
#  如果是目标字母,则不仅value减1,need也减1 当need=0时,判断此时滑动窗口的长度是否等于p字符串的长度,如果相等则记录slow的值,这是一个解.
#  如果长度不一样,则需要移动慢指针,慢指针每划过一个字母,对应value加1,而且当划过的是目标字母,而且目标字母是当前窗口中最后一个的时候,need加1
#  直到遍历完所有s,输出所有解,并存储在record里面

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        varlist = [0] * 26 # 创建一个数组哈希表
        record = [] # 用来记录最后的解
        need = len(p) # 所需要的字母数
        for i in range(len(p)):
            varlist[ord(p[i]) - ord('a')] += 1 # 将p中的字母映射到哈希表中

        fast, slow = 0, 0 # 创建快慢指针
        for fast in range(len(s)):
            if varlist[ord(s[fast]) - ord('a')] > 0: # 大于0，说明是需要的目标字母（不必要的字母必定小于等于0）
                need -= 1 # 快指针划过一个需要的目标字母，need减1
            varlist[ord(s[fast]) - ord('a')] -= 1 # 快指针每划过一个字母，对应value都要减1

            if need == 0: # 当前滑动窗口包含了所有我们需要的目标字母

                while need == 0:
                    if len(s[slow:fast + 1]) == len(p): # 开始判断，如果滑窗和目标字符串长度一样，说明没有其他无关字母，是其中一个解
                        record.append(slow) # 记录解的初始坐标

                    if s[slow] in p and varlist[ord(s[slow]) - ord('a')] >= 0: # 假如长度不相等，则判断当前慢指针指的位置是不是目标字母剩的最后一个
                        need += 1 # 如果是最后一个，则说明我们需要更多的目标字母，need加1
                    varlist[ord(s[slow]) - ord('a')] += 1 # 慢指针每划过一个字母，对应value加1
                    slow += 1 # 更新慢指针坐标
        return record