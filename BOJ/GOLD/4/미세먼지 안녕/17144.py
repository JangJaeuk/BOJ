import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def inc(xx, yy, orgv):
    cnt = 0
    board[xx][yy] -= orgv
    for h in range(4):
        x = xx + dx[h]
        y = yy + dy[h]
        if 0 <= x < r and 0 <= y < c and board[x][y] != -1:
            cnt += 1
            board[x][y] += orgv // 5
    orgv -= (orgv // 5) * cnt
    board[xx][yy] += orgv

def top_rot(s_i):
    for i in range(s_i-1, 0, -1):
        board[i][0] = board[i-1][0]

    board[0] = board[0][1:] + [0]

    for i in range(1, s_i+1):
        board[i-1][c-1] = board[i][c-1]

    board[s_i] = [-1, 0] + board[s_i][1:c-1]

def bottom_rot(s_i):
    for i in range(s_i + 1, r-1):
        board[i][0] = board[i+1][0]

    board[r-1] = board[r-1][1:] + [0]

    for i in range(r-1, s_i, -1):
        board[i][c-1] = board[i-1][c-1]

    board[s_i] = [-1, 0] + board[s_i][1:c-1]

if __name__ == "__main__":
    r, c, t = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(r)]
    d_list = list()
    top_s_pos = None
    bottom_s_pos = None

    for i in range(r):
        if board[i][0] == -1:
            top_s_row = i
            bottom_s_row = i+1
            break

    for _ in range(t):
        for i in range(r):
            for j in range(c):
                if board[i][j] != 0 and board[i][j] != -1:
                    d_list.append((i, j, board[i][j]))

        for d in d_list:
            x, y, ov = d
            inc(x, y, ov)
        d_list.clear()
        top_rot(top_s_row)
        bottom_rot(bottom_s_row)
    cnt = 0
    for i in range(r):
        for j in range(c):
            if board[i][j] != 0 and board[i][j] != -1:
                cnt += board[i][j]
    print(cnt)