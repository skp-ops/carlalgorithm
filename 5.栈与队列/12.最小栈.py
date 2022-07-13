'''

涉及到的题目
leetcode 155

'''
'''
leetcode 155
155. 最小栈
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

实现 MinStack 类:
MinStack() 初始化堆栈对象。
void push(int val) 将元素val推入堆栈。
void pop() 删除堆栈顶部的元素。
int top() 获取堆栈顶部的元素。
int getMin() 获取堆栈中的最小元素。

示例 1:
输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
'''
class MinStack:
    '''判断当前入栈的元素val是否比之前的最小值更小
    如果不是最小的，那么val入栈，辅助栈推入最小值
    如果是最小的，那么val入栈，最小值更替为val，辅助栈推入最小值
    在出栈的时候，辅助栈也要跟着一起出栈，这样才能保证最小值的及时更新'''
    def __init__(self):
        self.stack = []
        self.min_value = [float('inf')]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_value.append(min(val, self.min_value[-1]))

    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.min_value = self.min_value[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_value[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()