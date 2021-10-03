def sqrt(n):
    return(int(n**0.5))
def jump_search(arr,x):
    n=len(arr)

    step = sqrt(n)

    prev= 0
    while arr[int(min(step,n)-1)]<x:
        prev=step
        step +=  sqrt(n)
        
        if prev>=n:
            return -1

    while arr[int(prev)]<x:
        prev+=1

        if prev==min(step,n):
            return -1
    if arr[int(prev)]==x:
        return prev

    return -1

arr=[1,2,3,4,5,6]
print(jump_search(arr,6))

