class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def makeLL(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = Node(arr[i])
        curr = curr.next
    return head


def printLL(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print()


def swapLL(head, i, j):
    """
    Swap two nodes in a linked list.
        Args:
        head (Node): head of the linked list
        i (int): index of the first node
        j (int): index of the second node
    """
    if i == j:
        return head
    if i == 0:
        head = swapLL(head.next, j-1, j)
    else:
        head = swapLL(head, i-1, j)
    curr = head
    for _ in range(i):
        curr = curr.next
    temp = curr.next
    curr.next = temp.next
    temp.next = curr
    return head


head = makeLL([1, 2, 3, 4, 5])
printLL(head)
swapLL(head, 2, 4)
printLL(head)
