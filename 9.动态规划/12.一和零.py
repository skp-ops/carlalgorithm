'''

涉及到的题目
leetcode 474

'''
'''
474. 一和零
给你一个二进制字符串数组 strs 和两个整数 m 和 n 。
请你找出并返回 strs 的最大子集的长度，该子集中 最多 有 m 个 0 和 n 个 1 。
如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。

示例 1：
输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
输出：4
解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。

示例 2：
输入：strs = ["10", "0", "1"], m = 1, n = 1
输出：2
解释：最大的子集是 {"0", "1"} ，所以答案是 2 。
'''
class Solution:
    '''
    具体套路就是分析出这道题可以用背包模型来套
    需要求的是元素子集的最大值，这个最大值可以对应背包问题的最大价值
    同时给出的限制条件是0和1的数量不能超过一定限度，这个01数量可以对应背包问题的重量
    不过此时重量就有两个判定标准，要同时满足才能更新最大的价值
    所以带入到01背包，weight就是每一个元素中0，1对应的数量
    物品的value就是元素的个数，每个元素都是1
    '''
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        rows, cols = m+1, n+1
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in strs: # 先遍历物品
            zero_num = i.count('0')
            one_num = i.count('1')
            for j in range(m, zero_num - 1, -1): # 0
                for k in range(n, one_num - 1, -1): # 1
                    # 虽然是二维数组，但是两个维度都记录着两个重量，相当于二维滚动数组，所以要如同一维滚动数组一样，从后向前遍历
                    dp[j][k] = max(dp[j][k], dp[j - zero_num][k - one_num] + 1)
                    # 每一个元素的价值是1，输出最大子集就是求最大价值
        return dp[-1][-1]