'''

涉及到的题目
leetcode 718

'''
'''
leetcode 718
718. 最长重复子数组
给两个整数数组 nums1 和 nums2 ，返回 两个数组中 公共的 、长度最长的子数组的长度 。

示例 1：
输入：nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
输出：3
解释：长度最长的公共子数组是 [3,2,1] 。

示例 2：
输入：nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
输出：5
'''


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        '''动态规划
        题目中说了必须是连续的重复子数组，所以dp状态前后肯定严格相关
        我们假设dp[i][j]分别表示当两数组的坐标以i,j结尾时重复子数组的长度
        举个例子
            1 2 3 4 5
        1   1 0 0 0 0
        2   0 2 0 0 0
        3   0 0 3 0 0
        5   0 0 0 0 1
        6   0 0 0 0 0
        可以发现两个数组 [1,2,3,4,5] [1,2,3,5,6]重复子数组是[1,2,3]，等到了[4,5]和[5,6]的时候，最长重复子数组就变成了5
        所以从上面的关系可以看出，dp[i][j] = dp[i-1][j-1]+1（即dp[i][j]只能由dp[i-1][j-1]推导出来）
        对于初始化，我们只需要初始化第一排和第一列，将相同元素代表的value变成1就好
        '''
        n1, n2 = len(nums1), len(nums2)
        dp = [[0 for _ in range(n1)] for _ in range(n2)]
        for i in range(n1):
            if nums1[i] == nums2[0]:
                dp[0][i] = 1
        for j in range(n2):
            if nums2[j] == nums1[0]:
                dp[j][0] = 1

        for a in range(1, n1):
            for b in range(1, n2):
                if nums1[a] == nums2[b]:
                    dp[b][a] = dp[b - 1][a - 1] + 1
        return max([max(i) for i in dp])
