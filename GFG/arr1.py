arr = [21, 24, 56, 65, 34, 54, 76, 32, 23, 45, 21, 23, 25]
n=len(arr)
x = 23
k = 5
r = 1
last = arr[n-n%k:]
if x not in last:
    r=0
for i in range(n//k-1):
    if x not in arr[i*k:(i+1)*k]:
        r=0
print(r)

print("Rajat")
    
