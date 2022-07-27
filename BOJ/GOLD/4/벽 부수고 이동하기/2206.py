# 3차원 리스트로 접근하기
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(xx, yy, z):
    dq = deque()
    dq.append((xx, yy, z))
    
    while dq:
        r, c, bk = dq.popleft()
        if r == n - 1 and c == m - 1:
            return visited[r][c][bk]
        for h in range(4):
            x = r + dx[h]
            y = c + dy[h]
            if 0 <= x < n and 0 <= y < m:
                if board[x][y] == 1 and bk == 0:
                    visited[x][y][1] = visited[r][c][0] + 1
                    dq.append((x, y, 1))
                elif board[x][y] == 0 and visited[x][y][bk] == 0:
                    visited[x][y][bk] = visited[r][c][bk] + 1
                    dq.append((x, y, bk))
    return -1
    
if __name__ == "__main__":
    n, m = map(int, input().split())
    board = list()
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1
    for _ in range(n):
        board.append(list(map(int, input().rstrip())))


    print(bfs(0, 0, 0))
