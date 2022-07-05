'''

涉及到的题目
leetcode 22

'''
'''
leetcode 22
22. 括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例 1：
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]

示例 2：
输入：n = 1
输出：["()"]
'''
'''
将其想象成一棵树，想要生成一个合法的括号组合，必须要左括号等于右括号，并且在生成过程中，右括号的个数永远不会多于左括号的个数
所以我们假设目前生成的是'(()'（n=4），此时左括号是多于右括号且没超限，我们就进行两个dfs，一个节点分成两个分支，
分别生成'(()('以及'(())'. 当左右括号都达到4的时候，就把结果append到res中，然后return
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(string, left, right):
            if left == right == n:
                res.append(string)
                return
            if right <= left <= n: # 只要左括号大于等于右括号，且不超过n，那么就一定有其他分支解，一直搜下去
                dfs(string + '(', left+1, right)
                dfs(string + ')', left, right+1)
        dfs('', 0, 0)
        return res