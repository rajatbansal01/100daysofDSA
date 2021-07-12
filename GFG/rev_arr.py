s="Rajat"
s=list(s)
def reverse(s, start, end):
    while start<end:
        s[start],s[end]=s[end], s[start]
        start+=1
        end-=1
    return(s)

print("".join(reverse(s,0,4)))