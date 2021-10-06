def replacechar(s,a,b):
    if len(s)==0:
        return s
    smalloutput=replacechar(s[1:],a,b)
    if s[0]==a:
        return b+smalloutput
    else:
        return s[0]+smalloutput
print(replacechar('adab','d','b'))
