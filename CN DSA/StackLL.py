class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    
    def __init__(self):
        self.__head = None
        self.count = 0
        
    def push(self,item):
        newNode = Node(item)
        newNode.next = self.__head
        self.__head = newNode
        self.count += 1
        
    def pop(self):
        if self.isEmpty:
            print("Empty")
            return
        else:
            self.__head = self.__head.next
            self.count -= 1
            return self.__head.data
  
    def top(self):
        if self.isEmpty():
            print("Empty")
            return
        else:
            return self.__head.data
        
    def size(self):
        return self.count
    
    def isEmpty(self):
        return self.size() == 0

s = Stack()
s.push(10)
s.push(20)
s.push(30)
while not s.isEmpty():
    print(s.pop())

        
        