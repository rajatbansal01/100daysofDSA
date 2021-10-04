def peakElement(a,n):
    if n==1:
        return 0
    for i in range(n-1):
        if a[i]>a[i+1]:
            return i
        if i==n-2:
            return n-1

if __name__=='__main__':
    t = int(input('Enter no of test cases: '))
    for i in range(t):
        n = int(input('Enter size of array: '))
        arr = list(map(int, input('Enter array Elements: ').strip().split()))
        index = peakElement(arr.copy(), n)
        flag = False
        if index<0 or index>=n:
            flag = False
        else:
            if index == 0 and n==1:
                flag = True
            elif index==0 and arr[index]>=arr[index+1]:
                flag = True
            elif index==n-1 and arr[index]>=arr[index-1]:
                flag = True
            elif arr[index-1] <= arr[index] and arr[index] >= arr[index+1]:
                flag = True
            else:
                flag = False

        if flag:
            print(1)
        else:
            print(0)    
