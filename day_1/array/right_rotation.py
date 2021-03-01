#right rotation of array
#it avoids unnecessary no. of recursions for large no. of rotations.
def right_rot(arr,s):# r is the no. of times to rotate
    n=len(arr)
    s=s%n
    #print(s)
    for a in range(s):
        store=arr[n-1]
        for i in range(n-2,-1,-1):
            arr[i+1]=arr[i]
        arr[0]=store
    return(arr)


arr = [11,1,2,3,4]
s = 1
print(right_rot(arr,s))