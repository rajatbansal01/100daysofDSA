#sorting the queue  
import queue  
q = queue.Queue()  
  
q.put(100)  
q.put(67)  
q.put(11)  
q.put(8)  
q.put(13)  
  
  
# Here, we use bubble sort algorithm for sorting  
n =  q.qsize()  
for i in range(n):  
    # Remove the element  
    x = q.get()  
    for j in range(n-1):  
        # Remove the element  
        y = q.get()  
        if x > y :  
            # put the smaller element at the beginning of the queue  
            q.put(y)  
        else:  
            # the smaller one is put at the start of the queue  
            q.put(x)  
            x = y    # The greater element is replaced by the x and check again  
    q.put(x)  
  
while (q.empty() == False):   
    print(q.queue[0], end = " ")    
    q.get()  