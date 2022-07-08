'''

涉及到的题目
LeetCode 187

'''
'''
187. 重复的DNA序列
DNA序列 由一系列核苷酸组成，缩写为 'A', 'C', 'G' 和 'T'.。
例如，"ACGAATTCCG" 是一个 DNA序列 。
在研究 DNA 时，识别 DNA 中的重复序列非常有用。
给定一个表示 DNA序列 的字符串 s ，返回所有在 DNA 分子中出现不止一次的 长度为 10 的序列(子字符串)。你可以按 任意顺序 返回答案。

示例 1：
输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
输出：["AAAAACCCCC","CCCCCAAAAA"]

示例 2：
输入：s = "AAAAAAAAAAAAA"
输出：["AAAAAAAAAA"]
 
'''
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        '''本题要求求出出现过至少两次的长度为10的子串
        我们就用哈希表记录每一个10长度子串出现的次数
        为了防止重复解以及set利用过多的空间，我们可以在子串恰好出现两次的时候记录'''
        if len(s) <= 10: return []
        from collections import defaultdict
        res = []
        hash_table = defaultdict(int)
        for i in range(len(s) - 10 + 1):
            target = s[i:i+10]
            hash_table[target] += 1
            if hash_table[target] == 2:
                res.append(target)
        return res