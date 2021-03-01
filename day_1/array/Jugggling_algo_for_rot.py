def left_rotate(arr,d,n):
    d = d%n     # array is same as before after n rotations 
    sets = gcd(d,n)     # to find the number of iterations of outer loop.
    for i in range(sets):
        temp = arr[i]   # store first element of array 
        j = i   # store outer index 
        while True:         
            k = (j+d)%n     
            if k==i:
                break
            arr[j] = arr[k]
            j=k
        arr[j] = temp

    return(arr)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

            

arr = [1,2,3,4,5]
n=len(arr)
d = 2
print(left_rotate(arr,d,n))