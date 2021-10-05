def Binary_Search(arr,lower,high,x):
    #base case
    if lower > high:
        return -1
    mid=(lower+high)//2
    if x==arr[mid]:
        return mid
    elif x>arr[mid]:
        lower=mid+1
        return Binary_Search(arr,lower,high,x)
    else:
        high=mid-1
        return Binary_Search(arr,lower,high,x)  
#Enter Input Array
arr=[int(x) for x in input().split()]
#Enter Search Element
x=int(input())
y=Binary_Search(arr,0,len(arr)-1,x)
if(y!=-1):
    print("Present is at ",y)
else:
    print("Absent")