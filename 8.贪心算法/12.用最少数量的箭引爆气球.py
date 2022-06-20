'''

涉及到的题目
leetcode 452

'''
'''
452. 用最少数量的箭引爆气球
有一些球形气球贴在一堵用 XY 平面表示的墙面上。
墙面上的气球记录在整数数组 points ，其中points[i] = [xstart, xend] 表示水平直径在 xstart 和 xend之间的气球。
你不知道气球的确切 y 坐标。一支弓箭可以沿着 x 轴从不同点 完全垂直 地射出。在坐标 x 处射出一支箭，
若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足  xstart ≤ x ≤ xend，则该气球会被 引爆 。
可以射出的弓箭的数量 没有限制 。 弓箭一旦被射出之后，可以无限地前进。
给你一个数组 points ，返回引爆所有气球所必须射出的 最小 弓箭数 。
 
示例 1：
输入：points = [[10,16],[2,8],[1,6],[7,12]]
输出：2
解释：气球可以用2支箭来爆破:
-在x = 6处射出箭，击破气球[2,8]和[1,6]。
-在x = 11处发射箭，击破气球[10,16]和[7,12]。

示例 2：
输入：points = [[1,2],[3,4],[5,6],[7,8]]
输出：4
解释：每个气球需要射出一支箭，总共需要4支箭。

示例 3：
输入：points = [[1,2],[2,3],[3,4],[4,5]]
输出：2
解释：气球可以用2支箭来爆破:
- 在x = 2处发射箭，击破气球[1,2]和[2,3]。
- 在x = 4处射出箭，击破气球[3,4]和[4,5]。
'''
# 这道题本质就是找重合区间，如果几个区间之间有重合，就把他们当成一簇
# 然后要求所有区间中，最少簇是多少
# 贪心算法的思想在这边体现在：从头开始尽可能寻找最多的重合区间，进而推出满足所有区间的最小簇
# 所以我们需要先进行排序，然后进行之后的操作

# 解法一，利用双指针，两个while循环，
# 将第一个区间的右边界和下一个区间的左边界进行比较，如果大于等于说明可以包含在内。
#   然后更新右边界，取两者右边界的最小值，进行下一轮比较。
#   一旦比较失败，那么计数器加1，然后更新左右指针的坐标，将左指针移动到右指针的位置，右指针向加1，继续循环
#   同时进入新循环的时候更新右边界，直到循环结束，输出计数器即可
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 1: return 1
        points.sort()
        count = 0
        left, right = 0, 1
        while left < len(points):
            temp = points[left][1] # 记录右边界的值
            while right < len(points):
                temp = min(temp,points[right][1]) #每次比较右边界与左边界就更新一次右边界，取最小值
                if temp >= points[right][0]:
                    right += 1 # 如果满足重合区间这个条件，右指针一直右移
                    continue
                else: # 如果不满足，则说明需要新的箭
                    break
            count += 1 # 技术器加1
            left = right # 重新更新左指针
            right += 1 # 重新更新右指针，开始新一轮循环
        return count

# 解法二
# 用一个for循环来控制，中心思路一样
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 1: return 1
        points.sort()
        count = 1 # 初始化count，至少需要一根弓箭
        temp = points[0][1] # 初始化右边界
        for i in range(1,len(points)): # 这个i相当于右指针
            if temp >= points[i][0]: # 如果右区间大于等于左区间，说明是一个重合区间
                temp = min(temp,points[i][1]) # 更新右区间，取最小值
            else: # 如果不满足，说明这个不是一个重合区间，需要一根新的箭
                count += 1 # 计数器加1
                temp = points[i][1] # 更新右边界，继续循环
        return count