import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def dfs(start_v):
    print(start_v, end=' ')
    for v in ad_list[start_v]:
        if not visited[v]:
            visited[v] = True
            dfs(v)


def bfs(start_v):
    dq = deque()
    visited[start_v] = True
    dq.append(start_v)
    
    while dq:
        t = dq.popleft()
        print(t, end=' ')
        for v in ad_list[t]:
            if not visited[v]:
                visited[v] = True
                dq.append(v)

if __name__ == "__main__":
    n, m, s = map(int, input().split())
    ad_list = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    for _ in range(m):
        sv, ev = map(int, input().split())
        ad_list[sv].append(ev)
        ad_list[ev].append(sv)
    for i in range(1, n+1):
        ad_list[i].sort()
    
    visited[s] = True
    dfs(s)
    print()
    for i in range(n+1):
        visited[i] = False
    bfs(s)