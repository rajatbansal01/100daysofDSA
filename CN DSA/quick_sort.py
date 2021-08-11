def partition(arr,si,ei):
    """This takes a array and two indices, si and ei, and returns the index of the pivot element

    Args:
        arr (list): list to partition
        si (int): start index of list
        ei (int): end index of list
    """
    pivot = arr[ei]
    i = si
    for j in range(si,ei):
        if arr[j] <= pivot:
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
    arr[i],arr[ei] = arr[ei],arr[i]
    return i

def quick_sort(arr, si,ei):
    if si < ei:
        pi = partition(arr,si,ei)
        quick_sort(arr,si,pi-1)
        quick_sort(arr,pi+1,ei)
    
arr = [1,3,5,7,9,2,4,6,8,0]
quick_sort(arr,0,len(arr)-1)

print(arr)