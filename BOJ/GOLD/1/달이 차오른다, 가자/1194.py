import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(N)]

    def get_start_point():
        for i in range(N):
            for j in range(M):
                if board[i][j] == '0':
                    return i, j

    def bfs(p):
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        visited = [[[0] * 64 for _ in range(M)] for _ in range(N)]
        dq = deque()
        total_cnt = -1
        x, y = p
        dq.append((x, y, 0))
        visited[x][y][0] = 1

        while dq:
            tx, ty, tz = dq.popleft()
            if board[tx][ty] == '1':
                total_cnt = visited[tx][ty][tz] - 1
                break
            for k in range(4):
                x = tx + dx[k]
                y = ty + dy[k]
                # 범위를 벗어났거나 방문했거나 벽일 경우
                if not (0 <= x < N and 0 <= y < M and visited[x][y][tz] == 0 and board[x][y] != '#'):
                    continue
                # 열쇠인 경우
                if board[x][y] in ['a', 'b', 'c', 'd', 'e', 'f']:
                    z = tz | (1 << (ord(board[x][y]) - ord('a')))
                    if visited[x][y][z] == 0:
                        visited[x][y][z] = visited[tx][ty][tz] + 1
                        dq.append((x, y, z))
                # 문인 경우
                elif board[x][y] in ['A', 'B', 'C', 'D', 'E', 'F']:
                    if tz & (1 << (ord(board[x][y]) - ord('A'))):
                        visited[x][y][tz] = visited[tx][ty][tz] + 1
                        dq.append((x, y, tz))
                # 길인 경우
                else:
                    visited[x][y][tz] = visited[tx][ty][tz] + 1
                    dq.append((x, y, tz))
        return total_cnt

    p = get_start_point()
    print(bfs(p))
