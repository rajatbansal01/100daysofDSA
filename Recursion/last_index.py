def lastindex(a,x,si):
    l=len(a)
    if si==l:
        return -1

    smallerlistoutput=lastindex(a,x,si+1)
    if smallerlistoutput != -1:
        return smallerlistoutput
    else:
        if a[si]==x:
            return si;
        else:
            return -1

a=[1,2,3,4,2,5]
print(lastindex(a,4,0))