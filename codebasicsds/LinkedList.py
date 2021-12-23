class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None

    def insertAtBeginning(self,data):
        new_node = Node(data,self.head)
        self.head = new_node

    def printLinkedList(self):
        if(self.head is None):
            print("LinkedList is empty.")
            return

        itr = self.head
        llstr = ''
        while(itr):
            llstr = llstr + str(itr.data) + '-->'
            itr = itr.next

        print(llstr)

    def insertAtEnd(self,data):
        new_node = Node(data)
        if(self.head is None):
            self.head = new_node
            return
        itr = self.head
        while(itr.next):
            itr = itr.next
        itr.next = new_node

    def insertValues(self,list):
        for item in list:
            self.insertAtEnd(item)

    def getCount(self):
        if self.head is None:
            return(0)
        itr=self.head
        count = 1
        while(itr.next):
            count += 1
            itr = itr.next
        return(count)

    def removeAt(self,index):
        if(index < 0 or index > self.getCount()-1):
            raise Exception ("Index invalid out of range.")

        if(index==0):
            self.head = self.head.next
            return

        itr=self.head
        i=0
        while(i < index-1):
            itr = itr.next
            i+=1
        itr.next = itr.next.next

    def insertAt(self,index,data):
        if(index < 0 or index > self.getCount()):
            raise Exception("Index Invalid or Out of Range.")
        if index==0:
            self.insertAtBeginning(data)
            return
        itr = self.head
        i = 0
        while(i < index-1):
            itr=itr.next
            i=i+1
        temp = itr.next
        itr.next = Node(data,temp)

    def insertAfterValue(self,value,data):
        itr = self.head
        while(itr):
            if itr.data == value:
                temp = itr.next
                itr.next = Node(data,temp)
                break
            itr = itr.next

    def removeByValue(self,value):
        itr=self.head
        if itr.data == value:
            self.head = itr.next
            return
        while(itr.next):
            if itr.next.data == value:
                if itr.next.next:
                    itr.next = itr.next.next
                else:
                    itr.next = None
                break
            itr = itr.next



if __name__ == '__main__':
    pass

ll = LinkedList()
'''ll.insertAtBeginning(5)
ll.insertAtBeginning(89)
ll.insertAtEnd(35)
ll.insertValues(['banana','mango','grapes','orange'])
print(ll.getCount())
ll.printLinkedList()
ll.removeAt(3)
ll.insertValues(['banana','mango','grapes','orange'])
ll.printLinkedList()
ll.insertAt(4,'cashew')
ll.printLinkedList()
ll.insertValues(['banana','mango','grapes','orange'])
ll.printLinkedList()
ll.insertAfterValue('banana','cashew')
ll.printLinkedList()'''
ll.insertValues(['banana','mango','grapes','orange'])
ll.printLinkedList()
ll.removeByValue('orange')
ll.printLinkedList()
print(ll.getCount())
