'''

涉及到的题目
leetcode 459

'''

'''
leetcode 459
给定一个非空的字符串s，检查是否可以通过由它的一个子串重复多次构成。

示例 1:
输入: s = "abab"
输出: true
解释: 可由子串 "ab" 重复两次构成。

示例 2:
输入: s = "aba"
输出: false

示例 3:
输入: s = "abcabcabcabc"
输出: true
解释: 可由子串 "abc" 重复四次构成。 (或子串 "abcabc" 重复两次构成。)

https://leetcode.cn/problems/repeated-substring-pattern

'''
# 这里用到的思想就是，生成目标字符的next前缀表，通过getnext函数生成的前缀表只包括n-1个字符的最长公共前后缀的长度。
#   原因在于我们将整个列表向右移动了一位，第一位设置成了-1，例如以下的例子
#   a = getnext(16,'asdfasdfasdfasdf') # [-1, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#   a = getnext(9,'asdasdasd') # [-1, 0, 0, 0, 1, 2, 3, 4, 5]
#   a = getnext(4,'asas') # [-1, 0, 0, 1]
#   a = getnext(4,'asac') # [-1, 0, 0, 1]
#  问题出就出在第三例和第四例。看到前两例我们发现，由于前两例是重复子串，所以16-（11+1）=4,16一定能被4整除；9-（5+1）=3，9一定能被3整除。
#  到了第三例asas满足题目要求，asac不满足题目要求，但是生成的next数组是一样的，这就是因为getnext函数没有考虑到最后一个字符's'或者'c'
#  导致001只是记录了asa的prefix，
#  解决方法：1.将getnext函数改写一下，不要前移next列表，这样可以包含整个字符串的前缀表信息，具体写法在解法二
#           2.在不改写getnext的函数前提下，人为将字符串添加一个后缀*,使得字符串（例如 asas 变成 asas* ； asac 变成 asac*)
#             同时getnext中参数lens也要加1，从 getnext(len(s),s) 变成 getnext(len(s)+1,s+'*')
#             这样第三第四例输出的结果就是 [-1, 0, 0, 1, 2] 和 [-1, 0, 0, 1, 0]
#             只需要判断next列表最后一位是否为0，同时4能否被4-2整除，就能判断出是否为重复子串构成的字符串了
# 这个方法究其本质，就是通过next数组的最后一位，以及整个字符串的长度，算出单个重复子串的长度，再来判断是否能被整除，能整除说明是重复构成的。
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def getnext(n,target):
            next = ['' for i in range(n)]
            j,k = 0,-1
            next[0]=k
            while j < n-1:
                if k == -1 or target[j] == target[k]:
                    j += 1
                    k += 1
                    next[j] = k
                else:
                    k = next[k]
            return next
        lens = len(s)
        next = getnext(lens+1,s+'*') # 通过添加一个后缀，生成的next数组将包含前n-1个字符的最长公共前后缀信息

        if next[-1] != 0 and lens % (lens - next[-1]) == 0:
            return True
        else:
            return False

# 解法二，getnext函数的其他表达方法，去掉开头的-1，直接生成对应字符的最长公共前后缀
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def getnext(s):
            next = ['' for i in range(len(s))]
            k = 0
            next[0] = k
            for j in range(1, len(s)):
                while k > 0 and s[j] != s[k]:
                    k = next[k - 1]  # 假设j,k对应的字符不一样，而且k一直大于0，就不断向后跳跃，尽最大可能寻找重复前后缀,直到k回到原点0为止
                if s[j] == s[k]:  # 假设找到了某一个k使得jk对应的字符一样，则k加1
                    k += 1
                next[j] = k  # 无论k是否回到原点，还是找到了一个k满足s[j] == s[k]，都要更新next[j]的值
            return next

        next = getnext(s)
        print(next)
        if next[-1] != 0 and len(s) % (len(s) - next[-1]) == 0:
            return True
        else:
            return False
# 解法三
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        '''
        假设母串S是由子串s重复N次而成， 则 S+S则有子串s重复2N次，那么现在有： S=Ns， S+S=2Ns， 其中N>=2。
        如果条件成立， S+S=2Ns, 掐头去尾破坏2个s，S+S中还包含2*（N-1）s, 又因为N>=2, 因此S在(S+S)[1:-1]中必出现一次以上
        '''
        return s in (s+s)[1:-1]