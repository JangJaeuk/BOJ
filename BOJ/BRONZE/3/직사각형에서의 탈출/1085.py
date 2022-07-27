import sys
sys.stdin = open("input.txt", "r")

x,y,w,h=map(int, input().split())

if w-x<x:
    wlen=w-x
else:
    wlen=x
if h-y<y:
    hlen=h-y
else:
    hlen=y

if wlen<hlen:
    print(wlen)
else:
    print(hlen)