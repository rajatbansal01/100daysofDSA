def reverse(s1,s2):
    if len(s1) ==1:
        return
    while len(s1) != 1:
        data=s1.pop()
        s2.append(data)
    ele=s1[len(s1)-1]
    s1.pop()
    while len(s2) != 0:
        data=s2.pop()
        s1.append(data)
    reverse(s1,s2)
    s1.append(ele)
s1=list()
s2=list()
s1.append(1)
s1.append(2)
s1.append(3)
s1.append(4)
reverse(s1,s2)
while len(s1) != 0:
    print(s1.pop())


