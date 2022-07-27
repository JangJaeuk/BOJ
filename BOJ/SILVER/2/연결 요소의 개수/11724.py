import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def dfs(v):
    visited[v] = 1
    for i in range(n):
        if a[v][i] == 1 and visited[i] == 0:
            dfs(i)

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [[0] * n for _ in range(n)]
    visited = [0] * n
    for _ in range(m):
        s, e = map(int, input().split())
        a[s-1][e-1] = 1
        a[e-1][s-1] = 1
    
    cnt = 0
    for i in range(n):
        if visited[i] == 0:
            cnt += 1
            dfs(i)
    print(cnt)
        