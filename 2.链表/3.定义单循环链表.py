# define the single cycle link list
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

class SingleCycleLinkeList(object):
    '''单向循环链表'''
    def __init__(self,node = None):
        '''链表必须要有一个头部参数来指向之后的节点，默认头部参数为None'''
        self.__head = node #私有属性
        if node :
            node.next = node # 头节点不为None的时候，要有一个回环，指向自己

    def is_empty(self):
        '''链表是否为空'''
        return self.__head == None

    def length(self):
        '''返回链表长度'''
        if self.is_empty():
            return 0
       # cur游标，用来移动遍历节点
        # count记录数量
        cur = self.__head
        count = 1 # 这里count不能再从0开始了，要从1开始
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        '''遍历整个链表'''
        if self.is_empty():
            return
        cur = self.__head
        while cur.next !=self.__head:
            print(cur.elem,end=' ')
            cur = cur.next
        print(cur.elem) # 退出循环，cur指向尾节点，但是尾节点的元素没打出来
        print('')

    def add(self,item):
        '''链表头部添加元素，头插法'''
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            self.__head = node
            cur.next = self.__head

    def append(self,item):
        '''链表尾部添加元素,尾插法'''
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head

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
            pre.next = node



    def remove(self,item):
        '''删除指定节点'''
    #     double pointer
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            if cur.elem == item:
                # 先判断此节点是否是头节点
                if cur == self.__head:
                    # 对于头节点
                    # 找尾节点的位置
                    pointer = self.__head
                    while pointer.next != self.__head:
                        pointer = pointer.next
                    self.__head = cur.next
                    pointer.next = self.__head
                else:
                    # 对于中间节点
                    pre.next = cur.next # 当cur到尾部的时候，不在循环之内，所以cur是尾部时要再分情况讨论
                return
            else:
                pre = cur
                cur = cur.next
    #     退出循环代表着cur指到了尾节点
        if cur.elem == item :
            # print('****')
            '''还应该考虑整个链表只有一个节点的时候，pre.next会报错'''
            if self.length() == 1:
                self.__head = None
            else:
                pre.next = cur.next

    def search(self,item):
        '''查找节点是否存在'''
        if self.is_empty():
            return False

        cur = self.__head
        while cur != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        if cur.elem == item: # 指向尾节点，但是不会进入循环
            return True
        else:
            return False
a = SingleCycleLinkeList()
a.append(2)
a.add(8)
a.append(3)
a.append(4)
a.append(5)
a.append(6)
a.append(7)
a.insert(-1,50)
a.travel()
a.remove(2)
a.remove(50)
a.remove(7)
a.travel()
