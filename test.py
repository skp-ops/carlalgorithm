'''

涉及到的题目
LeetCode 20

'''

def rob( nums) -> int:
    if len(nums) <= 2: return max(nums)
    n = len(nums)
    dp = [0]*(n)
    dp[0] = nums[0]
    dp[1] = nums[1]
    for i in range(2, n):
        dp[i] = max(dp[i-1], nums[i]+dp[i-2])
    return dp
print(rob([2,1,1,2]))