import sys
sys.stdin = open("input.txt", "r")
import copy
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def fish_move(t_board):
    for i in range(1, 17):
        is_there = False
        f_pos = None
        for j in range(4):
            for k in range(4):
                if t_board[j][k][0] == i:
                    is_there = True
                    f_pos = [j, k]
                    break
        if is_there:
            dir = t_board[f_pos[0]][f_pos[1]][1]
            dir -= 1
            x = f_pos[0] + dx[dir]
            y = f_pos[1] + dy[dir]
            cnt = 0
            while not(0 <= x < 4 and 0 <= y < 4 and t_board[x][y][0] != -1):
                dir += 1
                if dir > 7:
                    dir -= 8
                x = f_pos[0] + dx[dir]
                y = f_pos[1] + dy[dir]
                cnt += 1
                if cnt == 7:
                    break
            if cnt < 7:
                t_board[f_pos[0]][f_pos[1]][1] = dir + 1
                t_board[f_pos[0]][f_pos[1]][0], t_board[x][y][0] = t_board[x][y][0], t_board[f_pos[0]][f_pos[1]][0]
                t_board[f_pos[0]][f_pos[1]][1], t_board[x][y][1] = t_board[x][y][1], t_board[f_pos[0]][f_pos[1]][1]

def dfs(x, y, dir, score, t_board):
    global max_score
    t_board[x][y][0] = -1
    fish_move(t_board)
    t_board[x][y][0] = 0
    is_block = True

    for i in range(1, 5):
        xx = x + dx[dir-1]*i
        yy = y + dy[dir-1]*i
        if 0 <= xx < 4 and 0 <= yy < 4 and t_board[xx][yy][0] != 0:
            is_block = False
            dfs(xx, yy, t_board[xx][yy][1], score + t_board[xx][yy][0], copy.deepcopy(t_board))
    if is_block:
        max_score = max(max_score, score)
        return
    

if __name__ == "__main__":
    board = [[] for _ in range(4)]
    max_score = 0

    for i in range(4):
        a = list(map(int, input().split()))
        for j in range(0, 8, 2):
            board[i].append([a[j], a[j+1]])
 
    dfs(0, 0, board[0][0][1], board[0][0][0], copy.deepcopy(board))
    print(max_score)