import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def init_doors():
    for key in keys:
        if key == '0':
            break
        doors[ord(key) - 97] = True
        
def init_building():
    for i in range(1, h+1):
        for j in range(1, w+1):
            if building[i][j].isupper() and doors[ord(building[i][j].lower())-97]:
                building[i][j] = '.'
                
def bfs():
    res = 0
    check_building = [[False] * w for _ in range(h)]
    dq = deque()
    dq.append((0, 0))
    check_building[0][0] = True
    
    while dq:
        ti, tj = dq.popleft()
        for k in range(4):
            x = ti + dx[k]
            y = tj + dy[k]
            
            if 0 <= x < h and 0 <= y < w and building[x][y] != '*' and not check_building[x][y]:
                if building[x][y] == '.':
                    check_building[x][y] = True
                    dq.append((x, y))
                else:
                    if building[x][y] == '$':
                        res += 1
                        check_building[x][y] = True
                        dq.append((x, y))
                        building[x][y] = '.'
                    else:
                        if building[x][y].isupper():
                            if doors[ord(building[x][y].lower())-97]:
                                building[x][y] = '.'
                                check_building[x][y] = True
                                dq.append((x, y))
                        elif building[x][y].islower():
                            doors[ord(building[x][y].lower())-97] = True
                            building[x][y] = '.'
                            check_building = [[False] * w for _ in range(h)]
                            dq = deque()
                            dq.append((x, y))
    return res

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        h, w = map(int, input().split())
        building = list()
        building.append(['.'] * (w + 2))
        for _ in range(h):
            building.append(['.'] + list(input().rstrip()) + ['.'])
        building.append(['.'] * (w + 2))
        
        keys = list(input().rstrip())
        doors = [False] * 26
        init_doors()
        init_building()
        
        h, w = h+2, w+2
                             
        print(bfs())