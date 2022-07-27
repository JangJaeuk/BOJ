import sys
sys.stdin = open("input.txt", "r")

count=int(input())
n=list(map(int, input()))
sum=0
for i in range(count):
    sum+=n[i]
print(sum)