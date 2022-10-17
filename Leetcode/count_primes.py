class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        array = [1] * (n)
        array[0], array[1] = 0, 0
        for i in range(2,int(n**0.5)+1):
            if array[i]:
                array[i*i:n:i] = [0] * ((n-1-i*i)//i + 1)
                print((n-1-i*i)//i + 1)
        return sum(array)
