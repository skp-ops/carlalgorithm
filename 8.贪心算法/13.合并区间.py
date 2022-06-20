'''

涉及到的题目
leetcode 56

'''
'''
56. 合并区间
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

示例 1：
输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2：
输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
'''
# 本题思路在于如何尽可能求出最大的重叠区间。
# 有一个需要注意的点是，假如区间2和区间1重合，区间2和区间3重合，但是区间1和区间3不重合，仍然能组成一个区间
# 所以我们可以先将数组排序，然后假设区间能重合，就不断更新区间的最大右边界，不断吸取其他重合区间
# 左区间不需要改变，因为遍历是从左到右的顺序，每次寻找新的重合区间时，i的左区间都会是固定的。
# 然后将所有的答案append到res里，最后输出即可
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        temp = [intervals[0][0],intervals[0][1]] # 记录初始区间，temp
        res = [] # 用来存放组合完的答案
        for i in range(1,len(intervals)):
            if intervals[i][0] <= temp[1]: # 新区间的左边界落在里当前temp右边界里，说明有重合
                temp[1] = max(temp[1],intervals[i][1]) # 更新右边界，使其最大化，以此获得更多的重合机会
                continue
            else: # 一旦不重合，说明这个重合区间已经达到最大，需要append答案，并且开始新的循环
                res.append(temp) # 将答案推入res中
                temp = [intervals[i][0],intervals[i][1]] # 重新更新temp区间，继续寻找新的重合区间
        res.append(temp) # 循环到最后一步，将当前的temp大区间推入答案，就是最终所有的结果
        return res