'''

涉及到的题目
leetcode 1217

'''
'''
leetcode 1217
1217. 玩筹码
有 n 个筹码。第 i 个筹码的位置是 position[i] 。
我们需要把所有筹码移到同一个位置。在一步中，我们可以将第 i 个筹码的位置从 position[i] 改变为:
position[i] + 2 或 position[i] - 2 ，此时 cost = 0
position[i] + 1 或 position[i] - 1 ，此时 cost = 1
返回将所有筹码移动到同一位置上所需要的 最小代价 。

示例 1：
输入：position = [1,2,3]
输出：1
解释：第一步:将位置3的筹码移动到位置1，成本为0。
第二步:将位置2的筹码移动到位置1，成本= 1。
总成本是1。

示例 2：
输入：position = [2,2,2,3,3]
输出：2
解释：我们可以把位置3的两个筹码移到位置2。每一步的成本为1。总成本= 2。

示例 3:
输入：position = [1,1000000000]
输出：1

具体图片参考：https://leetcode.cn/problems/minimum-cost-to-move-chips-to-the-same-position/
'''
'''
贪心的思想，移动两步不需要钱，移动一步才需要收费1元
所以我们尽可能先移动免费的步数，将所有的筹码聚集在一起
最终形成的情况就是，在不花一分钱的情况下，能将所有的筹码聚集在1号位或者2号位
然后再开始移动一位，将筹码聚集在同一个位置
'''
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        '''移动2步不收费，移动一步才收费
        我们可以把所有金币都移动到1或者2的位置，且不需要花一分钱
        就是将位置对2取余数，最后剩下的都是0和1，只需要移动一次就可以将所有的0移动到1，或者将1移动到0
        取最小的一个即可'''
        for i in range(len(position)):
            position[i] = position[i] % 2
        return min(position.count(0), len(position)-position.count(0))