'''

涉及到的题目
LeetCode 376

'''
'''
leetcode 376
如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为 摆动序列 。
第一个差（如果存在的话）可能是正数或负数。仅有一个元素或者含两个不等元素的序列也视作摆动序列。
例如，[1, 7, 4, 9, 2, 5] 是一个 摆动序列 ，因为差值 (6, -3, 5, -7, 3)是正负交替出现的。
相反，[1, 4, 7, 2, 5]和[1, 7, 4, 5, 5] 不是摆动序列，
第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。
子序列 可以通过从原始序列中删除一些（也可以不删除）元素来获得，剩下的元素保持其原始顺序。
给你一个整数数组 nums ，返回 nums 中作为 摆动序列 的 最长子序列的长度 。

示例 1：
输入：nums = [1,7,4,9,2,5]
输出：6
解释：整个序列均为摆动序列，各元素之间的差值为 (6, -3, 5, -7, 3) 。

示例 2：
输入：nums = [1,17,5,10,13,15,10,5,16,8]
输出：7
解释：这个序列包含几个长度为 7 摆动序列。
其中一个是 [1, 17, 10, 13, 10, 16, 8] ，各元素之间的差值为 (16, -7, 3, -3, 6, -8) 。

示例 3：
输入：nums = [1,2,3,4,5,6,7,8,9]
输出：2

https://leetcode.cn/problems/wiggle-subsequence

'''
'''
局部最优解：删除单调坡度上的节点（不包括单调坡度两端的节点）
全局最优解：整个序列有最多的局部峰值，从而获得最长的摆动序列
在实际操作中，其实不用删除元素，直接统计波峰或者波谷的个数，然后输出最大值就可以
'''
# 计算出相邻两个数的差，这样如果结果一正一负，则满足要求。
# 由于会出现爬坡和下坡两种情况，对应于差值，就会出现一直为正或者一直为负的情况，最后统计个数的时候排除掉一直为正或为负的情况
# 再重新计算就可以得到最后的结果
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(set(nums)) < 3: return len(set(nums)) # 加set的原因是[0,0]这种特殊情况 或者[1,1]
        cal = [] # 用于记录差值的数组
        need = True # 之后遍历差值数组的时候，如果结果为正并且需要的是True（正数）则count + 1，need变为False（负数）
        #                                 如果结果为负并且需要的是False（负数）则count + 1，need变为True（正数）
        count = 0 # 记录满足需求的个数
        slow, fast = 0, 1
        while fast < len(nums):
            cal.append(nums[fast] - nums[slow])
            slow += 1
            fast += 1

        for i in cal:
            # 找到cal数组里第一个不为0的数，如果为正，将need调整为True（意为此时需要一个正数）
            # 如果为负,将need调整为False（意为此时需要一个负数）
            if i > 0:
                need = True
            elif i < 0:
                need = False
            else:
                continue
            break

        for j in cal: # 开始遍历cal数组
            if j == 0:
                continue
            if j > 0 and need is True: # 当需要正数且j就是正数，计数器加一，需要变成负数
                count += 1
                need = False
            elif j < 0 and need is False: # 当需要负数且j就是负数，计数器加一，需要变成正数
                count += 1
                need = True
            else:
                continue
        return count + 1

# 跟解法一类似，在append计算结果的时候多一步判断，如果cal最后一个数字的正负号跟即将append的元素一样
# 那么说明有连续的正数或负数，就pop出去，然后再将结果append，这样cal数组就维护成了一正一负的情况，最后输出cal长度加一即可

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(set(nums)) < 3: return len(set(nums))
        cal = []
        need = True
        count = 0
        slow , fast = 0 , 1
        while fast < len(nums):
            if nums[fast] - nums[slow] > 0:
                if cal and cal[-1] == 1:
                    cal.pop()
                cal.append(1)
            elif nums[fast] - nums[slow] < 0:
                if cal and cal[-1] == -1:
                    cal.pop()
                cal.append(-1)
            slow += 1
            fast += 1
        return len(cal)+1

# 摆动序列出现波峰和波谷的次数之差一定等于1，所以当爬坡的时候只更新up的数量，不更新down的数量
#     如果遇到不断爬坡的情况，由于down的值不会变，up始终等于down+1
#     当遇到下坡的时候，更新down的值，down = up+1，遇到连续下坡，由于up的值不会更新，down始终为up+1不变
#     最后输出max（up，down）

class Solution:
    def wiggleMaxLength(self, nums):
        '''利用摆动序列，波峰和波谷的差值最多为1的特点'''
        up ,down = 1,1
        if len(nums)<2:return len(nums)
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                up = down+1
            if nums[i]<nums[i-1]:
                down = up+1
        return max(up,down)

# 算出差值之后，两两相乘，如果为负数说明异号，然后计数器加一，最后统计结果
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        pre = 0
        res = 1
        for i in range(len(nums)-1):
            post = nums[i+1] - nums[i] # 相邻两个数的差一定是一正一负才能是摆动序列，所以要算出pre和post
            if pre * post <= 0 and post !=0:
                '''
                post != 0说明此时没有进入平缓区
                pre*post<0说明一正一负，满足要求
                pre*post=0 只限于一开始pre=0的时候，也满足需求，这样res=2，刚好不用统计数组两端的情况
                    但是到了之后pre不会等于0，pre的值由post赋予，post只有在不等于0的情况下才有可能赋予pre
                '''
                res += 1
                pre = post
        return res