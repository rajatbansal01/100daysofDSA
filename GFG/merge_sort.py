#User function Template for python3

class Solution:
    def merge(self,arr, L, R):
        l=r=k=0
        while l<len(L) and r<len(R):
            if L[l]<R[r]:
                arr[k]=L[l]
                l+=1
            else:
                arr[k]=R[r]
                r+=1
            k+=1
        while l<len(L):
            arr[k] = L[l]
            l+=1
            k+=1
        while r<len(R):
            arr[k] = R[r]
            r+=1
            k+=1
            
            
            
    def mergeSort(self,arr, l, r):
        if len(arr)<=1:
            return
        m = len(arr)//2
        left = arr[:m]
        right = arr[m:]
        
        Solution().mergeSort(left, 0, len(left)-1)
        Solution().mergeSort(right, 0, len(right)-1)
        
        Solution().merge(arr, left,right)
        
        
            
            
            
            
        #code here


#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().mergeSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends