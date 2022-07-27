import sys
sys.stdin = open("input.txt", "r")

h,m=map(int, input().split())

h+=24

all=h*60+m-45

h=(all//60)%24

m=all%60

print(h, m)