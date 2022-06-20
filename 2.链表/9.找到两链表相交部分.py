'''

涉及到的题目
LeetCode 面试题02.07

'''
'''
leetcode 面试题02.07
给你两个单链表，如果有相交的部分则求出相交部分的链表
如果没有相交则返回None
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
'''
常规解法，用两个指针 求出哪个链表比较长，让该链表的指针先移动一部分，直到两者尾部对其时指针也是对其的
然后两个同步右移，注意取等条件是cura == curb，对应地址也要相等。而不仅仅是 cura.val == curb.val
'''
        lena = 0
        lenb = 0
        p = headA
        while p != None:
            lena += 1
            p = p.next
        p = headB
        while p != None:
            lenb += 1
            p = p.next
        diff = max(lena,lenb) - min(lena,lenb)
        cura = headA
        curb = headB
        for i in range(diff):
            if lenb > lena:
                curb = curb.next
            else:
                cura = cura.next
        while cura != None or curb != None:
            if cura == curb:
                return cura
            else:
                cura = cura.next
                curb = curb.next
        return None

#  解法二
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        根据快慢法则，走的快的一定会追上走得慢的。
        在这道题里，有的链表短，他走完了就去走另一条链表，我们可以理解为走的快的指针。

        那么，只要其中一个链表走完了，就去走另一条链表的路。如果有交点，他们最终一定会在同一个
        位置相遇
        """
        cur_a, cur_b = headA, headB  # 用两个指针代替a和b

        while cur_a != cur_b:
            cur_a = cur_a.next if cur_a else headB  # 如果a走完了，那么就切换到b走
            cur_b = cur_b.next if cur_b else headA  # 同理，b走完了就切换到a

        return cur_a