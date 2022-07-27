import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

count=int(input())

l=list(map(int, input().split()))
c=count
for i in range(count):
    if l[i]==1:
        c-=1
    else:
        for j in range(2,l[i]):
            if l[i]%j==0:
                c-=1
                break
print(c)