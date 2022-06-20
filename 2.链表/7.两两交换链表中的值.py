'''

涉及到的题目
LeetCode 24

'''
'''
leetcode 24
给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

示例 1：
输入：head = [1,2,3,4]
输出：[2,1,4,3]

示例 2：
输入：head = []
输出：[]

示例 3：
输入：head = [1]
输出：[1]

https://leetcode.cn/problems/swap-nodes-in-pairs

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        count = 0
        p = head
        while p != None:
            count += 1
            p = p.next
        if count <= 1:
            return head
        elif count % 2 == 0: # 偶数个
            pre = head
            cur = head.next
            start = cur # 记录交换之后的头结点
            while True:
                temp = cur.next
                cur.next = pre
                if temp != None:
                    pre.next = temp.next
                else:
                    pre.next = None
                pre = temp
                if pre is None:
                    return start
                else:
                    cur = pre.next

        else: # 奇数个
            pre = head
            cur = head.next
            start = cur
            while True:
                temp = cur.next
                cur.next = pre
                if temp.next != None:
                    pre.next = temp.next
                else:
                    pre.next = temp
                pre = temp
                if temp.next == None:
                    return start
                else:
                    cur = pre.next
                pre = temp