import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def after_hour():
    visited = [[False] * m for _ in range(n)]
    dq = deque()
    cheese_cnt = 0
    
    dq.append((0, 0))
    
    while dq:
        tx, ty = dq.popleft()
        for k in range(4):
            x = tx + dx[k]
            y = ty + dy[k]
            if 0 <= x < n and 0 <= y < m and not visited[x][y]:
                if board[x][y] == 0:
                    visited[x][y] = True
                    dq.append((x, y))
                elif board[x][y] == 1:
                    visited[x][y] = True
                    board[x][y] = 0
                    cheese_cnt += 1
                    
    return cheese_cnt            

if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    cheese_cnt_list = list()
    
    ah = 400
    while ah > 0:
        ah = after_hour()
        cheese_cnt_list.append(ah)
        
    print(len(cheese_cnt_list) - 1)
    print(cheese_cnt_list[-2])
    