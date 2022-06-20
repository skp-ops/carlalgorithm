'''

涉及到的题目
LeetCode 202

'''

'''
leetcode 202
编写一个算法来判断一个数 n 是不是快乐数。
「快乐数」定义为：
对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果这个过程 结果为1，那么这个数就是快乐数。
如果 n 是 快乐数 就返回 true ；不是，则返回 false 。

示例 1：
输入：n = 19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

示例 2：
输入：n = 2
输出：false

https://leetcode.cn/problems/happy-number

'''

# 这道题目看上去貌似一道数学问题，其实并不是！
# 题目中说了会 无限循环，那么也就是说求和的过程中，sum会重复出现，这对解题很重要！
# 当我们遇到了要快速判断一个元素是否出现集合里的时候，就要考虑哈希法了。
# 所以这道题目使用哈希法，来判断这个sum是否重复出现，如果重复了就是return false， 否则一直找到sum为1为止。
# 判断sum是否重复出现就可以使用unordered_set。

class Solution:
    def isHappy(self, n: int) -> bool:
        record = set()

        def calculate(n: int) -> int:  # 计算各个位上数平方的和
            sum = 0
            while n:  # 当n大于0的时候一直循环，n小于等于0停止循环
                sum += (n % 10) ** 2  # n对10取余数，求最右边一位数
                n = n // 10  # n对10整除，更新n
            return sum

        while True:
            n = calculate(n)
            if n == 1:
                return True

            if n in record:
                return False
            else:
                record.add(n)