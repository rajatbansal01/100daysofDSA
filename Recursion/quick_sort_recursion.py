def partition(a,si,ei):
    p = a[si]
    c = 0 # c will be number of elements smaller than p
    for i in range(si,ei+1):
        if a[i] < p:
            c += 1
    a[si], a[si+c] = a[si+c], a[si]
    i = si
    j = ei
    while i < j:
        if a[i] < p:
            i = i+1
        elif a[j] >= p:
            j = j-1
        else:
            a[i], a[j] = a[j], a[i]
            i = i+1
            j = j-1
    return si+c
  


def quick_sort(arr,si,ei):
  if si >= ei:
      return
  i = partition(arr,si,ei)
  quick_sort(arr,si,i-1)
  quick_sort(arr, i+1, ei)
        

      
a = [5,1,3,5,7,2,4,6,8,5,5,5,5]
quick_sort(a,0,len(a)-1)
