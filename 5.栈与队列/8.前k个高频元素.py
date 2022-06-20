'''

涉及到的题目
LeetCode 347

'''

'''
leetcode 347
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]

示例 2:
输入: nums = [1], k = 1
输出: [1]

https://leetcode.cn/problems/top-k-frequent-elements

'''
# 利用哈希表来统计每一个字符出现的次数，字符记为key，次数记为value，然后对value进行排序，输出前k个最大value对应的key
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        harshtable = dict()
        res = []
        for i in nums:
            harshtable[i] = harshtable.setdefault(i,0) + 1 # 记录下来每个字符出现的次数
        key_list = list(harshtable.keys())
        value_list = list(harshtable.values()) # 将key和value转换成列表，并且下标一一对应
        copy = value_list.copy() # 深拷贝一个value的列表，对拷贝的value排序
        copy.sort(reverse=True)
        for i in range(k):
            ind = value_list.index(copy[i]) # 确定前k个高频字符对应的index
            res.append(key_list[ind]) # 在key里面找到对应的字符后输出到res里
            value_list[ind] = '' # 为了防止两个字符出现频率一样，而导致无法正常输出答案，每次输出都将表格里的元素替换掉
            key_list[ind] = ''
        return res

# 字典排序
# 注意在使用sorted排序字典时，必须要将字典变成dict.items()形式，后面key里的参数，用lambda表达式来控制排序key还是排序value
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        harshtable = dict()
        for i in nums:
            harshtable[i] = harshtable.setdefault(i,0) + 1
        a = sorted(harshtable.items(), key = lambda x:x[1], reverse = True)
        # key是代表着要进行排序的对象，如果是x[1]说明是用value的值来排序，如果是x[0]则说明是用key的值来排序。
        # print(a)
        res = [i[0] for i in a[:k]] # 由于a此时是一个二维数组，所以我们值需要输出每一个元素数组里第一个元素即可，即只输出key的值
        return res

# 利用小顶堆来排序,前面的操作都是一样的,创建一个字典然后利用value来记录key的频率.
# 之后不同的处理方式就是枚举出(value,key)这个组合，将其放入到最小堆里面来生成一个树，控制树的容量一共有k个元素。
# 一旦超过k，就自动排除掉频率最低的那个元素，直到遍历结束，输出这个树里面（value，key）组合中所有key的值
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vardict = dict()
        for i in nums:
            vardict[i] = vardict.setdefault(i,0) + 1
        # 对频率用小顶堆进行排序
        prior_q = [] # 创建一个小顶堆
        for key, frequency in vardict.items():
            heapq.heappush(prior_q,(frequency,key)) # 将频率和键推入小顶堆中，同时以frequency来进行堆排序
            if len(prior_q) > k:
                heapq.heappop(prior_q) # 因为我们需要取前k个值，所以超过k个时，就自动剔除掉当前最小频率的值
        res = []
        for i in range(k):
            res.append(heapq.heappop(prior_q)[1]) # 弹出的一个值是（frequency，key）的组合，我们要提取出key，所以后面加一个[1]
        return res
'''
什么是小顶堆，小顶堆就是一个二叉树，每一个字树的父大于两个子，然后一直排序下去
import heapq
L= {
    'a':4,'c':3,'h':1,'b':5
}
q = []
for key,frequency in L.items():
    heapq.heappush(q,(key,frequency))
# print(q) [('a', 4), ('b', 5), ('h', 1), ('c', 3)]
        a
    b       h
c


for key,frequency in L.items():
    heapq.heappush(q,(frequency,key))
# print(q) [(1, 'h'), (4, 'a'), (3, 'c'), (5, 'b')]
        1
    4       3
5


#############################################

a = [1,3,5,7,9,12,46,7,9,45,3,1,2]
pre_q =[]
for i in a:
    heapq.heappush(pre_q,i)
# print(pre_q) [1, 3, 1, 7, 3, 2, 46, 7, 9, 45, 9, 12, 5]
#                                                 1
#                                 3                             1
#                         7               3               2          46
#                     7       9       45      9       12      5
'''