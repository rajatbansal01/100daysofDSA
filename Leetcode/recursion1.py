from logging import lastResort
import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')


def remove_dups(s):
    l = len(s)
    if l == 0:
        return s
    if s[0] == s[1]:
        return remove_dups(s[1:])
    else:
        return s[0] + remove_dups(s[1:])


s = input()
x = input()

print(remove_dups(s))
