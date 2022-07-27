import sys
sys.stdin = open("input.txt", "r")

a=int(input())
b=int(input())
c=int(input())

mul=list(map(int,str(a*b*c)))
li=[0]*10
for i in range(10):
    for j in range(len(mul)):
        if i==mul[j]:
            li[i]+=1
for i in li:
    print(i)