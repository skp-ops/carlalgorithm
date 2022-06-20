'''

涉及到的题目
LeetCode 1、15、18

'''

'''
leetcode 1
给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]

示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]

https://leetcode.cn/problems/two-sum

'''
# 该解法巧妙的点在于，建立了一个哈希表，只用来存储枚举过的数（其值和其在nums中的坐标），这样子在利用target与枚举的value作差之后，得到的结果
# 只需要跟哈希表中的元素进行比对，不需要遍历整个nums，如果哈希表中存在，则返回坐标值，如果不存在，则将枚举的值存进哈希表中。
# 这样每次查询target-value的时候,遍历的数量大大减少,效率更高
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = dict() # 利用字典创建一个带有key 和value的哈希表，其中record的index存储nums中的值，value存储对应的nums坐标
        for index, value in enumerate(nums): # 对nums进行枚举
            if target-value in record: # 当字典中的key含有target与value的差值，说明在nums中能找到两个数的和等于目标数
                return[index, record[target-value]] # 那么就返回当前枚举数的坐标，以及他们差值对应的坐标，而这个坐标是用字典的值保存的
            else:
                record[value] = index # 假如两者的差值不存在于字典中，则将该枚举的数字存在字典中，以供之后查找

'''
leetcode 15
给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。


示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]

示例 2：
输入：nums = []
输出：[]

示例 3：
输入：nums = [0]
输出：[]

https://leetcode.cn/problems/3sum

'''
# 双指针法可以有效降低时间复杂度。因为需要选出三个元素，所以我们固定一个，滑动另外两个。
# 首先判断数组长度是否大于3，且排序完之后最小的值是否大于0. 这样可以排除一些不符合的情况
# 然后用一个for循环，遍历排序完的数组，假设有重复的数字例如，[-3,-3,-3,-2.......],
#   则for遍历完第一个-3之后，剩下的几个-3直接跳过，这样可以排除一些重复的情况
# 左右指针一个位置在i+1,另外一个在len(nums)-1. 计算出三个数的和，记为s，当左边指针小于右边指针时
#   假如s>0，说明右边的数太大了，右边向左移动一位
#   假如s<0，说明左边的数太小了，左边向右移动一位
#   假如s=0，记录下来当前的值，当做一个解。同时要判断是否会有重复解，例如，["-8",....."2",2,2,3......5,6,6,6,6,6,"6"..]
#       此时要判断左指针的右边元素是否相等，相等则左指针右移。判断右指针左边的元素是否相等，相等则右指针左移
#       当没有重复解的时候，记录完解之后，左指针右移，右指针左移，开始寻找新的解

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if len(nums) < 3 or nums[0] > 0: # 排除一些不符合的情况
            return []

        record = []
        for i in range(len(nums)):
            if i >= 1 and nums[i] == nums[i - 1]: continue # 假设有重复的数字例如，[-3,-3,-3,-2.......],
                                                            # 则for遍历完第一个-3之后，剩下的几个-3直接跳过，这样可以排除一些重复的情况
            left, right = i + 1, len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                elif s == 0:
                    record.append([nums[i], nums[left], nums[right]]) # 记录符合情况的解
                    while left < len(nums) - 2 and nums[left] == nums[left + 1]: left += 1 # 判断左指针的右边元素是否相等，相等则左指针右移
                    while right < len(nums) - 2 and nums[right] == nums[right - 1]: right -= 1 # 判断右指针左边的元素是否相等，相等则右指针左移
                    left += 1
                    right -= 1
        return record

'''
leetcode 18
给你一个由 n 个整数组成的数组nums ，和一个目标值 target 。
请你找出并返回满足下述全部条件且不重复的四元组[nums[a], nums[b], nums[c], nums[d]]
（若两个四元组元素一一对应，则认为两个四元组重复）：

0 <= a, b, c, d< n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。

示例 1：
输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

示例 2：
输入：nums = [2,2,2,2,2], target = 8
输出：[[2,2,2,2]]

https://leetcode.cn/problems/4sum

'''
# 四数之和类似于三数之和，用两个for循环即可。剪枝操作略有不同，因为四个数相加等于target，所以当nums[0]>0返回这个判断就不需要了
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        lens = len(nums)
        if lens< 4 :
            return []
        record = []
        for i in range(lens-3):
            if i > 1 and nums[i] == nums[i-1] : continue
            for j in range(i+1,lens-2):
                if j > i+1 and nums[j] == nums[j-1]: continue
                left,right = j+1, lens-1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]

                    if s < target:
                        left += 1
                    elif s > target:
                        right -= 1
                    elif s == target:
                        if [nums[i],nums[j],nums[left],nums[right]] not in record:
                            record.append([nums[i],nums[j],nums[left],nums[right]])
                        while left != right and nums[left] == nums[left+1]: left += 1
                        while right != right and nums[right] == nums[right-1]: right -= 1
                        left += 1
                        right -=1
        return record