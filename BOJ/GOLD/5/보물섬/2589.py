import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    dq = deque()
    dq.append((x, y))
    visited = [[-1] * m for _ in range(n)]
    visited[x][y] = 0
    dis = 0

    while dq:
        tx, ty = dq.popleft()
        for h in range(4):
            xx = tx + dx[h]
            yy = ty + dy[h]
            if 0 <= xx < n and 0 <= yy < m and board[xx][yy] == 'L' and visited[xx][yy] == -1:
                dq.append((xx, yy))
                visited[xx][yy] = visited[tx][ty] + 1
                dis = max(dis, visited[xx][yy])
    return dis

if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [input().rstrip() for _ in range(n)]
    max_dis = -1

    for i, row in enumerate(board):
        for j, item in enumerate(row):
            if item == 'L':
                d = bfs(i, j)
                max_dis = max(d, max_dis)

    print(max_dis)