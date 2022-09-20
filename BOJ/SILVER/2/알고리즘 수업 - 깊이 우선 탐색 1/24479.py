import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(s):
    global order
    for connected_v in graph[s]:
        if visited[connected_v] == 0:
            visited[connected_v] = order
            order += 1
            dfs(connected_v)   
    
if __name__ == "__main__":
    n, m, r = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1) 
    for _ in range(m):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)
    for i in range(1, n+1):
        graph[i].sort()
    order = 1
    visited[r] = order
    order += 1
    dfs(r)
    for i in range(1, n+1):
        print(visited[i])