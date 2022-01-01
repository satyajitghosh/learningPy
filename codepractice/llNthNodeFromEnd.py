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

    def delete_nth_item_from_end(self,ind):
        ql = ind + 1
        itr = self.head
        itr_length = 0
        if not self.head:
            print("Linked List is empty")
            return
        if ind < 1:
            print("Index length incorrect. Must be integer > 1")
        q = deque()
        while(itr):
            q.appendleft(itr)
            if len(q) > ql:
                q.pop()
            itr = itr.next
            itr_length += 1
        if itr_length == index:
            self.head = self.head.next
        if len(q) > 2:
            q[-1].next = q[-3]
        if len(q) == 2:
            q[-1].next = None

def build_and_print_ll():
    list = [10,7,5,90,32,45,12,23]
    llist = LinkedList()
    llist.insert_list(list)
    llist.print_linked_list()
    llist.delete_nth_item_from_end(8)
    llist.print_linked_list()

if __name__ == "__main__":
    build_and_print_ll()
        llen = 0
        q = deque()

        while itr:
            q.lappend(itr)
            if len(q) > n+1:
                q.pop()
            itr = itr.next
            llen += 1

        if llen == n:
            self.head = self.head.next
            return
        
        if len(q) == 2:
            q[-1].next = None

        if len(q) > 2:
            q[-1].next = q[-3]
