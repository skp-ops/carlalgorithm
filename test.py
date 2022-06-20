'''

涉及到的题目
LeetCode 20

'''
def findPairs(nums, k: int) -> int:
    nums.sort()
    j, i = 0, 0
    count = 0
    while j < len(nums):
        while i < j:
            if nums[j] - nums[i] == k:
                while i < len(nums)-1 and nums[i] == nums[i + 1]:
                    i += 1
                    j = i + 1
                count += 1
                i += 1
            elif nums[j] - nums[i] > k:
                i += 1
            else:
                break
        j += 1
    return count
a = findPairs([1,1,1,1,1],0)
print(a)
