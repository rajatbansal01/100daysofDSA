class Solution:
    def myPow(self, x: float, n: int) -> float:
        flag = bool(n >= 0)
        n = abs(n)
        ans = 1
        while n > 0:
            if n & 1:
                ans = ans * x
            x *= x
            n = n >> 1
        if flag:
            return ans 
        else:
            return 1/ans
