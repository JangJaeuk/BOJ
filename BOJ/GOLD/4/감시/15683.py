import sys
from copy import deepcopy
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

INF = 2147000000
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

cctv_cates = [
    [],
    [[0], [1], [2], [3]],
    [(0, 2), (1, 3)],
    [(0, 1), (1, 2), (2, 3), (3, 0)],
    [(3, 0, 1), (0, 1, 2), (1, 2, 3), (2, 3, 0)],
    [(0, 1, 2, 3)]
]


def fill_range(board, x, y, cate_dir):
    for k in cate_dir:
        tx = x + dx[k]
        ty = y + dy[k]

        while 0 <= tx < N and 0 <= ty < M:
            if board[tx][ty] == 6:
                break
            if board[tx][ty] == 0:
                board[tx][ty] = -1
            tx += dx[k]
            ty += dy[k]

    return board


def dfs(board, cctv_list, curr):
    global min_div

    if curr == len(cctv_list):
        div = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0:
                    div += 1
        min_div = min(min_div, div)
        return

    cctv_num, x, y = cctv_list[curr]
    for cctv_dir in cctv_cates[cctv_num]:
        new_board = deepcopy(board)
        new_board = fill_range(new_board, x, y, cctv_dir)
        dfs(new_board, cctv_list, curr + 1)


if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    min_div = INF
    cctv_list = list()

    for i in range(N):
        for j in range(M):
            if board[i][j] in [1, 2, 3, 4, 5]:
                cctv_list.append((board[i][j], i, j))

    dfs(board, cctv_list, 0)
    print(min_div)
