'''

涉及到的题目
华为机考

'''
'''
消消乐
给定一个字符串，只包含小写字母。如果两个相邻元素相同，则相互消除，同时自动拼接字符串再次判断
最后输出消除完的字符串

例子1
输入：'abcdefggabc'
输出：'abcdefabc'
解释：两个相邻且相同的元素g被消除

例子2
输入：'bccbabbc'
输出：'ac'
解释：首先第一个和第二个c相邻且相同，被消除，同时新组成的字符串'bbabbc'又包含待消除的两处bb

例子3
输入：’abc‘
输出：’abc‘
'''

while True:
    try:
        strs = input()
        stack = []
        if strs == '':
            print('')
        for a in range(len(strs)):
            if not stack or strs[a] != stack[-1]:
                stack.append(strs[a])
            else:
                stack.pop()
        print(''.join(stack))
    except:
        break

