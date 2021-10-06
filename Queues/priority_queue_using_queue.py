from queue import PriorityQueue

p = PriorityQueue()

# insert into queue
p.put((8, 'h'))
p.put((2, 's'))
p.put((3, 'e'))
p.put((4, 'k'))
p.put((5, 'o'))
p.put((1, 'l'))

# remove and return lowest priority item
print(p.get())
print(p.get())

# check queue size
print('Items in queue :', p.qsize())

# check if queue is empty
print('Is queue empty :', p.empty())

# check if queue is full
print('Is queue full :', p.full())
