'''

涉及到的题目
LeetCode 556

'''
'''
leetcode 556
556. 下一个更大元素 III
给你一个正整数 n ，请你找出符合条件的最小整数，其由重新排列 n 中存在的每位数字组成，并且其值大于 n 。如果不存在这样的正整数，则返回 -1 。
注意 ，返回的整数应当是一个 32 位整数 ，如果存在满足题意的答案，但不是 32 位整数 ，同样返回 -1 。

示例 1：
输入：n = 12
输出：21

示例 2：
输入：n = 21
输出：-1
'''
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        '''因为要求出符合条件的最小整数，所以位数靠前的数尽可能不改变
        尽量在末尾位数增大一点点，即可保证得到的数大于n但又是最小的整数
        先分析如果该数本身递增54321，无法改变，从后往前遍历可以看出是个递增数组
        所以直接返回-1, 如果该数是1236541就可以改变，尽可能小，那么1，2尽量不变
        从后向前遍历，发现1->4->5->6->3有个陡降，那就挑出刚好大于陡降数的一个数与之替换
        即3和4替换，变成1246531，这样已经大于原本的数了，进一步让数变小，就是4之后的数最小
        那么就将6531升序排列，1356，最后答案就是1241356'''
        nums = list(str(n))
        i = j = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0: return -1
        index_1 = i-1
        while j > index_1 and nums[j] <= nums[index_1]:
            j -= 1
        nums[index_1], nums[j] = nums[j], nums[index_1]
        nums[index_1+1:] = sorted(nums[index_1+1:])
        return int(''.join(nums)) if int(''.join(nums)) < 2**31 else -1