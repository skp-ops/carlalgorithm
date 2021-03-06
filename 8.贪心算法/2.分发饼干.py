'''

涉及到的题目
LeetCode 455

'''
'''
leetcode 455
假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。
对每个孩子 i，都有一个胃口值g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j]。
如果 s[j]>= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。

示例1:
输入: g = [1,2,3], s = [1,1]
输出: 1
解释: 
你有三个孩子和两块小饼干，3个孩子的胃口值分别是：1,2,3。
虽然你有两块小饼干，由于他们的尺寸都是1，你只能让胃口值是1的孩子满足。
所以你应该输出1。

示例2:
输入: g = [1,2], s = [1,2,3]
输出: 2
解释: 
你有两个孩子和三块小饼干，2个孩子的胃口值分别是1,2。
你拥有的饼干数量和尺寸都足以让所有孩子满足。
所以你应该输出2.

https://leetcode.cn/problems/assign-cookies

'''
# 这里题目中说明了，饼干不能拆分，所以一块饼干只能给一个孩子
# 思考一下,大饼干应该分给小胃口的孩子还是大胃口的孩子:
#         显然,大饼干分给大胃口的孩子,小饼干分给小胃口的孩子
#         因为假如大饼干分给小胃口的孩子,那么饼干很大一部分都被浪费,后面胃口大的孩子分到的饼干太小了不满足他们的胃口
#         这样子我们就无法尽可能满足多的孩子胃口了.
#         因此我们要控制每次饼干-胃口的数最小,这样才能避免浪费,让足够多的孩子吃到饼干,满足他们胃口

# 解题方法是，首先将胃口和饼干数组排序，从后向前遍历，假如胃口大于饼干，说明这个孩子肯定无法满足
#           g数组向前遍历一位，找到胃口稍微小的孩子，然后再比较胃口和饼干大小，如果此时满足要求
#           说明该小孩能满足，胃口和饼干同时减1.
#           退出循环的条件是假设两个数组中有一个数组遍历结束，则退出循环，并且返回满足小孩的个数
#
# 局部最优：大饼干喂给胃口大的孩子；全局最优：喂饱尽可能多的孩子
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        pointer_g , pointer_s = len(g) - 1, len(s) - 1
        count = 0
        while pointer_g >= 0:
            if pointer_s == -1:
                return count
            if g[pointer_g] > s[pointer_s]:
                pointer_g -= 1
            else:
                count += 1
                pointer_g -= 1
                pointer_s -= 1
        return count