'''

涉及到的题目
LeetCode 19

'''
'''
leetcode 19
给你一个链表，删除链表的倒数第n个结点，并且返回链表的头结点。

示例 1：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

示例 2：
输入：head = [1], n = 1
输出：[]

示例 3：
输入：head = [1,2], n = 1
输出：[1]

https://leetcode.cn/problems/remove-nth-node-from-end-of-list

'''
# 先计算出整条链表有多少个元素，用总数减去n就是需要删除元素的下标index
# 然后我们找到指定元素之前的一个元素，跳过目标元素即可
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None or head.next is None: # 假设链表没有元素或者只有一个元素，返回一个空链表
            head = None
            return head
        count = 0
        p = head
        while p != None:
            count += 1
            p = p.next
        if n == count: # 假设长度等于n说明删除头部元素
            head = head.next
            return head
        else:
            index = count - n
            pre = head
            for _ in range(index-1): # 找到index之前的一个元素
                pre = pre.next
            pre.next = pre.next.next
            return head