import LinkedList

def MergeSorted(list1, list2):
    if list1 is None:
        return list2
    elif list2 is None:
        return list1
    if list1.data<=list2.data:
        iter = list1
        main_head = iter
        head = list2
    else:
        iter = list2
        head = list1
        main_head = iter

    if iter.next == None:
        iter.next = head
        return main_head



    print(iter.data, iter.next.data, iter.next.next.data)
    print(head.data, head.next.data, head.next.next.data)
    while head and iter.next:

        if iter.next.data>=head.data:
            temp = head.next
            head.next = iter.next
            iter.next = head
            head = temp



        iter = iter.next
    if head !=None:
        iter.next = head
    return main_head





list1 = LinkedList.LinkedListt()
list2 = LinkedList.LinkedListt()
list1.insert_new_values([1,2,4])
list2.insert_new_values([5,6,7])
print(MergeSorted(list1.head, list2.head).next.next.next.next.next.data)
