import sys
sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(tx, ty):
    if tx == N-1 and ty == M-1:
        return 1

    if dp[tx][ty] == -1:
        dp[tx][ty] = 0
        for k in range(4):
            x = tx + dx[k]
            y = ty + dy[k]
            if 0 <= x < N and 0 <= y < M and roadmap[tx][ty] > roadmap[x][y]:
                dp[tx][ty] += dfs(x, y)
    return dp[tx][ty]


if __name__ == "__main__":
    N, M = map(int, input().split())
    roadmap = [list(map(int, input().split())) for _ in range(N)]
    dp = [[-1] * M for _ in range(N)]
    print(dfs(0, 0))
    for road in dp:
        print(road)
