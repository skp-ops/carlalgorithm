'''

涉及到的题目
leetcode 860

'''
'''
860. 柠檬水找零
在柠檬水摊上，每一杯柠檬水的售价为 5 美元。顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。
每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。
你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。
注意，一开始你手头没有任何零钱。
给你一个整数数组 bills ，其中 bills[i] 是第 i 位顾客付的账。如果你能给每位顾客正确找零，返回 true ，否则返回 false 。

示例 1：
输入：bills = [5,5,5,10,20]
输出：true
解释：
前 3 位顾客那里，我们按顺序收取 3 张 5 美元的钞票。
第 4 位顾客那里，我们收取一张 10 美元的钞票，并返还 5 美元。
第 5 位顾客那里，我们找还一张 10 美元的钞票和一张 5 美元的钞票。
由于所有客户都得到了正确的找零，所以我们输出 true。

示例 2：
输入：bills = [5,5,10,10,20]
输出：false
解释：
前 2 位顾客那里，我们按顺序收取 2 张 5 美元的钞票。
对于接下来的 2 位顾客，我们收取一张 10 美元的钞票，然后返还 5 美元。
对于最后一位顾客，我们无法退回 15 美元，因为我们现在只有两张 10 美元的钞票。
由于不是每位顾客都得到了正确的找零，所以答案是 false。
'''
# 收取的钱只有5，10，20三种情况
# 当收到5元的时候不找钱，5元钱数量加1
# 当收到10元的时候找5元，10元钱数量加1，5元钱数量减1
# 当收到20元的时候找15元，10元5元各减1，或者没有10元的时候5元减3
#   判断如果满足不了找钱的条件的时候返回False
#   否则遍历完返回True
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_dollars = 0
        ten_dollars = 0
        twenty_dollars = 0
        for i in bills:
            if i == 5:
                five_dollars += 1
            elif i == 10:
                if five_dollars: # 有5元直接找
                    five_dollars -= 1
                    ten_dollars += 1
                else: # 没5元返回False
                    return False
            elif i == 20:
                if ten_dollars: # 有10元优先给10元
                    ten_dollars -= 1
                    twenty_dollars += 1
                    if five_dollars: # 有5元再给一张5元
                        five_dollars -= 1
                    else: # 否则返回False
                        return False
                else:
                    if five_dollars >= 3: # 没有10元给3张5元
                        twenty_dollars += 1
                        five_dollars -= 3
                    else: # 没有则返回False
                        return False
        return True 
        # 遍历结束返回True
