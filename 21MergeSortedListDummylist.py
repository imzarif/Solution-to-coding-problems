import LinkedList

def MergeSorted(l1, l2):
    dummy = LinkedList.Node()
    tail = dummy
    while l1 and l2:
        if l1.data<l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    return dummy.next


list1 = LinkedList.LinkedListt()
list2 = LinkedList.LinkedListt()
list1.insert_new_values([1,2,4])
list2.insert_new_values([5,6,7])
print(MergeSorted(list1.head, list2.head).data)
