#no of zeros
def func(m):
    if m==0:
        return 1
    l=m%10
    n=m//10
    if n==0:
        return 0
    s=func(n)
    if l==0:
        return s+1
    else:
        return s

m=int(input('Enter the no: '))
print(func(m))
