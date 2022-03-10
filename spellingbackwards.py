'''
Given a string as input, use recursion to output each letter of the strings in reverse order, on a new line.

Sample Input
HELLO

Sample Output
O
L
L
E
H
'''


def spell(txt):
    ltxt=list(txt)
    l=len(ltxt)
    if l!=0:
      print(ltxt.pop(-1))
      spell(ltxt)
       
         

txt = input()
spell(txt)