def left_rotate(arr,d,n):
    d = d%n
    for i in range(n):
        print(str(arr[(d+i)%n]),end=" ")

    return None

arr = [1,2,3,45]
d = 2
n =len(arr)
left_rotate(arr,d,n)