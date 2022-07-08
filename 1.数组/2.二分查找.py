'''

涉及到的题目
LeetCode 704、35、34、69、367

'''

'''
leetcode 704
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，
写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
https://leetcode-cn.com/problems/binary-search/
示例1：
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4

示例2：
输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
'''

'''
注意，一般题目中出现
    有序数组（升序、降序） 无重复元素
等条件的时候可以考虑二分法。
如何理解算法：
    在一开始定义左和右分别为0和n,n为数组的元素个数，middle是左和右的平均数，这样子可以通过arr[middle]来获取数组中的元素值
    获取完中间值之后再跟目标值作对比，然后将middle的值赋值给左或右（具体看数组升序还是降序），然后更新middle的值继续查找
    直到找到对应数，返回其坐标。
'''

def bisearch1 ( nums: list[int], target: int) -> int:
    '''
    第一种写法，二分法区间左闭右闭[left,right]，假设数组升序，例如[1,2,3,4,5,6]
    :param nums:给定的数组
    :param target:目标值
    :return:目标值下标

    一般是在while循环下面第一步开始计算mid值
    一般 mid = left + (right-left)//2 (为了防止left+right数据过大)
    也可以用位运算表示 mid = (left+right) >> 1
    '''

    left, right = 0, len(nums) - 1  # 这里减1的原因是右边闭区间，数组里元素的个数和其下标始终相差1（从0开始计数）

    while left <= right:
        middle = (left + right) // 2 # 整除2，可以防止左加右为奇数时出现错误
        if nums[middle] < target:
            left = middle + 1  # 更新左区间
        elif nums[middle] > target:
            right = middle - 1  # 更新右区间
        else:
            return middle
    return -1

print(bisearch1(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target=7))
# 输出6

def bisearch2 (nums: list[int], target: int) -> int:
    '''
    第二种写法，二分法区间左闭右开[left,right)，假设数组升序， 例如[1,2,3,4,5,6]
    :param nums:给定的数组
    :param target:目标值
    :return:目标值下标
    '''
    left, right = 0, len(nums) # 这里不减1是因为开区间，取不到len(nums)这个数

    while left < right:  # 这里不能取等号，可以会导致左右相等的死循环
        middle = (left + right -1)//2
        if nums[middle] < target:
            left = middle + 1
        elif nums[middle] > target:
            right = middle
        else:
            return middle
    return -1

print (bisearch2(nums= [3,5,6,78,567,1112,10898],target= 100))
# 输出-1


'''
leetcode 35 
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
请必须使用时间复杂度为O(logn)的算法
https://leetcode-cn.com/problems/search-insert-position/
示例1：
输入: nums = [1,3,5,6], target = 5
输出: 2

示例2：
输入: nums = [1,3,5,6], target = 2
输出: 1

示例3：
输入: nums = [1,3,5,6], target = 7
输出: 4
'''

def searchInsert(nums: list [int] , target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] < target:
            left = middle + 1
        elif nums[middle] > target:
            right = middle - 1
        else:
            return middle
    # while 循环结尾return时可以直接return 'right + 1', 因为当区间最后缩小到最小还是没找到target时，right+1就是它应该插入的位置
    return right + 1

'''
leetcode 34
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

示例2：
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]

示例 3：
输入：nums = [], target = 0
输出：[-1,-1]

https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums: return [-1,-1]
        else:
            count = nums.count(target)
            index = nums.index(target)
        return [index, index + count-1]
# 时间复杂度O(n)

# 第二种解法，用二分法不断逼近target的左右边界，分别将左右边界求出来，然后区间自然而然就出来了，时间复杂度O(logn)
#     分三种情况  1, target不在数组区间内，[3,4,5]，target=2，输出[-1,-1]
#               2, target在数组区间内，但是数组里没这个target，[4,6,8], target= 7, 输出[-1,-1]
#               3, traget在数组区间内，且数组里有target, [4,6,7], target = 7, 输出[2,2]
class Solution:
    def searchRange2(nums: list[int], target: int) -> list[int]:
        def getright(nums: list[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            rightborder = -2
            while left <= right:  # 无限趋近target的右边界，直到left等于target右边界的后一位，此时确定了右边界的值
                middle = left + (right - left) // 2
                if nums[middle] > target:
                    right = middle - 1
                else:
                    '''这里的判断条件就发生了变化，只要mid值小于等于target，就向右扩大范围'''
                    left = middle + 1
                    rightborder = left

            return rightborder

        def getleft(nums: list[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            leftborder = -2
            while left <= right:  # 无限趋近target的左边界，直到right等于target左边界的前一位，此时确定了左边界的值
                middle = left + (right - left) // 2
                if nums[middle] >= target:
                    '''同理，mid值等于target也一直向左扩大范围'''
                    right = middle - 1
                    leftborder = right
                else:
                    left = middle + 1
            return leftborder

        rightborder = getright(nums, target)
        leftborder = getleft(nums, target)
        if leftborder == -2 or rightborder == -2: return [-1, -1]
        if rightborder - leftborder > 1: return [leftborder + 1, rightborder - 1]
        return [-1, - 1]

# 第三种解法，找到其中一个target后左右移动指针
#     当target不存在于数组中返回[-1,-1]
#     当target存在的时候，返回middle,然后将middle分别加一，减一，去寻找其左右边界

def searchRange3(nums: list[int],target:int) -> list[int]:
    def CheckTarget (nums:list[int],target:int):
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = left + (right-left) // 2
            if nums[middle]>target:
                right = middle - 1
            elif nums[middle]<target:
                left = middle + 1
            else:
                return middle
        return -1

    index = CheckTarget(nums,target)
    left, right = index, index
    while left > 1 and nums[left-1] == target: left -= 1
    while right < len(nums)-1 and nums[right+1] == target: right += 1
    return [left,right]

nums=[1,2,2,2,2,2,2,3,4,5,6]
target = 2
a = searchRange3(nums,target)
print(a)  #[1, 6]

nums=[1,5,6]
target = 4
a = searchRange3(nums,target)
print(a)  #[-1, -1]

nums=[1]
target = 1
a = searchRange3(nums,target)
print(a)  #[0, 0]

'''
leetcode 69
给你一个非负整数 x ，计算并返回x的算术平方根。
由于返回类型是整数，结果只保留整数部分，小数部分将被舍去 。
注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
https://leetcode-cn.com/problems/sqrtx

示例1：
输入：x = 4
输出：2

示例2:
输入：x = 8
输出：2
解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
'''
# 思路:只考虑整数部分，相当于给定的x一定限制在n^2 与 (n+1)^2内，且n属于[0,x/2+1],用二分法找到这个整数n就行
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x/2 + 1
        while left <= right:
            m = left + (right-left) // 2
            if m * m < x:
                left = m + 1
            elif m * m > x:
                right = m - 1
            elif m * m == x:
                return int(m)
        return int(right)

'''
leetcode 367
给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。
进阶：不要 使用任何内置的库函数，如 sqrt 。

示例 1：
输入：num = 16
输出：true

示例 2：
输入：num = 14
输出：false

https://leetcode-cn.com/problems/valid-perfect-square
'''
# 思路：只需要用二分法，在区间(0,num/2+1)中找，是否存在一个n使得n^2==num，
# 如果存在就返回True，二分到最后发现不存在就返回False
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num / 2 + 1
        while left <= right:
            middle = left + (right-left) // 2
            if middle * middle < num:
                left = middle + 1
            elif middle * middle > num:
                right = middle - 1
            elif middle * middle == num:
                return True
        return False