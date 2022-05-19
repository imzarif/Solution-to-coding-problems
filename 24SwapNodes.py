class Node:
    def __init__(self,val = None, next = None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_instart(self,val):
        node = Node(val,self.head)
        self.head = node

    def add_inend(self, val):
        if self.head==None:
            self.head = Node(val, None)
            return

        else:
            iter = self.head
            while iter.next:
                iter = iter.next

            node = Node(val)
            iter.next = node

    def add_values(self,values):
        self.head = None
        for i in values:
            self.add_inend(i)

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        iter = self.head
        liststr = ""
        while iter:
            liststr += str(iter.val) + "-->"
            iter = iter.next

        print(liststr)

    def swapPairs(self):
        if self.head==None or self.head.next==None:
            return self.head
        iter = self.head
        dummy = self.head.next
        prev_iter = iter
        while iter.next:
            temp = iter.next   #assign 2nd value to a temporary var
            prev_iter.next = temp
            print(iter.val, temp.val)
            if temp.next:
                iter.next = temp.next   #assign next of first to 3rd
                temp.next = iter       # finally switch first and 2nd
            else:
                break
            prev_iter = iter
            iter = iter.next

        iter.next = None
        temp.next = iter
        self.head = dummy




linkedlist = LinkedList()
linkedlist.add_values([1])
linkedlist.swapPairs()
linkedlist.print()

