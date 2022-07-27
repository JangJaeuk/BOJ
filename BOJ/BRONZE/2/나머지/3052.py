import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

li=[]
for i in range(10):
    a=int(input())
    a%=42
    li.append(a)
li=set(li)
print(len(li))