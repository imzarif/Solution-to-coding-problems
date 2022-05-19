import LinkedList
def addTwoNumbers(l1,l2):
    iterl1 = l1
    iterl2 = l2
    while iterl1 or iterl2:
        if iterl1.next==None:
            while iterl2.next:
                iterl1.next = LinkedList.Node(0)
                iterl1 = iterl1.next
                iterl2 = iterl2.next
            break
        elif iterl2.next==None:
            while iterl1.next:
                iterl2.next = LinkedList.Node(0)
                iterl2 = iterl2.next
                iterl1 = iterl1.next
            break
        iterl1 = iterl1.next
        iterl2 = iterl2.next
    dummy = LinkedList.Node(None,None)
    tail = dummy  
    carry = 0
    iter1 = l1
    iter2 = l2
    while iter1:
        sum = iter1.data + iter2.data + carry
       # print(sum)
        carry = 0
        if sum>=10:
            carry = int(sum/10)
            #print(f'"carry:"  {carry}')
            sum = int(sum%10)
        tail.next = LinkedList.Node(sum)
        tail = tail.next
        iter1 = iter1.next
        iter2 = iter2.next

    if carry>0:
        tail.next = LinkedList.Node(carry)
    dummy = dummy.next
    return dummy

l1 = LinkedList.LinkedListt()
l2 = LinkedList.LinkedListt()

l1.insert_new_values([9,9,9,9,9,9,9])
l2.insert_new_values([9,9,9,9])
ret = (addTwoNumbers(l1.head,l2.head))
l = []
while ret:
    l.append(ret.data)
    ret = ret.next
print(l)


