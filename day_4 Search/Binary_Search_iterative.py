# condition for binary search is that array should be sorted.

def binary_search(arr,x):
    L=0
    R=len(arr)-1
    while L<=R :
        mid = L+(R-L)//2
        #print(mid)
        if arr[mid]==x:
            return(mid)
        elif arr[mid]<x:
            L = mid+1
        else:
            R = mid-1
    return -1

arr=[1,2,3,4,5]
print(binary_search(arr,3))
        
