class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def takeinput():
    inputlist=[int(ele) for ele in input().split()]
    head=None
    for currdata in inputlist:
        if currdata==-1:
            break
        newnode=node(currdata)
        if head is None:
            head=newnode
        else:
            curr=head
            while curr.next is not None:
                curr=curr.next
            curr.next=newnode
    return head
def printLL(head):
    while head is not None:
        print(str(head.data)+"->",end="")
        head=head.next
    print("None")
def mergesortedlist(h1,h2):
    if h1.data<h2.data:
        fh=h1
        ft=h1
        h1=h1.next
    else:
        fh=h2
        ft=h2
        h2=h2.next
    while h1 is not None and h2 is not None:
        if h1.data<h2.data:
            ft.next=h1
            ft=ft.next
            h1=h1.next
        else:
            ft.next=h2
            ft=ft.next
            h2=h2.next
    if h1 is not None:
        ft.next=h1
    else:
        ft.next=h2
    return fh
def sortlinkedlist(head):
    if head.next is None:
        return head
    slow=head
    fast=head
    while fast.next is not None and fast.next.next is not None:
        slow=slow.next
        fast=fast.next.next
    mid=slow
    head2=mid.next
    mid.next=None
    sortlinkedlist(head)
    sortlinkedlist(head2)
    fh=mergesortedlist(head,head2)
    return fh


head=takeinput()
#head2=takeinput()
#printLL(head1)
#printLL(head2)
#head3=mergesortedlist(head1,head2)
#printLL(head3)
head4=sortlinkedlist(head)
printLL(head4)