def func(s):
    l=len(s)
    if l==1:
        return int(s[0])
    a=func(s[1:])
    b=int(s[0])*(10**(l-1))
    return b+a

s=input('Enter no: ')
print(func(s))
