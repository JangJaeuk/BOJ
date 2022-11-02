import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    dp = [[0] * M for _ in range(N)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    max_cnt = 0

    def dfs(tx, ty, cnt):
        global max_cnt
        max_cnt = max(max_cnt, cnt)
        for k in range(4):
            x = tx + dx[k] * int(board[tx][ty])
            y = ty + dy[k] * int(board[tx][ty])
            if 0 <= x < N and 0 <= y < M and board[x][y] != 'H' and cnt + 1 > dp[x][y]:
                if visited[x][y]:
                    print(-1)
                    exit()
                else:
                    visited[x][y] = True
                    dp[x][y] += 1
                    dfs(x, y, cnt + 1)
                    visited[x][y] = False
    dfs(0, 0, 0)
    print(max_cnt + 1)
