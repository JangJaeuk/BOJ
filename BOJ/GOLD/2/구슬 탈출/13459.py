import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(red_p, blue_p):
    dq = deque()
    check_set = set()
    count = 0
    
    dq.append((red_p, blue_p))
    check_set.add((red_p, blue_p))
    while dq:
        for _ in range(len(dq)):
            t_red_p, t_blue_p = dq.popleft()
            if count > 10:
                print(0)
                return
            if a[t_red_p[0]][t_red_p[1]] == 'O':
                print(1)
                return
            for i in range(4):
                red_x = t_red_p[0]
                red_y = t_red_p[1]
                blue_x = t_blue_p[0]
                blue_y = t_blue_p[1]  
            
                while True:
                    red_x += dx[i]
                    red_y += dy[i]
                    if a[red_x][red_y] == '#':
                        red_x -= dx[i]
                        red_y -= dy[i]
                        break
                    elif a[red_x][red_y] == 'O':
                        break

                while True:
                    blue_x += dx[i]
                    blue_y += dy[i]
                    if a[blue_x][blue_y] == '#':
                        blue_x -= dx[i]
                        blue_y -= dy[i]
                        break
                    elif a[blue_x][blue_y] == 'O':
                        break
                    
                if a[blue_x][blue_y] == 'O':
                    continue
                
                if (red_x, red_y) == (blue_x, blue_y):
                    if abs(red_x - t_red_p[0]) + abs(red_y - t_red_p[1]) > abs(blue_x - t_blue_p[0]) + abs(blue_y - t_blue_p[1]):
                        red_x -= dx[i]
                        red_y -= dy[i]
                    else:
                        blue_x -= dx[i]
                        blue_y -= dy[i]
                if ((red_x, red_y), (blue_x, blue_y)) not in check_set:
                    dq.append(((red_x, red_y), (blue_x, blue_y)))
                    check_set.add(((red_x, red_y), (blue_x, blue_y)))
        count += 1
    print(0)

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [list(input().rstrip()) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if a[i][j] == 'R':
                red_p = (i, j)
            if a[i][j] == 'B':
                blue_p = (i, j)
                
    bfs(red_p, blue_p)