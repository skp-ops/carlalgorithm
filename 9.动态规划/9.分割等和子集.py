'''

涉及到的题目
leetcode 416

'''
'''
leetcode 416
416. 分割等和子集
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

示例 1：
输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。

示例 2：
输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。
'''
# 这道题乍一看可以用回溯，来求出每一种情况对应子集的和为多少，但是这样时间复杂度过大
# 就需要用动态规划来优化时间
# 我们可以分析得到，我们的目标是求两个子集区间，使得每个子集元素和相等
# 就说明我们要算出总的sum再除以2，就是每个集合的总和
# 在一个空集合中，每次往里面添加一个元素i，剩余总和就是（sum/2 -nums[i]）
# 当我们什么时候恰好能将剩余减为0，就说明可以拆分成两个子集
# 我们可以把这个地方的sum/2当成背包的容量，我们需要找到一种情况使得背包恰好被装满
# 而这种情况又是我们需要的最终结果，对应到价值就是背包恰好装满的时候背包价值恰好最大
# 那么自然而然可以联想到，元素的重量就是元素的价值，都是nums[i]

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0: return False # 由于元素都是正整数，所以算出来sum的一半有小数，怎么样都无法实现拆分
        target_value = int(sum(nums)/2) # 我们目标的价值就是sum一半
        dp = [0]*(target_value+1) # 同时，dp数组的重量也是sum一半
        for i in range(len(nums)): # 先遍历物品
            for j in range(target_value, nums[i]-1, -1): # 再倒序遍历背包重量
                dp[j] = max(dp[j], nums[i] + dp[j-nums[i]])
        return dp[-1] == target_value # 最后求出来在背包重量刚刚好为target_value的时候，其价值是否也是target_value
    