import sys
sys.stdin = open("input.txt", "r")

a,b=input().split()
a=list(a)
b=list(b)
a.reverse()
b.reverse()
a=int("".join(a))
b=int("".join(b))
if a>b:
    print(a)
else:
    print(b)