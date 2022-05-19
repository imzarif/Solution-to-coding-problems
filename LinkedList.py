class Node:
    def __init__(self, data = None, next = None):
        self.data = data #contains main data of linked list
        self.next = next #points to the next node

class LinkedListt:
        def __init__(self):
            self.head = None

        def insert_at_beginning(self, data):
            node = Node(data, self.head)
            self.head = node

        def print(self):
            if self.head is None:
                print("Linked List is empty")
                return

            iter = self.head
            llstr = ""
            while iter:
                llstr += str(iter.data) + "-->"
                iter = iter.next
            print(llstr)

        def insert_at_end(self, data):
            if self.head is None:
                self.head = Node(data, None)
                return

            iter = self.head
            while iter.next:
                iter = iter.next

            iter.next = Node(data, None)

        def insert_new_values(self, data_list):
            self.head = None
            for data in data_list:
                self.insert_at_end(data)

        def get_length(self):
           count = 0
           itr = self.head
           while itr:
               count+=1
               itr = itr.next
           return count

        def remove_in(self, index):
            if index<0 or index>=self.get_length():
                raise Exception("Invalid Index")

            if index==0:
                self.head = self.head.next
                return

            count = 0
            iter = self.head
            while iter:
                if count == index-1:
                    iter.next = iter.next.next
                    break
                count+=1
                iter=iter.next

        def insert_at(self, index, data):
            if index<0 or index>=self.get_length():
                raise Exception("Invalid Index")

            if index==0:
                self.insert_at_beginning(data)
                return

            iter = self.head
            count = 0
            while iter:
                if count == index-1:
                    node = Node(data, iter.next)
                    iter.next = node
                    break

                count+=1
                iter = iter.next

        def insert_after_value(self, data_after, data_to_insert):
            iter = self.head
            while iter:
                if iter.data==data_after:
                    node = Node(data_to_insert, iter.next)
                    iter.next = node
                iter = iter.next

        def remove_at(self, data):
            iter = self.head
            while iter:
                if iter.next.data==data:
                    iter.next=iter.next.next
                    break
                iter = iter.next





if __name__ == '__main__':
    ll = LinkedListt()
    #ll.insert_at_beginning(5)
    #ll.insert_at_beginning(89)
    #ll.insert_at_end(43)
    ll.insert_new_values(["apple", "samsung", "lenovo", "hp"])
    ll.print()
    ll.insert_at(0,"acer")
    ll.insert_after_value("samsung", "asus")
    ll.remove_at("hp")
    ll.print()

    print(ll.get_length())

