import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == "__main__":
    n, m = map(int, input().split())
    maze = [list(map(int, input().rstrip())) for _ in range(n)]

    dq = deque()
    dq.append((0, 0, 1))
    maze[0][0] = 0
    res = 0

    while dq:
        tx, ty, cnt = dq.popleft()
        if tx == n-1 and ty == m-1:
            res = cnt
            break
        for k in range(4):
            x = tx + dx[k]
            y = ty + dy[k]
            if 0 <= x < n and 0 <= y < m and maze[x][y] == 1:
                dq.append((x, y, cnt + 1))
                maze[x][y] = 0

    print(res)
