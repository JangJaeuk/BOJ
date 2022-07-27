import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(100000)
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(i, j):
    a[i][j] = 0
    for h in range(4):
        x = i + dx[h]
        y = j + dy[h]
        if 0 <= x < n and 0 <= y < m and a[x][y] == 1:
            dfs(x, y) 
 
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        m, n, k = map(int, input().split())
        a = [[0] * m for _ in range(n)]
        for _ in range(k):
            c, r = map(int, input().split())
            a[r][c] = 1
        
        cnt = 0
        
        for i in range(n):
            for j in range(m):
                if a[i][j] == 1:
                    cnt += 1
                    dfs(i, j)
        print(cnt)
                
        