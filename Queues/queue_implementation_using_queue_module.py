
#implementation of queue using queue module

from queue import Queue

# Initializing a queue
q = Queue(maxsize = 3)

# qsize() give the maxsize of the queue
print(q.qsize())

# Adding of element to queue
q.put('l')
q.put('o')
q.put('k')

# Return Boolean for Full Queue
print("\nFull: ", q.full())

# Removing element from queue
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())

# Return Boolean for Empty Queue
print("\nEmpty: ", q.empty())

q.put(1)
print("\nEmpty: ", q.empty())
print("Full: ", q.full())


