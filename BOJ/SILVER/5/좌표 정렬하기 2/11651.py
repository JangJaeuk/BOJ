import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n=int(input())
nList=[]

for i in range(n):
    nList.append(list(map(int, input().split())))
nList.sort(key=lambda x: (x[1], x[0]))

for i in range(n):
    print(nList[i][0], nList[i][1])