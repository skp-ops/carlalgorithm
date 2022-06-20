'''

涉及到的题目
LeetCode 225

'''
'''
leetcode 225
请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（push、top、pop 和 empty）。
实现 MyStack 类：
void push(int x) 将元素 x 压入栈顶。
int pop() 移除并返回栈顶元素。
int top() 返回栈顶元素。
boolean empty() 如果栈是空的，返回 true ；否则，返回 false 。

注意：
你只能使用队列的基本操作 —— 也就是push to back、peek/pop from front、size 和is empty这些操作。
你所使用的语言也许不支持队列。你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列, 只要是标准的队列操作即可。

示例：
输入：
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
输出：
[null, null, null, 2, 2, false]

解释：
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // 返回 2
myStack.pop(); // 返回 2
myStack.empty(); // 返回 False

https://leetcode.cn/problems/implement-stack-using-queues

'''
from collections import deque
class MyStack:
    '''
    使用两个队列来进行实现
    '''
    def __init__(self):
        '''
        需要引入双向队列 deque
        q1用来push元素
        q2只在pop时备份q1前n-1个元素
        '''
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        for i in range(len(self.q1)-1):
            self.q2.append(self.q1.popleft())
            # 这里要用popleft，例如q1为[1,2,3,4,5]
            # popleft 然后添加到q2的结果为[1,2,3,4]，q1只剩下[5]
            # 假如用pop 添加到q2的结果为[5,4,3,2]，q1剩下[1].不满足要求
        self.q1 , self.q2 = self.q2 , self.q1 # 交换q1，q2的元素，从而让q2剩下带pop的元素
        return self.q2.popleft()

    def top(self) -> int:
        result = self.pop()
        self.q1.append(result)
        return result

    def empty(self) -> bool:
        return not (self.q1 or self.q2)

# 优化，用一个队列实现栈
from collections import deque
class MyStack:
    '''
    使用一个队列来进行实现
    '''
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        for i in range(len(self.q)-1):
            self.q.append(self.q.popleft())
            # q = [1,2,3,4,5]
            # after popleft q became [5,1,2,3,4]
            # then popleft q ,result is 5
        return self.q.popleft()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return not self.q