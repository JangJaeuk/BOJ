import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

stack=[]
point=-1

def cal(fun, n):
    global point
    global stack
    if fun=='push':
        stack.append(n)
        point= point+1
    elif fun=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
            point=point-1
    elif fun=='size':
        print(len(stack))
    elif fun=='empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif fun=='top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[len(stack)-1])
c=int(input())

for i in range(c):
    sentence = input().split()
    if len(sentence)==2:
        cal(sentence[0], int(sentence[1]))
    elif len(sentence)==1:
        cal(sentence[0], 0)