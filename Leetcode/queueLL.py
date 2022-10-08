import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class qLL:
    def init(self, item):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, item):
        newNode = Node(item)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.count += 1

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def dequeue(self):
        if self.count > 0:
            item = self.head.data
            head = head.next
            count -= 1
            return item
        else:
            return("empty queue")

# Implement Queue using two stacks
