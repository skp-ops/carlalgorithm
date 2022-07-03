'''

涉及到的题目
LeetCode 20

'''

def countSubstrings( s: str) -> int:

    if len(s) <= 1 : return len(s)
    dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
    for x in range(len(s)): dp[x][x] = 1
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            temp = 0
            for k in range(0, j):
                if s[k] == s[j]:
                    if j - k == 1 : temp += 1 # 如果前后指针碰巧挨在一起，也能组成一个回文子串 bba a，最后一个a与倒数第二个a也能组合成回文串
                    # elif s[k+1:j] == s[j-1:k:-1]: temp += 1 # abb a, 最后一个a与第一个a之间夹住的bb是回文串
                    else: temp += dp[k+1][j-1]
            dp[i][j] = dp[i][j-1] + temp + 1
    print(dp)
    return dp
countSubstrings('aaabcabaacsvsdvsdv')
