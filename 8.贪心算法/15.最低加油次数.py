'''

涉及到的题目
leetcode 871

'''
'''
leetcode 871
871. 最低加油次数
汽车从起点出发驶向目的地，该目的地位于出发位置东面 target 英里处。
沿途有加油站，每个 station[i] 代表一个加油站，它位于出发位置东面 station[i][0] 英里处，并且有 station[i][1] 升汽油。
假设汽车油箱的容量是无限的，其中最初有 startFuel 升燃料。它每行驶 1 英里就会用掉 1 升汽油。
当汽车到达加油站时，它可能停下来加油，将所有汽油从加油站转移到汽车中。
为了到达目的地，汽车所必要的最低加油次数是多少？如果无法到达目的地，则返回 -1 。
注意：如果汽车到达加油站时剩余燃料为 0，它仍然可以在那里加油。如果汽车到达目的地时剩余燃料为 0，仍然认为它已经到达目的地。

示例 1：
输入：target = 1, startFuel = 1, stations = []
输出：0
解释：我们可以在不加油的情况下到达目的地。

示例 2：
输入：target = 100, startFuel = 1, stations = [[10,100]]
输出：-1
解释：我们无法抵达目的地，甚至无法到达第一个加油站。

示例 3：
输入：target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
输出：2
解释：
我们出发时有 10 升燃料。
我们开车来到距起点 10 英里处的加油站，消耗 10 升燃料。将汽油从 0 升加到 60 升。
然后，我们从 10 英里处的加油站开到 60 英里处的加油站（消耗 50 升燃料），
并将汽油从 10 升加到 50 升。然后我们开车抵达目的地。
我们沿途在1两个加油站停靠，所以返回 2 。
'''
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # 贪心思想，每经过一个加油站就把油带在身上，一直往target开
        # 什么时候没油了就先加最大桶的油，直到没油为止
        rest_fuel = startFuel
        stations.insert(0,[0,0]) # 增加一个起点，用来记录开到第一个加油站所花的油 stations[i][0]-stations[i-1][0]
        stations.append([target,0]) # 增加一个终点，表明到达终点
        count, oil_tank = 0, []
        for i in range(1,len(stations)):
            rest_fuel -= (stations[i][0]-stations[i-1][0]) # 每次经过一个加油站油就减少两个加油站之间相隔的距离
            while rest_fuel < 0 and oil_tank: # 当油不够的时候，且油桶里有油，就开始加最大的油
                rest_fuel -= heappop(oil_tank) # 由于python只有小顶堆，所以用负数来表示大顶堆
                count += 1 # 每加一桶，计数器加一
            if rest_fuel < 0: # 当油桶全部加完，油还是不够的时候，返回-1
                return -1
            heappush(oil_tank, -stations[i][1]) # ，每经过一个加油站，将油收入囊中
        return count