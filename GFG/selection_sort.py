class Solution: 
    def select(self, arr, i):
        min_index = i
        for a in range(i+1,len(arr)):
            if arr[min_index]>arr[a]:
                min_index=a
        return min_index
                
            
            
    
    def selectionSort(self, arr,n):
        for b in range(n):
            min_index = Solution.select(self,arr,b)
            arr[b], arr[min_index] = arr[min_index],arr[b]
        return arr

            
        
        