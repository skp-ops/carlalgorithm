'''

涉及到的题目
LeetCode 746

'''
'''
leetcode 746
746. 使用最小花费爬楼梯
给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。
你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。
请你计算并返回达到楼梯顶部的最低花费。

示例 1：
输入：cost = [10,15,20]
输出：15
解释：你将从下标为 1 的台阶开始。
- 支付 15 ，向上爬两个台阶，到达楼梯顶部。
总花费为 15 。

示例 2：
输入：cost = [1,100,1,1,1,100,1,1,100,1]
输出：6
解释：你将从下标为 0 的台阶开始。
- 支付 1 ，向上爬两个台阶，到达下标为 2 的台阶。
- 支付 1 ，向上爬两个台阶，到达下标为 4 的台阶。
- 支付 1 ，向上爬两个台阶，到达下标为 6 的台阶。
- 支付 1 ，向上爬一个台阶，到达下标为 7 的台阶。
- 支付 1 ，向上爬两个台阶，到达下标为 9 的台阶。
- 支付 1 ，向上爬一个台阶，到达楼梯顶部。
总花费为 6 。
'''
# 首先一开始准备上楼前不用花钱，同时爬到最顶层之后也不用交钱
# 所以这个数列只展示了中间需要交钱的部分阶梯
# 对于花费来说，你只要到达了第i层，那么要继续向上爬，就一定要交这一层的钱cost[i]
# 所以假设dp[i]表示的是上到第i层楼需要交最少的钱，那么dp[i]里肯定有一部分是cost[i]
# 那么dp[i]的公式就是 dp[i] = cost[i] + x
# 其中x就是爬到第i-1楼和爬到第i-2楼花费最少的情况，这样才能保证每次都花最少的钱
# 所以x = min(dp[i-1],dp[i-2])
# 确定了递推公式 dp[i] = cost[i] + min(dp[i-1],dp[i-2])
# 再确定初始情况，初始第零层和第一层花费分别是cost[0]和cost[1]
# 所以就能算出爬到最后一层花费最少的情况

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2: return min(cost)
        cost.append(0) # 爬到最后一层不需要钱，因为已经到顶
        dp = [0] * (len(cost))
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,len(cost)):
            dp[i] = cost[i] + min(dp[i-1] , dp[i-2])

        return dp[i]

# 节省空间的做法
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2: return min(cost)
        cost.append(0)
        a = cost[0]
        b = cost[1]
        for i in range(2, len(cost)):
            temp = cost[i] + min(a, b)
            a, b = b, temp
        return b