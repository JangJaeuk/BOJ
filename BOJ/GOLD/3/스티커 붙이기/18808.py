import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def find_position(sticker, r, c):
    dx = n - r
    dy = m - c
    start_i, start_j = -1, -1

    is_possible = True
    for i in range(dx+1):
        for j in range(dy+1):
            is_possible = True
            for ir in range(r):
                for ic in range(c):
                    if not ((board[ir+i][ic+j] == 1 and sticker[ir][ic] == 0) or board[ir+i][ic+j] == 0):
                        is_possible = False
                        break
                if not is_possible:
                    break
            # 만약 가능하다면
            else:
                start_i = i
                start_j = j
                break
        if is_possible:
            break
    return start_i, start_j


def rotate_sticker(sticker, r, c):
    new_sticker = [[0] * r for _ in range(c)]

    for i in range(r):
        for j in range(c):
            new_sticker[j][i] = sticker[r-i-1][j]

    return new_sticker, c, r


def stick(sticker, r, c, si, sj):
    for i in range(r):
        for j in range(c):
            if board[si+i][sj+j] != 1:
                board[si+i][sj+j] = sticker[i][j]


def process_stick(sticker, r, c):
    si, sj = find_position(sticker, r, c)
    cnt = 0
    while si == -1 and sj == -1 and cnt < 3:
        sticker, r, c = rotate_sticker(sticker, r, c)
        cnt += 1
        si, sj = find_position(sticker, r, c)
    if si == -1 and sj == -1:
        return
    stick(sticker, r, c, si, sj)


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]

    for _ in range(k):
        r, c = map(int, input().split())
        sticker = [list(map(int, input().split())) for _ in range(r)]
        process_stick(sticker, r, c)

    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                cnt += 1

    print(cnt)
