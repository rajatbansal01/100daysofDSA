def recursive_insertion_sort(arr):
    isort(arr,len(arr))
    return(arr)

def isort(arr,k): # sort slice arr[0:k]
    if k>1:
        isort(arr,k-1)
        insert(arr,k-1)

def insert(arr,k):
    pos=k
    while pos>0 and arr[pos]<arr[pos-1]:
        arr[pos],arr[pos-1]=arr[pos-1],arr[pos]
        pos=pos-1


arr = [2,3,1,5,6]
print(recursive_insertion_sort(arr))