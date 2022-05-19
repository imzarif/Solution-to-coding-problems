class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data #contains main data of linked list
        self.next = next #points to the next node
        self.prev = prev

class DLinkedList:
        def __init__(self):
            self.head = None

        def insert_at_beginning(self, data):
            node = Node(data, self.head, None)
            if self.head is None:
                self.head = node
            else:
                self.head.prev = node
                self.head = node


        def print_forward(self):
            if self.head is None:
                print("Linked List is empty")
                return

            iter = self.head
            llstr = ""
            while iter:
                llstr += str(iter.data) + "-->"
                iter = iter.next
            print(llstr)

        def print_backward(self):
            if self.head is None:
                print("Linked List is empty")
                return

            iter = self.head
            llstr = ""
            while iter.next:
               # llstr += str(iter.data) + "-->"
                iter = iter.next

            while iter:
                llstr += str(iter.data) +"-->"
                iter = iter.prev

            print(llstr)

        def insert_at_end(self, data):
            if self.head is None:
                self.head = Node(data, None, None)
                return

            iter = self.head
            while iter.next:
                iter = iter.next

            iter.next = Node(data, None, iter)


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
                    iter.next.prev = iter
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
                    node = Node(data, iter.next, iter)
                    if node.next:
                        node.next.prev = node
                    iter.next = node
                    break

                count+=1
                iter = iter.next

        def insert_after_value(self, data_after, data_to_insert):
            iter = self.head
            while iter:
                if iter.data==data_after:
                    node = Node(data_to_insert, iter.next, iter)
                    iter.next.prev = node
                    iter.next = node
                iter = iter.next

        def remove_at(self, data):
            iter = self.head
            while iter:
                if iter.next.data==data:
                    if iter.next.next:
                        iter.next.next.prev = iter
                    iter.next = iter.next.next
                    break
                iter = iter.next





if __name__ == '__main__':
    ll = DLinkedList()
    #ll.insert_at_beginning(5)
    #ll.insert_at_beginning(89)
    #ll.insert_at_end(43)
    ll.insert_new_values(["apple", "samsung", "lenovo", "hp"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at(2,"acer")
    ll.print_forward()
    ll.print_backward()
    ll.insert_after_value("samsung", "asus")
    ll.print_forward()
    ll.print_backward()
    ll.remove_at("hp")
    ll.print_forward()
    ll.print_backward()
    print(ll.get_length())

