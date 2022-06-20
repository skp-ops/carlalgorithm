'''

涉及到的题目
LeetCode 93
有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，
但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。
给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入'.' 来形成。
你 不能重新排序或删除 s 中的任何数字。你可以按 任何 顺序返回答案。

示例 1：
输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]

示例 2：
输入：s = "0000"
输出：["0.0.0.0"]

示例 3：
输入：s = "101023"
输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

https://leetcode.cn/problems/restore-ip-addresses

'''
# 与分割回文串的题目类似，都是在同一个字符串中进行切割操作，所以定义的backtracking函数必须要有start_index来定位，防止重复截取
# 同时此题要求的条件较多，首先判断的条件就是给的字符串长度是否合适，如果长度小于4或者大于12则返回[]
# 紧接着在每次判断是否结束循环，将path append到res时，需要判断当前path里的元素是否超过了4个，如果超过了就return。
#   然后我们所需要的结束循环条件就是path里元素刚好4个,同时start_index到达了len(s) 已经结束了循环,然后将path以"."组合起来推入res
# 单循环代码中,for循环里range可以有剪枝操作,凡是遇到取的组合或者分割字符有长度要求,就可以在这个地方剪枝

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []
        res = []
        path = []
        def backtracking(s,start_index):
            if len(path) > 4:
                return
            if len(path) == 4 and start_index == len(s):
                res.append(str(".".join(path)))
                return

            for i in range(start_index, min(start_index+3,len(s)) ):
                #  剪枝操作，截取的字段最多三个数字min(start_index+3,len(s))
                if 0<=int(s[start_index:i+1])<=255 and len(s[start_index:i+1]) == len(str(int(s[start_index:i+1]))):
                    # 判断大小是否满足，同时没有前导0
                    path.append(s[start_index:i+1])
                    backtracking(s,i+1)
                    path.pop()

        backtracking(s,0)
        return res