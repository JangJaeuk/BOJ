import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(board, visited, pos, color):
    tx, ty = pos
    board[tx][ty] = '-'
    visited[tx][ty] = True
    for k in range(4):
        x = tx + dx[k]
        y = ty + dy[k]
        if 0 <= x < N and 0 <= y < N and board[x][y] == color and not visited[x][y]:
            dfs(board, visited, (x, y), color)


if __name__ == "__main__":
    colors = ['R', 'G', 'B']
    N = int(input())
    a = list(list(map(str, input().rstrip())) for _ in range(N))
    b = [[''] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if a[i][j] == 'R' or a[i][j] == 'G':
                b[i][j] = 'R'
            else:
                b[i][j] = 'B'
    visited_a = [[False] * N for _ in range(N)]
    visited_b = [[False] * N for _ in range(N)]
    res_a = 0
    res_b = 0

    for i in range(N):
        for j in range(N):
            if a[i][j] in colors:
                res_a += 1
                if a[i][j] == 'R':
                    dfs(a, visited_a, (i, j), 'R')
                elif a[i][j] == 'G':
                    dfs(a, visited_a, (i, j), 'G')
                elif a[i][j] == 'B':
                    dfs(a, visited_a, (i, j), 'B')
            if b[i][j] in colors:
                res_b += 1
                if b[i][j] == 'R':
                    dfs(b, visited_b, (i, j), 'R')
                elif b[i][j] == 'B':
                    dfs(b, visited_b, (i, j), 'B')
    print(res_a, res_b)
