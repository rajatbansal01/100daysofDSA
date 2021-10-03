# will do for the left rotation of array.

def left_rotate(arr,d,n):
    for i in range(d):
        rotate_by_one(arr,n)
    return(arr)


def rotate_by_one(arr,n):
    store = arr[0]  # storing the first element of the array.
    for i in range(n-1):
        arr[i]=arr[i+1] # shift each element by one to the left.

    arr[n-1] = store   # replacing the last element by the first element.

    return(arr)



# testing our program


arr = [2,3,4,5,6,7,8]
d = 3
n= len(arr)

print(left_rotate(arr,d,n))