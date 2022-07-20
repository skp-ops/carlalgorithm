'''

涉及到的题目
leetcode 312

'''
'''
leetcode 312
312. 戳气球
有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。 
这里的 i - 1 和 i + 1 代表和 i 相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。
求所能获得硬币的最大数量。

示例 1：
输入：nums = [3,1,5,8]
输出：167
解释：
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

示例 2：
输入：nums = [1,5]
输出：10
'''
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        '''
        气球 3 1 5 8
        实际上的气球 【1】 3 1 5 8 【1】 # 左右两个1硬币的气球只算做边界奖励，无法戳破
    [
        0  1  2  3   4    5
     0 [0, 0, 3, 30, 159, 167],
     1 [0, 0, 0, 15, 135, 159],
     2 [0, 0, 0, 0,  40,  48],
     3 [0, 0, 0, 0,  0,   40],
     4 [0, 0, 0, 0,  0,   0],
     5 [0, 0, 0, 0,  0,   0]
     ]

    dp[i][j]定义为在i,j这个开区间内能够获得的最大硬币数，开区间的意义在于在边界时不能戳破【1】这个气球
    如何获得最大硬币数，我们要考虑在这个区间戳破的最后一个气球，
    例如在【1】3158【1】开区间中最后戳破的气球可以选择3158,记为第k个气球
    情况就是    【1】..3..【1】、【1】..1..【1】、【1】..5..【1】、【1】..8..【1】
    我们戳破气球可以获得的钱是 coins = nums[i]*nums[k]*nums[j]
    总共获得的钱就是dp[i][k]+coins+dp[k][j],因为我们戳的是最后存在的一个气球，

    （因为 k 是最后一个被戳爆的，所以 (i,j) 区间中 k 两边的东西必然是先各自被戳爆了的，
    所以你把 (i,k) 开区间所有气球戳爆，然后把戳爆这些气球的所有金币都收入囊中，金币数量记录在 dp[i][k]
    同理，(k,j) 开区间你也已经都戳爆了，钱也拿了，记录在 dp[k][j]
    所以你把这些之前已经拿到的钱 dp[i][k]+dp[k][j] 收着，
    再加上新赚的钱 val[i]*val[k]*val[j] 不就得到你现在戳爆气球 k 一共手上能拿多少钱了吗）

        所以两边其他的气球戳破时获得的最大硬币已经存储在dp数组中了
        至此我们需要先算出区间长度为3时获得的最大硬币数，然后再慢慢拓展到区间长度为4，再....到区间长度为len(nums)+1（即增加了左右两个边界）
    同时由于我们的最后一个气球k可以选择3、1、5、8
    所以我们还需要再用一个for循环来遍历这4种情况，最后选择一个获得硬币最多的情况
        '''
        nums = [1] + nums + [1]
        dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        for l in range(2, len(nums)): # 区间长度从3开始【1】x【1】，慢慢加到总长
            for i in range(0, len(nums)-l): # 保证index~index+l这个滑动窗口始终在有效范围内
                for k in range(i+1, i+l): # 枚举i到i+l这个开区间内所有的元素，算出最大硬币数
                    total = dp[i][k] + dp[k][i+l] + nums[i]*nums[k]*nums[i+l]
                    dp[i][i+l] = max(dp[i][i+l], total)
        # print(dp)
        return dp[0][-1]