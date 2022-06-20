'''

涉及到的题目
LeetCode 206

'''
'''
leetcode 206
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

示例 1：
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]

示例 2：
输入：head = [1,2]
输出：[2,1]

示例 3：
输入：head = []
输出：[]

https://leetcode.cn/problems/reverse-linked-list

'''
# 双指针法
# 利用两个指针，一个pre（初始为None），一个cur（初始为head）
# 只需要每次循环将pre和cur往后挪动一位，然后将cur指向pre即可完成链表的翻转
# 但是存在的问题就是cur.next = pre 会导致原先的链表丢失，所以需要一个临时储存的链表temp来存储cur.next之后的值
# 即当temp存储完 cur之后的值，将cur的链表方向指向pre。这个操作完成之后，将pre和cur向右移动一位，重复之前的操作

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur != None:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        head = pre
        return head

# 解法二，递归法。本质上与解法一是一样的，但是代码写的方式不一样

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def re(pre, cur):
            if cur is None:
                return pre # 当递归结束之后返回pre，即反转过后链表的头

            tempt = cur.next
            cur.next = pre

            return re(pre=cur, cur=tempt) # 这一行就等同于解法一当中 pre = cur; cur = tempt

        return re(pre=None, cur=head)
