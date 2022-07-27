import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, k =map(int , input().split())
val=[]
sum=0
for i in range(n):
    value=int(input())
    val.append(value)
val=list(map(int, val))
for i in range(n-1,-1,-1):
    if k>=val[i]:
        sum+=k//val[i]
        k=k%val[i]
    if k==0:
        break

print(sum)