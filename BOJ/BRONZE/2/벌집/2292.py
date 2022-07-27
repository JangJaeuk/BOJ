import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

a=int(input())

sum=1
m=6
count=1

while sum<a:
    sum=sum+m
    m+=6
    count+=1
    
print(count)