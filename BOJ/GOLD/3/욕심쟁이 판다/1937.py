import sys
sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(tx, ty):
    if dp[tx][ty]:
        return dp[tx][ty]
    dp[tx][ty] = 1
    for k in range(4):
        x = tx + dx[k]
        y = ty + dy[k]
        if 0 <= x < N and 0 <= y < N and board[tx][ty] > board[x][y]:
            dp[tx][ty] = max(dp[tx][ty], dfs(x, y) + 1)
    return dp[tx][ty]


if __name__ == "__main__":
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * N for _ in range(N)]

    max_cnt = -1
    for i in range(N):
        for j in range(N):
            max_cnt = max(max_cnt, dfs(i, j))

    print(max_cnt)
