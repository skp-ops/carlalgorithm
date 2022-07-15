'''

涉及到的题目
leetcode 745

'''
'''
leetcode 745
745. 前缀和后缀搜索
设计一个包含一些单词的特殊词典，并能够通过前缀和后缀来检索单词。
实现 WordFilter 类：

WordFilter(string[] words) 使用词典中的单词 words 初始化对象。
f(string pref, string suff) 返回词典中具有前缀 prefix 和后缀 suff 的单词的下标。
如果存在不止一个满足要求的下标，返回其中 最大的下标 。如果不存在这样的单词，返回 -1 。

示例：
输入
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
输出
[null, 0]
解释
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // 返回 0 ，因为下标为 0 的单词：前缀 prefix = "a" 且 后缀 suff = "e" 。
'''
class WordFilter:
    '''暴力穷举，将每个下标的前后缀情况列举出来
    再去寻找题目中要求的前后缀，如果存在就返回该word的坐标
    否则返回-1'''
    def __init__(self, words: List[str]):
        hash_map = {}
        for index, word in enumerate(words):
            for a in range(len(word)+1):
                pre = word[:a]
                for b in range(len(word)+1):
                    post = word[b:]
                    hash_map[(pre,post)] = index
        self.hash_map = hash_map
    def f(self, pref: str, suff: str) -> int:
        if (pref, suff) in self.hash_map:
            return self.hash_map[(pref, suff)]
        else:
            return -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)