def bubble_sort(arr):
    n = len(arr)

    for i in range(n):  # iterate over all the elements
        swapped = False 


        for j in range(0,n-i-1): # last n-i elements will be sorted already

            if arr[j]>arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True  

        if swapped == False:  # if there is no swapping in inner loop means array is sorted and we can break the outer loop.
            break
    return(arr)


arr = [2,3,1,4,7,5]
print(bubble_sort(arr))

