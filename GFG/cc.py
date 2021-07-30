def CircularArrayRotation(arr,k,query):
    # rotate the array "arr" k times towards right direction
    # query is the list of index of the element to be queried
    # return all the value of the queried element in a list
    arr = arr[-k:] + arr[:-k]
    return [arr[i] for i in query]