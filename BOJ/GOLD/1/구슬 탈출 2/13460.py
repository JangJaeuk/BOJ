import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(rp, bp):
    count = 0            
    dq = deque()
    check_set = set()
    dq.append((rp, bp))
    check_set.add((rp, bp))
    
    while dq:
        for _ in range(len(dq)):
            trp, tbp = dq.popleft()
            if count > 10:
                return -1
            if board[trp[0]][trp[1]] == 'O':
                return count
            for k in range(4):
                rp_x = trp[0]
                rp_y = trp[1]
                bp_x = tbp[0]
                bp_y = tbp[1]
                
                while True:
                    rp_x += dx[k]
                    rp_y += dy[k]
                    if board[rp_x][rp_y] == '#':
                        rp_x -= dx[k]
                        rp_y -= dy[k]
                        break
                    if board[rp_x][rp_y] == 'O':
                        break
                while True:
                    bp_x += dx[k]
                    bp_y += dy[k]
                    if board[bp_x][bp_y] == '#':
                        bp_x -= dx[k]
                        bp_y -= dy[k]
                        break
                    if board[bp_x][bp_y] == 'O':
                        break
                if board[bp_x][bp_y] == 'O':
                    continue
                if rp_x == bp_x and rp_y == bp_y:
                    if abs(rp_x - trp[0]) + abs(rp_y - trp[1]) > abs(bp_x - tbp[0]) + abs(bp_y - tbp[1]):
                        rp_x -= dx[k]
                        rp_y -= dy[k]
                    else:
                        bp_x -= dx[k]
                        bp_y -= dy[k]
                r_rp = (rp_x, rp_y)
                r_bp = (bp_x, bp_y)
                
                if not (r_rp, r_bp) in check_set:
                    dq.append((r_rp, r_bp))
                    check_set.add((r_rp, r_bp))
        count += 1
    return -1

if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(n)]
    
    rp = (-1, -1)
    bp = (-1, -1)
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                rp = (i, j)
            if board[i][j] == 'B':
                bp = (i, j)
    
    print(bfs(rp, bp))
                  