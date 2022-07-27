import sys
sys.setrecursionlimit(10**9)
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def dfs(x, y, ptype):
    global cnt
    if x == n-1 and y == n-1:
        cnt += 1
        return

    if ptype == 1 or ptype == 3:
        if y + 1 < n:
            if a[x][y+1] == 0:
                dfs(x, y+1, 1)
    if ptype == 2 or ptype == 3:
        if x + 1 < n:
            if a[x+1][y] == 0:
                dfs(x+1, y, 2)
    if ptype == 1 or ptype == 2 or ptype == 3:
        if x + 1 < n and y + 1 < n:
            if a[x+1][y] == 0 and a[x][y+1] == 0 and a[x+1][y+1] == 0:
                dfs(x+1, y+1, 3)
                
if __name__ == "__main__":
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    dfs(0, 1, 1)
    print(cnt)