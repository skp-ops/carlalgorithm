'''

涉及到的题目
leetcode 494

'''
'''
leetcode 494
494. 目标和
给你一个整数数组 nums 和一个整数 target 。
向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。

示例 1：
输入：nums = [1,1,1,1,1], target = 3
输出：5
解释：一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

示例 2：
输入：nums = [1], target = 1
输出：1
'''


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # arr_a - arr_b = target
        # arr_a + arr_b = sum
        # arr_a = (sum+target)/2
        # 本题变成装满背包有几种方法，排列组合问题
        # dp[0]=1表示现在背包承重为0，只有一种方式将它填满就是什么都不装
        # dp[j]表示背包承重为j，有几种填充方法，而这个j对应于本题就是(sum+target)/2
        # 那么递推公式为 dp[j] = dp'[j] + dp[j-nums[i]]
        #   如何理解，假设我们现在遍历物品到i，可以选择的物品个数就是i个
        #   我们有两个方案，第一种方案是不装物品i，这样装满j的情况根物品数为i-1的情况一样 就是dp[j](i-1的情况)
        #               第二种方案就是装物品i，那么此时剩下的空间就是 j-nums[i]，
        #               那我们就要去寻找在物品只剩下i-1个的情况下，装满承重为j-nums[i]背包的个数
        #               两种方案相加就是在i情况下的组合数

        target_value = (sum(nums) + target) / 2
        if abs(target) > sum(nums) or target_value != int(target_value): return 0
        target_value = int(target_value)
        dp = [1] + [0] * target_value  # 初始化背包重量为0的时候情况为1，其他初始化都为0
        for i in range(len(nums)):
            for j in range(target_value, nums[i] - 1, -1):
                dp[j] = dp[j] + dp[j - nums[i]]
        return dp[-1]