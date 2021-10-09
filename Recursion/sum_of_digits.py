def sum_digits(n):
    # base case
    if n // 10 == 0:
        return n
    return n%10 + sum_digits(n//10)
 


# sample input
sum_digits(12)
# ans = 3
