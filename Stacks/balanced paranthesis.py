def balancepar(string):
    s=[]
    for i in  string:
        if i in "({[":
            s.append(i)
        elif i == ")":
            if(not s or s[-1]!="("):
                return False
            s.pop()
        elif i == "}":
            if(not s or s[-1]!="{"):
                return False
            s.pop()
        elif i == "]":
            if(not s or s[-1]!="["):
                return False
            s.pop()
    if (len(s)==0):
        return True
    else:
        return False
string=input()
ans=balancepar(string)
print(ans)
