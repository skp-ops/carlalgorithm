'''

涉及到的题目
LeetCode 203

'''
'''
leetcode 203
给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。

示例 1：
输入：head = [1,2,6,3,4,5,6], val = 6
输出：[1,2,3,4,5]

示例 2：
输入：head = [], val = 1
输出：[]

示例 3：
输入：head = [7,7,7,7], val = 7
输出：[]

https://leetcode.cn/problems/remove-linked-list-elements

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy_head = ListNode() # 先创建一个虚拟头结点
        dummy_head.next = head # 将虚拟头节点连接在链表头的位置
        cur = dummy_head # 创建一个指针开始从头移动
        while cur.next != None: # 当指针下一位为None，即移动到尾结点的时候停止循环
            if cur.next.val == val:
                cur.next = cur.next.next # 找到目标val，跳过该链表
            else:
                cur = cur.next # 否则就继续移动
        return dummy_head.next # 返回dummy_head之后的链表