c,t = input().split()
c = int(c)
t = float(t)

if t>c+0.5 and c%5==0:
    print("%.2f"%(t-c-0.5))
else:
    print("%.2f"%t)
    