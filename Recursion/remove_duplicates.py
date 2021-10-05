def removeDup(s):
    l = len(s)
    if l == 0 or l == 1:
        return s
    if s[0] == s[1]:
        return removeDup(s[1:])
    else:
        return s[0] + removeDup(s[1:])
