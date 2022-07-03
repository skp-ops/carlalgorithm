'''

涉及到的题目
leetcode 300

'''
'''
leetcode 300
300. 最长递增子序列
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

示例 1：
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

示例 2：
输入：nums = [0,1,0,3,2,3]
输出：4

示例 3：
输入：nums = [7,7,7,7,7,7,7]
输出：1

示例 4：
输入：nums = [4,10,4,3,8,9]
输出：3
'''

class Solution:
    '''动态规划'''
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n # dp[i]表示到当前位置i位置，最大的递增子序列长度，一开始只有一个数，所以长度为1
        # 通过 [4,10,4,3,8,9] 这个case可以知道，如果我们只是一味地计算后一项比前一项大总和加1，答案就会出错
        # 这个case正确答案是3 [3,8,9] 如果只是单纯累加计数，算出来是4，因为4->10加起来为2,3->9加起来为2，总和为4.就出问题了
        # 如何正确解决这个问题，就是每次i遍历一个新的数的时候，要求出他当前的最大递增子序列长度，需要再来一个循环，遍历i之前所有的数
        # 假设nums[i]>nums[j]，说明在j的基础上加上i可以递增，那么dp[i] = dp[j]+1，当然在j循环过程中始终要找最大值
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''二分法
        维护一个数组tails, tails代表的是，长度为i的最长递增子序列的最末尾的元素
        我们这个地方用一个贪心的思想，假设一个数组有一个最长的递增子数组，那么其每一个递增的元素应该尽可能小
        所以tails数组就记录了长度为i的递增子序列末尾最小的那个元素
        往后遍历，每次遇见了更大的一个新数，就append到tails里，说明此时最长递增子序列又增加了一个单位长度
        假如遍历的数小于当前tails[-1]，那么这个数可能是第x长递增子序列里最小的尾部元素，那我们就要用二分法找到这个x并替换掉tails
        可以利用反证法证明tails数组是一个严格递增的数组，二分查找即可降低时间复杂度
        拿[4,10,4,3,8,9]这个case举例，当number遍历到3之前，tails数组是[4,10]
        说明长度为1的递增子序列最小尾巴为4，长度为2的递增子序列最小尾巴为4
        当number为3时，tails更新为[3,10]
        当number为8时，tails更新为[3,8]，此时4.10 彻底被弃用，因为有更好的解 即 3.8
        当number为9时，tails更新为[3,8,9] 最终递增子序列不是tails本身，我们只关注tails的长度
        '''
        tails = []
        for number in nums:
            if not tails or number > tails[-1]:
                tails.append(number)
            else:
                left, right = 0, len(tails)-1
                change_index = right
                while left <= right:
                    mid = left + (right-left)//2
                    if tails[mid] >= number:
                        change_index = mid
                        right = mid -1
                    else:
                        left = mid + 1
                tails[change_index] = number
        print(tails)
        return len(tails)