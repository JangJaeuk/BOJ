import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n=int(input())

p=list(input().split())
p=list(map(int, p))

sum=0
bin=0

for i in range(n-1):
    for j in range(i+1, n):
        if p[i]>p[j]:
            bin=p[i]
            p[i]=p[j]
            p[j]=bin

for i in range(n):
    for j in range(i+1):
        sum+=p[j]

print(sum)