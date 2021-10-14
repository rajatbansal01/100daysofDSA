"""
Replace pi with 3.14
Given a string s and replace all occurances of pi with 3.14.

l = len(s)

Approach
Base Case:

if l == 0 or l == 1 then return the s as it is.

Induction Step and Induction Hypothesis:

Will be true for next part of string as well. There are two cases.

Case 1: if first two characters of s are 'pi' then return replacePi(s[2:])+'3.14'.

Case 2: if first two chars are not pi then return return replacePi(s[1:])+s[0].
"""

def replacepi(s):
    if len(s)==0 or len(s)==1:
        return s
    if s[0]=='p'and s[1]=='i':
        smalloutput=replacepi(s[2:])
        return '3.14'+smalloutput
    else:
        smalloutput=replacepi(s[1:])
        return s[0]+smalloutput
print(replacepi('pi*r*r'))
## output = 3.14*r*r

# test 2
print(replacepi('hellopipipir'))
## output = 'hello3.143.143.14r'
