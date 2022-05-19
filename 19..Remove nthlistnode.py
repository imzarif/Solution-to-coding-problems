class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(self.data, None)
        self.head = node

    def print(self):
        if self.head == None:
            print("Linked list is empty")
            return
        iter = self.head
        liststr = ""
        while iter:
            liststr += str(iter.data) + "-->"
            iter = iter.next
        print(liststr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        iter = self.head
        while iter.next:
            iter = iter.next
        iter.next = Node(data,None)
        return

    def insert_new_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        if self.head is None:
            return
        count = 0
        iter = self.head
        while iter:
            count+=1
            iter = iter.next

        return count

    def delete_node_from_end(self, n):
        index = self.get_length() - n+1
        iter = self.head
        count = 1
        while iter:
            if index==1:
                self.head = self.head.next
                return
            if count==index-1:
                iter.next = iter.next.next
                return
            iter = iter.next
            count+=1


head =   [1,2,3,4,5]
n = 2
ll = LinkedList()
ll.insert_new_values(head)
print(ll.get_length())
ll.print()
ll.delete_node_from_end(n)
ll.print()
print(ll.get_length())





