def binary(a,si,ei):
    if si>ei:
        return -1
    mid=(si+ei)//2
    if a[mid]==1:
        l=binary(a,si,mid-1)
        if l!=-1:
            return l
        else:
            return mid
    else:
        return binary(a,mid+1,ei)


def transitionPoint(a, n):
    return binary(a,0,n-1)

if __name__=='__main__':
    n = int(input('Enter size of array: '))
    arr = [int(i) for i in input('Enter array elements: ').split()]
    print(transitionPoint(arr, n))
