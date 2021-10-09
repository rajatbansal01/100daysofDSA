def multipication(m,n):
    # base case
    if n == 0:
        return 0
    return m + multipication(m,n-1)
