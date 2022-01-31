from collections import deque

class Node():
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        new_node = Node(data,self.head)
        self.head = new_node

    def print_linked_list(self):
        itr = self.head
        llstr = ""
        if not itr:
            print("LinkedList is empty")
            return
        while(itr):
            llstr = llstr + str(itr.data) + "-->"
            itr = itr.next
        print(llstr)

    def insert_list(self,items):
        for item in items:
            self.insert_at_beginning(item)

def addTwoNumbers():
    l1 = LinkedList()
    l1.insert_list([3,4,2])
    l2 = LinkedList()
    l2.insert_list([4,6,5])
    l1.print_linked_list()
    l2.print_linked_list()


    i = 0
    carry = 0
    retlist = LinkedList()
    retlist.insert_at_beginning(0)
    l3 = retlist

    while l1 or l2 or carry > 0:
        if i > 0:
            l3.next = Node(0,None)
            l3 = l3.next

        digsum =  ((l1.data if l1 else 0) + (l2.data if l2 else 0)) * pow(10,i) + carry
        carry  =  int(digsum/10)
        l3.data =  digsum % 10

        i = i+ 1
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    retlist.print_linked_list()


if __name__ == "__main__":
    addTwoNumbers()
