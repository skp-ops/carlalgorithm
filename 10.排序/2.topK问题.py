'''

涉及到的题目
leetcode 215、414、973

'''
'''
leetcode 215
215. 数组中的第K个最大元素
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:
输入: [3,2,1,5,6,4], k = 2
输出: 5

示例 2:
输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4
'''

'''topK基于快排的模板'''
###########################################################
def partition(self, nums, left, right) -> int:  # Partition函数
    pivot = nums[left]  # 初始化一个待比较的数据
    i, j = left, right
    while i < j:
        # 从右向左遍历，将小于pivot的数据全部放到左边
        while i < j and nums[j] >= pivot:  # 从后往前查找，直到找到一个比pivot更小的数
            j -= 1
        nums[i] = nums[j]  # 将小于pivot的数据移动到i这个位置
        while i < j and nums[i] <= pivot:  # 从前往后找，直到找到一个比pivot更大的数
            i += 1
        nums[j] = nums[i]  # 将大于pivot的数据移动到j这个位置
    # 跳出循环此时i=j，将pivot重新添加进nums
    nums[i] = pivot
    return i  # 返回这个位置坐标


def quicksort(self, nums, left, right) -> None:  # 快排算法
    # 获取待比较数据的坐标，将nums分割成大数据和小数据，分治继续排
    if left < right:
        index = self.partition(nums, 0, len(nums) - 1)
        self.partition(nums, 0, index - 1)
        self.partition(nums, index + 1, len(nums) - 1)


def K_split(self, nums, k, left, right) -> None:  # 快速选择算法
    '''快速选择位置K，使得K左边都是比这个位置更小的数，K右边都是比这个位置更大的数'''
    if left < right:
        index = self.partition(nums, left, right)
        if index == k:
            return
        elif index < k:  # K处于index+1和right之间
            self.K_split(nums, k, index + 1, right)
        elif index > k:  # K处于left和index-1之间
            self.K_split(nums, k, left, index - 1)

# 获得前K小的数
def topk_small_list(self, nums, k):
    self.K_split(nums, k, 0, len(nums)-1)
    return nums[:k]

# 获得第K小的数
def topk_small_number(self, nums, k):
    self.K_split(nums, k-1, 0, len(nums)-1) # index为0表示第1小，所以index为k-1表示第k小
    return nums[k]

# 获得前K大的数：
def topk_large_list(self, nums, k):
    self.K_split(nums, len(nums)-k, 0, len(nums)-1)
    return nums[len(nums)-k:]

# 获得第K大的数：
def topk_large_number(self, nums, k):
    self.K_split(nums, len(nums) - k, 0, len(nums) - 1)
    return nums[len(nums) - k]

# 只排序前k个小的数：
def topk_sort_left(self, nums, k):
    self.K_split(nums, k, 0, len(nums)-1)
    small_part = nums[:k]
    large_part = nums[k:]
    self.quicksort(small_part, 0, len(small_part)-1)
    return small_part + large_part

# 只排序后k个大的数：
def topk_sort_left(self, nums, k):
    self.K_split(nums, len(nums)-k, 0, len(nums))
    small_part = nums[: len(nums)-k]
    large_part = nums[len(nums)-k:]
    self.quicksort(large_part, 0, len(large_part)-1)
    return small_part + large_part

###########################################################



class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.K_split(nums, len(nums) - k, 0, len(nums) - 1)
        return nums[len(nums) - k]

    def partition(self, nums, left, right) -> int:  # Partition函数
        pivot = nums[left]  # 初始化一个待比较的数据
        i, j = left, right
        while i < j:
            # 从右向左遍历，将小于pivot的数据全部放到左边
            while i < j and nums[j] >= pivot:  # 从后往前查找，直到找到一个比pivot更小的数
                j -= 1
            nums[i] = nums[j]  # 将小于pivot的数据移动到i这个位置
            while i < j and nums[i] <= pivot:  # 从前往后找，直到找到一个比pivot更大的数
                i += 1
            nums[j] = nums[i]  # 将大于pivot的数据移动到j这个位置
        # 跳出循环此时i=j，将pivot重新添加进nums
        nums[i] = pivot
        return i  # 返回这个位置坐标

    def K_split(self, nums, k, left, right) -> None:  # 快速选择算法
        '''快速选择位置K，使得K左边都是比这个位置更小的数，K右边都是比这个位置更大的数'''
        if left < right:
            index = self.partition(nums, left, right)
            if index == k:
                return
            elif index < k:  # K处于index+1和right之间
                self.K_split(nums, k, index + 1, right)
            elif index > k:  # K处于left和index-1之间
                self.K_split(nums, k, left, index - 1)

'''
leetcode 414
414. 第三大的数
给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。

示例 1：
输入：[3, 2, 1]
输出：1
解释：第三大的数是 1 。

示例 2：
输入：[1, 2]
输出：2
解释：第三大的数不存在, 所以返回最大的数 2 。

示例 3：
输入：[2, 2, 3, 1]
输出：1
解释：注意，要求返回第三大的数，是指在所有不同数字中排第三大的数。
此例中存在两个值为 2 的数，它们都排第二。在所有不同数字中排第三大的数为 1 。
'''

# 解法一
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) <= 2: return max(nums)
        self.K_split(nums, len(nums) - 3, 0, len(nums) - 1)
        return nums[len(nums) - 3]

    def partition(self, nums, left, right) -> int:  # Partition函数
        pivot = nums[left]
        i, j = left, right
        while i < j:
            while i < j and nums[j] >= pivot:
                j -= 1
            nums[i] = nums[j]
            while i < j and nums[i] <= pivot:
                i += 1
            nums[j] = nums[i]
        nums[i] = pivot
        return i

    def K_split(self, nums, k, left, right) -> None:  # 快速选择算法
        if left < right:
            index = self.partition(nums, left, right)
            if index == k:
                return
            elif index < k:
                self.K_split(nums, k, index + 1, right)
            elif index > k:
                self.K_split(nums, k, left, index - 1)

# 解法二，有序集合
'''我们可以遍历数组，同时用一个有序集合来维护数组中前三大的数。
具体做法是每遍历一个数，就将其插入有序集合，若有序集合的大小超过 33，就删除集合中的最小元素。
这样可以保证有序集合的大小至多为 33，且遍历结束后，若有序集合的大小为 33，其最小值就是数组中第三大的数；
若有序集合的大小不足 33，那么就返回有序集合中的最大值。'''
from sortedcontainers import SortedList
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = SortedList()
        for num in nums:
            if num not in s:
                s.add(num)
                if len(s) > 3:
                    s.pop(0)
        return s[0] if len(s) == 3 else s[-1]

'''
leetcode 973
973. 最接近原点的 K 个点
给定一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点，并且是一个整数 k ，返回离原点 (0,0) 最近的 k 个点。
这里，平面上两点之间的距离是 欧几里德距离（ √(x1 - x2)2 + (y1 - y2)2 ）。
你可以按 任何顺序 返回答案。除了点坐标的顺序之外，答案 确保 是 唯一 的。

示例 1：
输入：points = [[1,3],[-2,2]], k = 1
输出：[[-2,2]]
解释： 
(1, 3) 和原点之间的距离为 sqrt(10)，
(-2, 2) 和原点之间的距离为 sqrt(8)，
由于 sqrt(8) < sqrt(10)，(-2, 2) 离原点更近。
我们只需要距离原点最近的 K = 1 个点，所以答案就是 [[-2,2]]。

示例 2：
输入：points = [[3,3],[5,-1],[-2,4]], k = 2
输出：[[3,3],[-2,4]]
（答案 [[-2,4],[3,3]] 也会被接受。）
'''
# 排序
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key = lambda x: x[0]**2 + x[1]**2)
        return points[:k]

# 快速选择(超时)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.K_split(points, k, 0, len(points)-1)
        return points[:k]
    def partition(self, nums, left, right) -> int:
        pivot = nums[left]
        i, j = left, right
        distance = pivot[0]**2 + pivot[1]**2
        while i < j:
            d_i = nums[i][0]**2 + nums[i][1]**2
            d_j = nums[j][0]**2 + nums[j][1]**2
            while i < j and d_j >= distance:
                j -= 1
                d_j = nums[j][0]**2 + nums[j][1]**2
            nums[i] = nums[j]
            while i < j and d_i <= distance:
                i += 1
                d_i = nums[i][0]**2 + nums[i][1]**2
            nums[j] = nums[i]
        nums[i] = pivot
        return i
    def K_split(self, nums, k, left, right) -> None:
        if left < right:
            index = self.partition(nums, left, right)
            if index == k:
                return
            elif index < k:
                self.K_split(nums, k, index + 1, right)
            elif index > k:
                self.K_split(nums, k, left, index - 1)