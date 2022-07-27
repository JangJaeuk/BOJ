import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

count = int(input())

for i in range(count):
    h, w, n = map(int, input().split())
    if n%h==0:
        floor = h
        ads = n//h
        print(f'{floor*100+ads}')
    else:
        floor = n%h
        ads = n//h+1
        print(f'{floor*100+ads}')