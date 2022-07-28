import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
    
    
def bfs(xx, yy, b_c):
    dq = deque()
    dq.append((xx, yy, b_c))
    
    while dq:
        tx, ty, brick_count = dq.popleft()
        if tx == n-1 and ty == m-1:
            return visited[tx][ty][brick_count]
        for h in range(4):
            x = tx + dx[h]
            y = ty + dy[h]
            if 0 <= x < n and 0 <= y < m:
                if board[x][y] == 1 and brick_count < k and visited[x][y][brick_count + 1] == 0:
                    visited[x][y][brick_count + 1] = visited[tx][ty][brick_count] + 1
                    dq.append((x, y, brick_count + 1))
                elif board[x][y] == 0 and visited[x][y][brick_count] == 0:
                    visited[x][y][brick_count] = visited[tx][ty][brick_count] + 1
                    dq.append((x, y, brick_count))
    return -1
    
if __name__ == "__main__":
    n, m, k = map(int, input().split())
    board = [list(map(int, input().rstrip())) for _ in range(n)]
    visited = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]
    
    visited[0][0] = [1] * (k+1)
    
    print(bfs(0, 0, 0))
    