# A Linked List Node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
 
#function to print a given linked list
def printList(msg, head):
 
    print(msg, end='')
    ptr = head
    while ptr:
        print(ptr.data, end=' —> ')
        ptr = ptr.next
    print('None')
  
# Sorting two lists in increaing order and merge nodes to make one big sorted listreturned
def sortedMerge(a,b):
    if a is None:
        return b
    elif b is None:
        return a
     # pick either a or b, and recur
    if a.data <= b.data:
        result = a
        result.next = sortedMerge(a.next, b)
    else:
        result = b
        result.next = sortedMerge(a, b.next)
 
    return result
 
# Driver code
if __name__ == '__main__':
 
    # input keys
    keys = [1,2,3,4,5,6,7,8] # taking random numbers
 
    a = b = None 
    for i in reversed(range(0, len(keys), 2)):
        a = Node(keys[i], a)
 
    for i in reversed(range(1, len(keys), 2)):
        b = Node(keys[i], b)
 
    # print both lists
    printList('First List: ', a)
    printList('Second List: ', b)
 
    head = sortedMerge(a, b)
    printList('After Merge: ', head)
