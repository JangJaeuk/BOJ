import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

stack=[]
point=-1

c=int(input())

for i in range(c):
    t=int(input())
    if t==0:
        stack.pop()
        point=point-1
    else:
        stack.append(t)
        point=point+1
sum=0
for i in range(len(stack)):
    sum+=stack[i]

print(sum)