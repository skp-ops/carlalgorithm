'''

'''
'''
leetcode 239
给你一个整数数组 nums，有一个大小为k的滑动窗口从数组的最左侧移动到数组的最右侧。
你只可以看到在滑动窗口内的 k个数字。滑动窗口每次只向右移动一位。
返回 滑动窗口中的最大值 。

示例 1：
输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 
示例 2：
输入：nums = [1], k = 1
输出：[1]

https://leetcode.cn/problems/sliding-window-maximum

'''
# 这道题很明显要用到队列，deque，但是难就难在如何控制好时间，不要超时。
# 下面给的解法就是创建一个队列，这个队列只存储数组的下标。遍历整个数组，假设队列是空的，则append当前坐标进入队列，然后接着遍历，
#   当遍历的这个数大于队列最右边的数时，直接pop掉，直到小于队列最右边的数，将该下标append到队列里。
#   这时，队列就是一个nums值从大到小排序的下标队列。（stack第一个值对应的nums最大）
# 例如 nums = [1000,500,100,10,200] stack = []
# 第一次 nums[i] = 1000, stack = [0]
# 第二次 nums[i] = 500, stack = [0,1]
# 第三次 nums[i] = 100, stack = [0,1,2]
# 第四次 nums[i] = 10, stack = [0,1,2,3]
# 第五次 nums[i] = 200, stack = [0,1,4] (直接将2,3,剔除掉)
# 同时在遍历nums的时候要进行两个判断。
#   第一个：当stack[0]等于i-k时，说明最大值超出滑动窗口的位置，需要popleft 即 3,[2,0,4],2,5,6。原来3是最大值，原来的窗口是[3,2,0]
#             stack[0]=0,当i指向4的时候，i=3，k=3，此时stack[0]=3-3=0，3需要被剔除
#   第二个：当i的值大于等于k-1时，说明此时窗口大小已经达到目标的k，每次滑动窗口向前移动一位时，res都要append一个最大值进去
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = deque()
        res = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                # 让stack里坐标位置呈从大到小排序，即nums[stack[0]]>nums[stack[1]]>...>nums[stack[i]]
                stack.pop() # 同时剔除掉小于nums[i]的所有值
            stack.append(i) # 让stack的第一个位置，始终是滑动窗口中最大值的坐标
            if stack[0] == i - k: # 最大值将离开滑动窗口时，popleft
                stack.popleft()
            if stack and i >= k-1: # 当滑动窗口大于k的时候，开始向res里面append最大值，最大值就是stack第一个元素坐标对应的nums里的值
                res.append(nums[stack[0]])
        return res

# 超时解法 52/61通过案例
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def getmax(a):
            c = list(a.copy())
            c.sort()
            return c[-1]

        stack = deque()
        res = []

        for i in range(k): # 创建初始k长度的窗口
            stack.append(nums[i])
        max_element = getmax(stack)
        res.append(max_element)

        for i in range(k, len(nums)):
            stack.append(nums[i])
            stack.popleft() # 窗口维护

            if nums[i] < max_element and max_element in stack:  # 最大值还在框内，nums[i]小于最大值，直接append最大值
                pass
            elif nums[i] < max_element and max_element not in stack:  # 最大值不在框内，nums[i]小于最大值，重新选出最大值并append
                max_element = getmax(stack)
            elif nums[i] >= max_element: # 如果nums[i]大于最大值，则更新max_element
                max_element = nums[i]

            res.append(max_element)

        return res