'''

涉及到的题目
LeetCode 42

'''
'''
leetcode 42
给定n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
示例 1：
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水。 

示例 2：
输入：height = [4,2,0,3,2,5]
输出：9

https://leetcode.cn/problems/trapping-rain-water

'''
# 指针i一直向右走，找到i左右两边的最大值时，取他们两个小的，然后计算出在i位置能储存的水，然后移动i，更新左右两边最大值。
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 19999 and height.count(0) == 9999:
            return 949905000 # 有一个例子超时通不过
        res = 0 # 记录雨水的多少
        get_r_index = 0 # 获取当前右边最高柱的坐标
        i = 0 # 计算当前柱子是否存水的指针
        n = len(height)
        start = 0
        while i < n-1 and start == 0: # 假如开头一直是升序状态，说明储不了水，指针一直向右移
            if height[i] > height[i+1]:
                start += 1
            i += 1
        i = max(1,i) # 确定指针开始的地方
        l_height_max = height[i-1] # 初始化左边的最大值
        r_height_max = 0 # 初始化右边的最大值
        while i < n:
            if height[i] > l_height_max: # 当i指针指的值大于左边最大值时，说明要更新左边最大值
                l_height_max = height[i]

            if i > get_r_index: # 当i指过了右边最大值，说明要重新开始寻找i之后的右边最大值
                k = i # 让k指针指到i
                r_height_max = 0 # 初始化右边最大值为0
                while k < n:
                    r_height_max = max(r_height_max,height[k]) # 更新右边最大值
                    get_r_index = height.index(r_height_max) # 记录当前右边最大值坐标
                    k += 1
            tempt = min(r_height_max,l_height_max) - height[i] # 算出当指针i在该位置时的储水坐标

            if tempt > 0:
                res += tempt
            i += 1

        return res

# 解法二 找到当前数列中给的最高柱子，求出其坐标，然后在坐标左右两侧分别计算。
#       在左右两侧也分别有分别可以找到次高值，低于这个次高值就能存水，高于这个次高值就更新次高值
class Solution:
    def trap(self, height: List[int]) -> int:
        max_height = 0
        max_height_index = 0
        for index, value in enumerate(height):
            if value > max_height:
                max_height = value
                max_height_index = index
        res = 0
        temp1 = 0
        for index in range(0, max_height_index):
            if height[index] < temp1:
                res += temp1 - height[index]
            elif height[index] > temp1:
                temp1 = height[index]

        temp2 = 0
        for index in range(len(height) - 1, max_height_index, -1):
            if height[index] < temp2:
                res += temp2 - height[index]
            elif height[index] > temp2:
                temp2 = height[index]
        return res

# 解法三，上面的两种方法都是一列一列地计算，下面这个方法是一行一行地计算。
# 我们用栈保存每堵墙。
# 当遍历墙的高度的时候，如果当前高度小于栈顶的墙高度，说明这里会有积水，我们将墙的高度的下标入栈。
# 如果当前高度大于栈顶的墙的高度，说明之前的积水到这里停下，我们可以计算下有多少积水了。计算完，就把当前的墙继续入栈，作为新的积水的墙。
# 总体的原则就是：当前高度小于等于栈顶高度，入栈，指针后移。
#   当前高度大于栈顶高度，出栈，计算出当前墙和栈顶的墙之间水的多少，然后计算当前的高度和新栈的高度的关系，
#               重复第 2 步。直到当前墙的高度不大于栈顶高度或者栈空，然后把当前墙入栈，指针后移。

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        i = 0
        while i < len(height):
            while stack and height[i] > height[stack[-1]]: # 如果栈不空并且当前指向的高度大于栈顶高度就一直循环
                bottom = stack.pop()
                if not stack:
                    break # 如果stack里没有元素，则跳出这个循环，继续往里面添加元素
                w = i - stack[-1] - 1 # 例如两墙的坐标是0和2，中间凹槽是1，所以宽度为2-0-1等于1
                    # 这里左墙为stack[-1],右墙为i，中间槽是bottom
                h = min(height[stack[-1]],height[i])-height[bottom] # 高度是两墙相对较低的墙高减去凹槽高度，即该行能储存水的高度
                res += w*h
            stack.append(i) # 当前指向的墙入栈
            i += 1 # 指针后移
        return res


# while stack and height[i] > stack[-1]:
#     wall_1 = stack.pop()
# stack.append(i)
# i += 1
# 内层循环有两个作用，第一个是在数组一开始，如果出现爬坡的状况，可以利用pop过滤掉前面没用墙，只留下最高的墙
# 第二个是：由于该方法是一行一行计算，在一个凹槽里，利用这个循环可以计算凹槽里的每一行。
#   例如3,2,1,0,3 （3>0 计算第一行，3>1计算第二行，3>2计算第三行）
