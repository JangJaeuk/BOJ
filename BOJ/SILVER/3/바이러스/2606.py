import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n=int(input())
m=int(input())

graph=[[0 for i in range(n+1)]for j in range(n+1)]
visit=[0 for i in range(n+1)]
for i in range(n+1):
    for j in range(n+1):
        graph[i][j]=-1

for i in range(m):
    start, end = map(int, input().split())
    graph[start][end]=1
    graph[end][start]=1

bfs=deque()

bfs.append(1)
visit[1]=1
count = 0

while bfs:
    v=bfs.popleft()
    count =count+1
    for i in range(1, n+1):
        if visit[i]==0 and graph[v][i]==1:
            bfs.append(i)
            visit[i]=1

print(count-1)