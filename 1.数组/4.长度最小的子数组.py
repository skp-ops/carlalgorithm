'''

涉及到的题目
LeetCode 209、904、76

'''

'''
leetcode 209
给定一个含有n个正整数的数组和一个正整数 target 。
找出该数组中满足其和 ≥ target 的长度最小的 连续子数组[numsl, numsl+1, ..., numsr-1, numsr] ，
并返回其长度。如果不存在符合条件的子数组，返回 0 。

示例 1：
输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组[4,3]是该条件下的长度最小的子数组。

示例 2：
输入：target = 4, nums = [1,4,4]
输出：1

示例 3：
输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0

https://leetcode-cn.com/problems/minimum-size-subarray-sum

'''

# 暴力解法，直接一个一个尝试，判断最小子集个数是否为1，不为1就尝试2，一直尝试，直到满足，返回当前子集长度。但是时间复杂度太高
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        for i in range(len(nums)):
            left, right = 0, i
            while right < len(nums):
                a = 0
                for j in range(right- left + 1):
                    a += nums[left + j]
                if a >= target:
                    return right - left + 1
                else:
                    pass
                left += 1
                right += 1
        if right >= len(nums):
            return 0

# 解法二，滑动窗口 时间复杂度O(n)
# 将过程想象成动态的窗口滑动过程。一开始左右指针都在0，然后右指针向右移动一位，计算出当前窗口内元素之和做判断
#   判断1：元素之和小于目标target，右指针继续向右移动，并且继续相加，重复上面的判断
#   判断2：元素之和小于等于目标target，记录当前的result，然后左指针向右移动，查找有没有最小子集的情况
#           当左指针向右移动的时候，元素之和要剔除掉原先的最左边的元素，即sumup -= nums[left]，然后left +=1 实现左指针右移
#           重复上述判断流程，不断更新result，最终遍历结束
# 这里注意特例，当target过大，数组中所有元素相加都小于target时，result是没有值的，这个时候要提前将result设置为无限大flot('inf')
# 设置完无限大，上述更新result的过程就是比较更新前result和当前窗口长度，取最小值。
# 当出现特例的时候，假如result无限大，就返回0；否则就返回result

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        result = float('inf')   # 用于之后比较result，取最小值，如果遍历完没有result，即result等于无限大，则返回0
        sumup = 0   # 用于将滑动窗口中所有元素相加
        left = 0    # 左指针一开始为0
        for right in range (len(nums)): # 右指针开始移动
            sumup += nums[right]    # 计算窗口内所有元素之和
            while sumup >= target:  # 如果大于等于目标元素，开始收缩窗口，寻找最小子集
                result = min(result, right - left + 1)  # 比较滑动窗口长度大小，并记录当前最小值
                sumup -= nums[left] # 左边右移之后要在sumup里删除
                left += 1   # 更新左指针
        if result == float('inf'):
            return 0
        else:
            return result

'''
leetcode 904
你正在探访一家农场，农场从左到右种植了一排果树。这些树用一个整数数组 fruits 表示，其中 fruits[i] 是第 i 棵树上的水果 种类 。
你想要尽可能多地收集水果。然而，农场的主人设定了一些严格的规矩，你必须按照要求采摘水果：
你只有 两个 篮子，并且每个篮子只能装 单一类型 的水果。每个篮子能够装的水果总量没有限制。
你可以选择任意一棵树开始采摘，你必须从 每棵 树（包括开始采摘的树）上 恰好摘一个水果 。
采摘的水果应当符合篮子中的水果类型。每采摘一次，你将会向右移动到下一棵树，并继续采摘。
一旦你走到某棵树前，但水果不符合篮子的水果类型，那么就必须停止采摘。
给你一个整数数组 fruits ，返回你可以收集的水果的 最大 数目。

示例 1：
输入：fruits = [1,2,1]
输出：3
解释：可以采摘全部 3 棵树。

示例 2：
输入：fruits = [0,1,2,2]
输出：3
解释：可以采摘 [1,2,2] 这三棵树。
如果从第一棵树开始采摘，则只能采摘 [0,1] 这两棵树。

示例 3：
输入：fruits = [1,2,3,2,2]
输出：4
解释：可以采摘 [2,3,2,2] 这四棵树。
如果从第一棵树开始采摘，则只能采摘 [1,2] 这两棵树。

示例 4：
输入：fruits = [3,3,3,1,2,1,1,2,3,3,4]
输出：5
解释：可以采摘 [1,2,1,1,2] 这五棵树。

https://leetcode-cn.com/problems/fruit-into-baskets

'''
class Solution:
    def totalFruit(self, tree: list[int]) -> int:
        res, tree_len = 0, len(tree)
        one = tree[0]
        begin, end = 0, 1
        while (end < tree_len) and (tree[end] == one):
            end += 1
        if tree_len == end:
            return tree_len  # 找出第二种不同的水果，如果全部都是一种，输出tree的len

        two = tree[end]  # 此时确定tree里至少有两种水果
        end += 1  # 右指针开始向右运动
        while end < tree_len:
            if (one != tree[end]) and (two != tree[end]):  # 如果找到第三种水果
                res = max(res, end - begin)  # 记录当前一二种水果的len并且不断更新最大值
                one = tree[end - 1]  # 更新左边
                two = tree[end]  # 更新右边
                begin = end - 1  # 查找左边有无重复的果树，如果有要算上
                # 例如[1,2,2,2,1,1,1,1,3,4,5,6],此时one 和two 包裹的区间为[1,2,2,2,1,1,1,{1-begin,3-end},4,5,6]
                while tree[begin - 1] == one:  # 这个循环则把例子中begin前面的1全部囊括
                    begin -= 1
                    # [1,2,2,2,{1-begin,1,1,1,3-end},4,5,6]
            end += 1  # 然后end从3开始继续向右寻找
        return max(res, end - begin)

'''
leeetcode 76
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

示例 1：
输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"

示例 2：
输入：s = "a", t = "a"
输出："a"

示例 3:
输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，因此没有符合条件的子字符串，返回空字符串。

https://leetcode-cn.com/problems/minimum-window-substring

'''
# 利用快慢指针来创建滑动窗口，滑动窗口里的元素满足题目条件的时候，记录当前窗口长度，储存到字典里，然后慢指针加一继续判断
# 如果滑动窗口里的元素不满足题目条件，快指针加一继续判断
# 最后将fianl定义为长度的最小值，最后输出字典里key等于final的字符串就能达到目的

# 出现的问题: 虽然时间复杂度O(n)，测试用例都通过，但是LeetCode上会超时，需要另外的思路
def ziji(a:str,b:str) -> bool:
    if len(b) > len(a):
        return False
    i = 0
    while i < len(b):
        if a.count(b[i]) >= b.count(b[i]):
            i += 1
        else:
            return False
    return True

def minWindow(s: str, t: str) -> str:
    true_dict = dict()
    final = float('inf')
    fast, slow = 0, 0
    while fast <= len(s):

        if ziji(s[slow:fast], t):
            final = min(final, fast - slow + 1)
            true_dict[fast-slow+1] = s[slow:fast]

            slow += 1
        else:
            fast += 1
    if final == float('inf'):
        result = ''
    else:
        result = true_dict[final]
    return result

# 更加高效的做法
class Solution:
    def minWindow(self, s: str, t: str) -> int:
        need_dict = collections.defaultdict(int)
        for ch in t:
            need_dict[ch] += 1  # 将需要的元素加起来，算出其每一个需要的个数，储存在字典里。只有需要的元素为正数，其他不需要的元素为负数
        count = len(t)  # 是否满足子集的需求，右指针每框选一个目标元素，count-1，左指针每释放一个目标元素，count+1.
        # 只有count=0时，记录当前滑动窗口的位置
        i, j = 0, 0  # 初始化快慢指针
        res = [0, float('inf')]

        for j in range(len(s)):
            if need_dict[s[j]] > 0:  # 只有必要字符才可能大于0
                count -= 1
            need_dict[s[j]] -= 1
            if count == 0:
                while count == 0:

                    if res[1] - res[0] > j - i:  # 记录最小覆盖子串
                        res = [i, j]

                    if s[i] in t and need_dict[s[i]] >= 0:  # 假如是目标元素，而且数值大于0了，count就会加1，说明此时达不到要求，需要右指针开始移动了
                        count += 1

                    need_dict[s[i]] += 1  # 左指针右移之前，释放元素当前左指针指的元素，释放完字典里对应元素的值需要加1
                    i += 1  # 左指针右移

        return '' if (res[1] - res[0]) > len(s) else s[res[0]:res[1] + 1]
