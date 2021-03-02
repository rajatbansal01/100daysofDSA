def selection_sort(arr):
    n = len(arr) # store length of array in a variable

    for start in range(n):
        min_pos = start  # let the minimum position where we start each loop
        for i in range(start,n):
            if arr[i]<arr[min_pos] : # check if we find some element smaller than the starting element of loop
                min_pos = i # if yes we replace the minimum position by that index

        arr[start],arr[min_pos]=arr[min_pos],arr[start] # replace the actual element of array

    return(arr)


# testing
arr = [3,2,1,4,5,6]
print(selection_sort(arr))



                                    