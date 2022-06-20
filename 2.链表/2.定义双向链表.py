# define the double link list
'''需要封装的操作 (全部都是对于链表类的对象方法)
is_emppty()链表是否为空
length()链表长度
travel()遍历整个链表
add(item)链表头部添加元素
append(item)链表尾部添加元素
insert(pos,item)指定位置添加元素
remove(item)删除节点
search(item)查找节点是否存在'''

class Node(object):
    '''node类'''
    def __init__(self,elem):
        self.elem = elem
        self.next = None # 对有一个节点的初始状态，我们不知道指向谁，所以就指向空
        self.prev = None

class DoubleLinkeList(object):
    '''双链表'''
    def __init__(self,node = None):
        '''链表必须要有一个头部参数来指向之后的节点，默认头部参数为None'''
        self.__head = node #私有属性

    def is_empty(self):
        '''链表是否为空'''
        return self.__head is None

    def length(self):
        '''返回链表长度'''
       # cur游标，用来移动遍历节点
        # count记录数量
        count = 0
        cur = self.__head
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        '''遍历整个链表'''
        cur = self.__head
        while cur != None:
            print(cur.elem,end=' ')
            cur = cur.next
        print('')

    def add(self,item):
        '''链表头部添加元素，头插法'''
        node = Node(item)
        if self.__head != None:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node
        else:
            self.__head = node

    def append(self,item):
        '''链表尾部添加元素,尾插法'''
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self,pos,item):
        '''链表指定位置添加元素'''
        node = Node(item)
        if pos <= 0:
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:
            pre = self.__head # 指针从头指向position前面的node,首先指到第一个node
            for count in range(pos-1):
                pre = pre.next # 循环结束后pre指向pos前一个
            node.next = pre.next
            node.prev = pre
            pre.next.prev = node
            pre.next = node

    def remove(self,item):
        '''删除指定节点'''
    #     single pointer
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                # 判断此节点是否是头节点
                # 如果是头节点
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next != None: # 对于 head - 1 - None 这种情况，判断链表是否只有一个节点
                        cur.next.prev = None
                elif cur.next == None: # 判断是否在尾部
                    cur.prev.next = cur.next
                else: # 一般情况
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                break
            cur = cur.next

    def search(self,item):
        '''查找节点是否存在'''
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

dll = DoubleLinkeList()
dll.append(1)

dll.remove(1)
dll.travel()