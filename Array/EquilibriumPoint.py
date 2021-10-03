
class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
   def equilibriumPoint(self,a, n):
        if n==1:
            return 1
        x=0#start
        y=n-1#end
        #left sum
        s1=0
        #right sum
        s2=0
        for i in range(n):
            s1+=a[i]
        while x<y and y > 0:
            #checking if z is Equilibrium Point or not.
            z=a[y-1]
            
            #left sum before z
            s1=s1-a[y]-z
            
            #right sum after z
            s2+=a[y]
            
            #if both sum are equal return.
            if s1==s2:
                return y
            else:
                s1+=z
            y-=1
        return -1


#{ 
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()