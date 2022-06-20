'''

涉及到的题目
leetcode 142

'''
'''
leetcode 142
给定一个链表的头节点 head，返回链表开始入环的第一个节点。如果链表无环，则返回null。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 
为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
不允许修改 链表。

具体例子请访问链接
https://leetcode.cn/problems/linked-list-cycle-ii

'''
# 八戒和悟空在树林中看见一个盘丝洞，此时悟空直接飞过去，八戒只能跑，飞的速度比跑的快2倍。
# 然后他们都从洞口进入洞内探寻，最终在洞内某处相遇，悟空说：八戒我刚才又经过洞口怎么没看见你，你干嘛去了？
# 八戒说，猴哥你飞得快比我走得快2倍，比我多绕这洞一圈了，看见妖怪了吗？
# 突然，八戒踩到机关，被传送回小树林看见盘丝洞的地方，
# 这是八戒给悟空传音说，猴哥洞里有机关，你别飞了，我们都用走的，因为你飞得比我走得快2倍，多在洞里飞了一圈，
# 所以我刚才走的路跟洞里的路一样长，我从小树林开始走向洞口，你从我们相遇处走到洞口，我们就能相遇在洞口了，然后一起进去捉妖怪。

# 评论区中对于该循环代码的解释，快指针一次走两步，慢指针一次走一步。
# 假如这个链表有循环，那么快慢指针一定会在环中的某一个位置相遇。
# 当他们相遇的时候此时重新建立一个指针指向头，步数为1，然后快指针步数也为1
# 当新指针和快指针相遇的时候，说明他们到达了环的头，具体数学证明可以参考leetcode解题区等
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: # 空链表或者只有一个元素的链表，直接返回None
            return None
        slow = fast = head # 初始化快慢指针
        slow = slow.next # 调整慢指针到1号位，准备开始循环
        fast = fast.next.next # 调整快指针到2号位，准备开始循环
        while fast != slow: # 如果快慢指针一直没有碰面则不断循环
            if fast is None or fast.next is None or slow is None: # 当链表不是循环链表的时候返回None
                return None
            fast = fast.next.next # 快指针一次走两步
            slow = slow.next # 慢指针一次走一步
        start = head # 退出循环说明快慢指针碰面了，此时创建一个start指针指向head
        while start != fast:
            '''start指针和fast指针速度一样，开始循环'''
            start = start.next
            fast = fast.next
        return start # 当碰面的时候说明到达了循环入口