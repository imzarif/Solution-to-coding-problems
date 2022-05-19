import LinkedList
def addTwoNumbers(l1,l2):
    dummy = LinkedList.Node(None, None)
    itr = dummy
    carry = 0
    while l1 or l2:
        if l1.next==None and l2.next!=None:
            l1.next = LinkedList.Node(0)
        if l2.next==None and l1.next!=None:
            l2.next = LinkedList.Node(0)
        summ = l1.data + l2.data + carry
        if summ >= 10:
            carry = 1
            summ = summ % 10
        else:
            carry = 0
        itr.data = summ
        if l1.next or l2.next:
            itr.next = LinkedList.Node()
            itr = itr.next
        l1 = l1.next
        l2 = l2.next
    if carry==1:
        itr.next = LinkedList.Node(1)


    return dummy
l1 = LinkedList.LinkedListt()
l2 = LinkedList.LinkedListt()
l1.insert_new_values([9,9,9,9,9,9,9])
l2.insert_new_values([9,9,9,9])
returned_list = addTwoNumbers(l1.head, l2.head)
while returned_list:
    print(returned_list.data)
    returned_list = returned_list.next