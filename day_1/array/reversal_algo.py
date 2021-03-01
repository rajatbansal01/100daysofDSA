def reverse_array(arr, start, end):
    while start<end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start+=1
        end-=1
def left_rotate(arr,d,n):
    if d == 0:
        return None
    d = d%n # i.e the n time rotation will give same that array
    reverse_array(arr,0,d-1)
    reverse_array(arr,d,n-1)
    reverse_array(arr,0,n-1)


    return(arr)


arr = [11,12,13,14,15,16]
d= 2
n= len(arr)

print(left_rotate(arr,d,n))