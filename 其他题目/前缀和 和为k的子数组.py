'''

涉及到的题目
leetcode 560

'''
'''
leetcode 560
560. 和为 K 的子数组
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的连续子数组的个数 。

示例 1：
输入：nums = [1,1,1], k = 2
输出：2

示例 2：
输入：nums = [1,2,3], k = 3
输出：2
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''   3, 4, 7, 2, -3, 1, 4, 2
        前缀和3, 7, 14,16,13, 14,18,20
        pre[i]=nums[0]+nums[1]+...+nums[i]
        pre[1]=7:  pre[1]-0=sum(nums[:2])==target
        pre[2]=14: pre[2]-pre[1]=sum(nums[2:3])==target
        记录前缀和出现的次数，在之后的遍历中如果出现pre[i]-k存在于前缀和的哈希表中，
        那么就可以凑成一个连续子串，答案相应添加出现的次数'''
        pre_sum, res = 0, 0
        hash_dict = {0:1} # 初始化0出现了1次
        for i in nums:
            pre_sum += i
            if pre_sum - k in hash_dict:
                res += hash_dict[pre_sum - k]
            hash_dict[pre_sum] = hash_dict.setdefault(pre_sum, 0) + 1
        return res
