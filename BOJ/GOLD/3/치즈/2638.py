import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def after_hour():
    visited = [[2] * m for _ in range(n)]
    dq = deque()
    cheese_cnt = 0
    dq.append((0, 0))
    
    while dq:
        tx, ty = dq.popleft()
        for k in range(4):
            x = tx + dx[k]
            y = ty + dy[k]
            if 0 <= x < n and 0 <= y < m and visited[x][y] != 0:
                if board[x][y] == 0:
                    visited[x][y] = 0
                    dq.append((x, y))
                else:
                    visited[x][y] -= 1
                    if visited[x][y] == 0:
                        board[x][y] = 0
                        cheese_cnt += 1
                        
    return cheese_cnt
                         

if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    hours = 0
    
    ah = 400
    while ah > 0:
        ah = after_hour()
        hours += 1

    print(hours - 1)