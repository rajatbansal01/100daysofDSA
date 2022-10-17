class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0
        i = 0
        while i < n:
            ans =  ans ^ start

            start += 2
            i += 1
        return ans
