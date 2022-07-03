'''

涉及到的题目
leetcode 1035

'''
'''
leetcode 1035
1035. 不相交的线
在两条独立的水平线上按给定的顺序写下 nums1 和 nums2 中的整数。
现在，可以绘制一些连接两个数字 nums1[i] 和 nums2[j] 的直线，这些直线需要同时满足满足：
 nums1[i] == nums2[j]
且绘制的直线不与任何其他连线（非水平线）相交。
请注意，连线即使在端点也不能相交：每个数字只能属于一条连线。
以这种方法绘制线条，并返回可以绘制的最大连线数。

示例 1：
输入：nums1 = [1,4,2], nums2 = [1,2,4]
输出：2
解释：可以画出两条不交叉的线，如上图所示。 
但无法画出第三条不相交的直线，因为从 nums1[1]=4 到 nums2[2]=4 的直线将与从 nums1[2]=2 到 nums2[1]=2 的直线相交。

示例 2：
输入：nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
输出：3

示例 3：
输入：nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
输出：2
'''
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        '''同 求最长重复子序列一样的
            2 5 1 2 5
            0 0 0 0 0
    10  0   0 0 0 0 0
    5   0   0 1 1 1 1
    2   0   1 1 1 2 2
    1   0   1 1 2 2 2
    5   0   1 2 2 2 3
    2   0   1 2 2 3 3
        '''
        n1, n2 = len(nums1), len(nums2)
        dp = [[0 for _ in range(n1+1)]for _ in range(n2+1)]
        for i in range(1, n2+1):
            for j in range(1, n1+1):
                if nums1[j-1] == nums2[i-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
