class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head = None

    def deletelist(self):
        current = self.head
        while current:
            prev = current.next

            del current.data
            current = prev

    def push(self,new_data):
        