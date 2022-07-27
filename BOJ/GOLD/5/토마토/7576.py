import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    m, n = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    dq = deque()

    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                dq.append((i, j, 0))

    min_day = 0
    while dq:
        xx, yy, day = dq.popleft()
        min_day = day
        for h in range(4):
            x = xx + dx[h]
            y = yy + dy[h]
            if 0 <= x < n and 0 <= y < m and a[x][y] == 0:
                a[x][y] = 1
                dq.append((x, y, day + 1))
    
    is_all_r = True
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                is_all_r = False
                break
        if not is_all_r:
            break
    if is_all_r:
        print(min_day)
    else:
        print(-1)