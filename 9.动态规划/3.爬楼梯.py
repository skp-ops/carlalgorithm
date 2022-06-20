'''

涉及到的题目
LeetCode 70

'''
'''
70. 爬楼梯
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

示例 1:
输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶

示例 2：
输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶
'''
# 这道题需要思考的地方就是不太清楚具体的规律是什么
# 那就举特殊例子看看
# 假如爬1层,一种方法
# 假如爬2层,一种方法
# 假如爬3层,有两种情况,我先爬1层,再一口气上两阶
#                   我先爬2层,再一口气上一阶
# 此时就可以发现，我爬1层有x种情况，爬2层有y种情况，那我爬3层，就是x+y种情况
# 这个时候我们就知道了dp[i]代表着爬i层的情况个数
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1: return n
        memo = [0]*(n+1)
        memo[1] = 1
        memo[2] = 2
        for i in range(3,n+1):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[n]


# 降低空间复杂度，只用两个变量
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1: return n
        a = 0 # dp[0]
        b = 1 # dp[1]
        total = 0
        for i in range(1,n+1):
            total = a + b # dp[i] = do[i-1] + do[i-2]
            a, b = b, total
        return total

'''
假设扩展开：
    爬n阶楼梯，每次可以爬1~m个台阶，有多少种不同的爬法
    那么递推公式就是
    举个例子 n = 6 , m = 3
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    dp[4] = dp[3] + dp[2] + dp[1]
    dp[5] = dp[4] + dp[3] + dp[2]
    dp[6] = dp[5] + dp[4] + dp[3]
    所以推广到最后
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + ...... + dp[max(i-m),1] # 最小不能小于1
    用两个for循环实现
    let dp[0] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i >= j: # 包含dp[0]的情况
                dp[i] += dp[i-j]
'''