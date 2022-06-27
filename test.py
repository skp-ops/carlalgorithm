'''

涉及到的题目
LeetCode 20

'''


def findLUSlength(strs) -> int:
    def sub_check(long_str, short_str):
        if len(long_str) < len(short_str): long_str, short_str = short_str, long_str
        i = j = 0
        while i < len(long_str) and j < len(short_str):  # 从长字符串中确定短字符串是否为子串
            if long_str[i] == short_str[j]:
                i += 1
                j += 1
            else:
                i += 1
        return j == len(short_str)  # 如果j遍历到头，说明找到了，是子串。否则说明长字符串遍历完了都没找到子串

    res = -1

    for i in range(len(strs)):
        record = True
        for j in range(len(strs)):
            if i != j:
                if not sub_check(strs[i], strs[j]):
                    continue
                else:
                    record = False
                    break
        if record and len(strs[i]) > res: res = len(strs[i])
    return res
print(findLUSlength(["aabbcc", "aabbcc","c","e","aabbcd"]))