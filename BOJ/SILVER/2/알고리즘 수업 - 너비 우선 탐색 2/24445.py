import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
    
def bfs(s):
    dq = deque()
    dq.append(s)
    order = 1
    
    while dq:
        t = dq.popleft()
        if visited[t] == 0:
            visited[t] = order
            order += 1
            for connected_v in graph[t]:
                if visited[connected_v] == 0:
                    dq.append(connected_v)
    
if __name__ == "__main__":
    n, m, r = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1) 
    for _ in range(m):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)
    for i in range(1, n+1):
        graph[i].sort(reverse = True)
    bfs(r)
    for i in range(1, n+1):
        print(visited[i])