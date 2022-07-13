'''

涉及到的题目
leetcode 738

'''
'''
738. 单调递增的数字
当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。
给定一个整数 n ，返回 小于或等于 n 的最大数字，且数字呈 单调递增 。

示例 1:
输入: n = 10
输出: 9

示例 2:
输入: n = 1234
输出: 1234

示例 3:
输入: n = 332
输出: 299
'''
'''
局部最优：遇到strNum[i - 1] > strNum[i]的情况，让strNum[i - 1]--，然后strNum[i]给为9，可以保证这两位变成最大单调递增整数。
全局最优：得到小于等于N的最大单调递增的整数。
但这里局部最优推出全局最优，还需要其他条件，即遍历顺序，和标记从哪一位开始统一改成9。
'''
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if n < 10: return n
        nums = list(str(n))
        change_point = -1
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                change_point = nums.index(nums[i])
                break
        if change_point == -1:
            return int(''.join(nums))
        else:
            nums[change_point] = str(int(nums[change_point])-1)
            for j in range(change_point+1,len(nums)):
                nums[j] = '9'
            return int(''.join(nums))