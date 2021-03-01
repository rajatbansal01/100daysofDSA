def rotate_temp(arr, d, n):
    temp = arr[:d]  # storing array upto d elemets in temp.
    for j in range(n-d):
        arr[j]=arr[j+d]  # shift the remaining array.
    arr[-d:] = temp  # replace the last part with temp.
    return(arr)

arr = [1,2,3,4,5,6]  # actually a list
d= 4  # d is the number of elements by which we have to rotate.
n= len(arr)  
print(rotate_temp(arr,d,n))

