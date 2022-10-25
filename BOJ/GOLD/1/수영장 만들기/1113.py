import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(tx, ty, h):
    dq = deque()
    dq.append((tx, ty))
    visited[tx][ty] = True
    ac_h = 1
    is_possible = True

    while dq:
        tx, ty = dq.popleft()
        for k in range(4):
            x = tx + dx[k]
            y = ty + dy[k]
            if not (0 <= x < N and 0 <= y < M):
                is_possible = False
                continue
            if board[x][y] <= h and not visited[x][y]:
                visited[x][y] = True
                dq.append((x, y))
                ac_h += 1
    if is_possible:
        return ac_h
    else:
        return 0


if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list(map(int, input().rstrip())) for _ in range(N)]
    res = 0
    for h in range(1, 9):
        visited = [[False] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if board[i][j] <= h and not visited[i][j]:
                    res += bfs(i, j, h)
    print(res)
