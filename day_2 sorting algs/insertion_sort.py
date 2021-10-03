# Build longer and longer sorted slices.
# In each iteration arr[0:i is sorted]

def insertion_sort(arr):
    n = len(arr)

    for i in range(n):
        pos = i
        while i>0 and arr[pos] < arr[pos-1]:
            arr[pos],arr[pos-1] = arr[pos-1], arr[pos]
            pos = pos-1 # make the sequence shorter
    return(arr)


# test
arr = [1,3,2,45,23,12,56]
print(insertion_sort(arr))
