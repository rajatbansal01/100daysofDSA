#implementing queue using collection.deque
from collections import deque

# Initializing a queue
q = deque()

# Adding elements to a queue
q.append('l')
q.append('o')
q.append('k')
q.append('e')
q.append('s')
q.append('h')

print("Initial queue")
print(q)

# Removing elements from a queue
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nQueue after removing elements")
print(q)


