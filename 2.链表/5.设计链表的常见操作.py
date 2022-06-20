'''

涉及到的题目
LeetCode 707

'''
'''
leetcode 707
设计链表的实现。您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val和next。
val是当前节点的值，next是指向下一个节点的指针/引用。
如果要使用双向链表，则还需要一个属性prev以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。

在链表类中实现这些功能：
get(index)：获取链表中第index个节点的值。如果索引无效，则返回-1。
addAtHead(val)：在链表的第一个元素之前添加一个值为val的节点。插入后，新节点将成为链表的第一个节点。
addAtTail(val)：将值为val 的节点追加到链表的最后一个元素。
addAtIndex(index,val)：在链表中的第index个节点之前添加值为val 的节点。如果index等于链表的长度，则该节点将附加到链表的末尾。
如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
deleteAtIndex(index)：如果索引index 有效，则删除链表中的第index 个节点。

示例：

MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1,2);   //链表变为1-> 2-> 3
linkedList.get(1);            //返回2
linkedList.deleteAtIndex(1);  //现在链表是1-> 3
linkedList.get(1);            //返回3

https://leetcode.cn/problems/design-linked-list

'''


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self, node=None):
        self.__head = node

    def length(self):
        if self.__head is None:
            return 0
        else:
            count = 1
            cur = self.__head
            while cur.next != None:
                count += 1
                cur = cur.next
            return count

    def get(self, index: int) -> int:
        if self.__head is None:  # 空链表的情况
            return -1
        if self.length() == 1 and index == 0:  # 一个元素的链表
            return self.__head.val
        if index < 0 or index >= self.length():  # index不符合要求
            return -1
        cur = self.__head
        count = 0
        while cur.next != None:  # 非空链表的情况
            if count != index:
                cur = cur.next
                count += 1
            else:
                return cur.val
        return cur.val

    def addAtHead(self, val: int) -> None:
        item = Node(val)
        item.next = self.__head
        self.__head = item

    def addAtTail(self, val: int) -> None:
        item = Node(val)
        if self.__head is None:  # 空链表
            self.__head = item
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = item

    def addAtIndex(self, index: int, val: int) -> None:
        lens = self.length()
        item = Node(val)
        if index <= 0:
            self.addAtHead(val)
            return
        if index == lens:
            self.addAtTail(val)
            return
        if index > lens:
            return
        if index < lens:
            pointer = self.__head
            for _ in range(index - 1):
                pointer = pointer.next
            item.next = pointer.next
            pointer.next = item

    def deleteAtIndex(self, index: int) -> None:
        cur = self.__head
        if self.__head is None or index > self.length() or index < 0:  # 空链表或者index无效
            return
        if self.length() == 1 and index == 0:  # 单个元素链表删除
            self.__head = None
            return
        else:
            if index == 0:
                self.__head = cur.next
                return
            else:
                pointer = self.__head
                pre = 0
                while pointer.next != None:
                    if pre == index - 1:
                        pointer.next = pointer.next.next
                        return
                    else:
                        pre += 1
                        pointer = pointer.next
        return