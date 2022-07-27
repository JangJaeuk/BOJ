import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def bfs(x, y):
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    
    dq = deque()
    dq.append((x, y, 0))
    check_set = set()
    check_set.add((x, y))

    while dq:
        t = dq.popleft()
        if board[t[0]][t[1]] == 1:
            return t[2]
        for h in range(8):
            xx = t[0] + dx[h]
            yy = t[1] + dy[h]
            if 0 <= xx < n and 0 <= yy < m and (xx, yy) not in check_set:
                dq.append((xx, yy, t[2] + 1))
                check_set.add((xx, yy))

if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    max_cnt = 0

    for i in range(n):
        for j in range(m):
            if board[i][j] != 1:
                max_cnt = max(max_cnt, bfs(i, j))
    print(max_cnt)