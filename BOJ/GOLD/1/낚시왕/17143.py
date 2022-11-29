import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dx = (-1, 1, 0, 0)
dy = (0, 0, 1, -1)


def get_closest_shark(board, c, R):
    for i in range(R):
        if board[i][c]:
            return i
    return -1


def get_moved_shark(board, R, C, cr, cc):
    d, s, z = board[cr][cc][0]

    for _ in range(s):
        cr += dx[d]
        cc += dy[d]

        if not (0 <= cr < R and 0 <= cc < C):
            cr -= dx[d]
            cc -= dy[d]
            # 위쪽 방향이었을 경우
            if d == 0:
                cr += 1
                d = 1
            # 아래쪽 방향이었을 경우
            elif d == 1:
                cr -= 1
                d = 0
            # 오른쪽 방향이었을 경우
            elif d == 2:
                cc -= 1
                d = 3
            # 왼쪽 방향이었을 경우
            elif d == 3:
                cc += 1
                d = 2
    # 이동된 좌표와 상어 반환
    return cr, cc, (d, s, z)


def get_moved_sharks_board(board, R, C):
    new_board = [[[] for _ in range(C)] for _ in range(R)]

    for i in range(R):
        for j in range(C):
            # 상어가 있으면
            if board[i][j]:
                moved_i, moved_j, shark = get_moved_shark(board, R, C, i, j)
                new_board[moved_i][moved_j].append(shark)

    for i in range(R):
        for j in range(C):
            # 상어가 한 칸에 두마리 이상있으면
            if len(new_board[i][j]) >= 2:
                # 상어 크기 내림차순으로 정렬
                new_board[i][j].sort(key=lambda x: -x[2])
                # 제일 큰 상어만 남을때까지 나머지 상어 제거
                while len(new_board[i][j]) > 1:
                    new_board[i][j].pop()

            board[i][j] = new_board[i][j]


if __name__ == "__main__":
    R, C, M = map(int, input().split())
    board = [[[] for _ in range(C)] for _ in range(R)]
    total_sum = 0
    for _ in range(M):
        r, c, s, d, z = map(int, input().split())
        r -= 1
        c -= 1
        d -= 1
        board[r][c].append((d, s, z))
    for c in range(C):
        # 해당 열에서 땅에 가장 가까운 상어 찾기
        row = get_closest_shark(board, c, R)
        if 0 <= row < 4:
            total_sum += board[row][c][0][2]
            board[row][c].remove(board[row][c][0])

        # 상어 이동!
        get_moved_sharks_board(board, R, C)
    print(total_sum)
