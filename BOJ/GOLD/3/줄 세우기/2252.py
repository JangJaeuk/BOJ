import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
from collections import deque

def topology():
    dq = deque()
    
    for i in range(1, n+1):
        if degrees[i] == 0:
            dq.append(i)
            
    while dq:
        t = dq.popleft()
        print(t, end=' ')
        for cv in graph[t]:
            degrees[cv] -= 1
            if degrees[cv] == 0:
                dq.append(cv)

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    degrees = [0] * (n+1)
    
    for _ in range(m):
        s, e = map(int, input().split())
        graph[s].append(e)
        degrees[e] += 1
        
    topology()