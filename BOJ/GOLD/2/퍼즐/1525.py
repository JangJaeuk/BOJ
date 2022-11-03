import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def get_list_to_str(board):
    s = ''
    for i in range(3):
        for j in range(3):
            s += board[i][j]
    return s


def bfs(board):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    target = '123456780'
    puzzle_set = set()
    dq = deque()

    dq.append((board, 0))
    puzzle_set.add(board)

    while dq:
        board, cnt = dq.popleft()
        if board == target:
            return cnt

        z = board.index('0')
        tx = z // 3
        ty = z % 3

        for k in range(4):
            x = tx + dx[k]
            y = ty + dy[k]
            if 0 <= x < 3 and 0 <= y < 3:
                nz = 3 * x + y
                nboard = list(board)
                nboard[z], nboard[nz] = nboard[nz], nboard[z]
                nboard = "".join(nboard)

                if nboard not in puzzle_set:
                    dq.append((nboard, cnt + 1))
                    puzzle_set.add(nboard)
    return -1


if __name__ == "__main__":
    board = [list(input().split()) for _ in range(3)]
    board = get_list_to_str(board)
    print(bfs(board))
