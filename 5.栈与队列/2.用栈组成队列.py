'''

涉及到的题目
LeetCode 232

'''
'''
leetcode 232
请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：

实现 MyQueue 类：
void push(int x) 将元素 x 推到队列的末尾
int pop() 从队列的开头移除并返回元素
int peek() 返回队列开头的元素
boolean empty() 如果队列为空，返回 true ；否则，返回 false

说明：
你 只能 使用标准的栈操作 —— 也就是只有push to top,peek/pop from top,size, 和is empty操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。


示例 1：
输入：
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
输出：
[null, null, null, 1, 1, false]

解释：
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false

https://leetcode.cn/problems/implement-queue-using-stacks

'''
# 主要思路，一个栈（in）用来接收元素，一个栈（out）用来弹出元素。
# 接收元素用append即可，弹出时要判断：
#       假如两个栈都没有元素，则返回none，如果out栈有元素则直接pop。
#       假如out栈没有元素，但是in栈有元素，则将in栈的元素弹出，再填充到out栈里，执行完后弹出out栈里的最外层的元素
# 实现peek时，先利用写好的pop函数弹出一个元素作为返回值，然后再将该元素append到out栈里，以防止元素损失

class MyQueue:

    def __init__(self):
        '''
        建立两个栈，stack_in（用来push元素）；stack_out（用来pop元素）
        '''
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        '''
        有元素x进来，就将x添加到stack_in这个栈里面
        '''
        self.stack_in.append(x)

    def pop(self) -> int:
        '''
        从队列返回开头的元素，而且要移除它
        '''
        if self.empty():  # stack_in; stack_out都为空，就返回none
            return None

        if self.stack_out:  # 如果stack_out栈不是空的，则pop一个元素
            return self.stack_out.pop()
        else:  # 将stack_in里的元素移动到stack_out里
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self) -> int:
        '''
        从队列返回开头的元素，但是不移除，这里可以先利用pop()函数，移除开头的元素，然后再添加到stack_out栈，从而取消移除的效果
        '''
        result = self.pop()
        self.stack_out.append(result)
        return result

    def empty(self) -> bool:
        if self.stack_out or self.stack_in:
            return False
        else:
            return True
