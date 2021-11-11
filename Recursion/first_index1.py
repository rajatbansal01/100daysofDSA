def firstindexbetter(a,si,k):
    l=len(a)
    if l==si:
        return -1
    if a[si]==k:
        return si
    smallerlist=firstindexbetter(a,si+1,k)
    return smallerlist
a=[1,2,3,4,5]
print(firstindexbetter(a,0,1))