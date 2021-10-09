def palindrome(s):
    l = len(s)
    if l == 0 or l == 1:
        return True
    return (s[0] == s[l-1]) and palindrome(s[1:l-1])
