def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return(i)
    return("not found")

arr=[2,3,4,5,6,7,45]
print(linear_search(arr,4))