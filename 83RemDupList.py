import LinkedList
Node = LinkedList.Node(None, None)
def RemoveDupList(head):
    cur = head
    if cur.next==None:
        return cur
    cmp = cur.next
    while cmp:
        print(cur.data)
        if cur.data!=cmp.data:
            cur.next = cmp
            cur = cmp
            cmp = cmp.next
        else:
            cmp=cmp.next
            cur.next=cur.next.next
    print(head.data, head.next.data, head.next.next.data, head.next.next.next.data,
          head.next.next.next.next.data)
    return head



list1 = LinkedList.LinkedListt()
list1.insert_new_values([1,1,2,2,2,3,3,4,5])
print(RemoveDupList(list1.head))

