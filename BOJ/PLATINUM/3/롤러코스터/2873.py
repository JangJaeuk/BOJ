import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    r, c = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(r)]

    if r % 2 == 1:
        print('R' * (c-1)+('D'+'L' * (c-1)+'D'+'R' * (c-1)) * (r//2))
    elif c % 2 == 1:
        print('D' * (r-1)+('R'+'U' * (r-1)+'R'+'D' * (r-1)) * (c//2))
    else:
        min_v = 2147000000
        min_p = None
        is_even = True
        for i in range(r):
            for j in range(c):
                if (i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0):
                    if board[i][j] < min_v:
                        min_v = board[i][j]
                        min_p = [i, j]
                        if i % 2 == 0:
                            is_even = True
                        else:
                            is_even = False
        res = ''
        m_r = min_p[0]
        if not is_even:
            m_r -= 1
        for i in range(m_r):
            if i % 2 == 0:
                res += 'R' * (c-1)
            else:
                res += 'L' * (c-1)
            res += 'D'
        for j in range(min_p[1]):
            if j % 2 == 0:
                res += 'DR'
            else:
                res += 'UR'
        for j in range(min_p[1], c-1):
            if j % 2 == 1:
                res += 'RU'
            else:
                res += 'RD'
        for i in range(m_r + 2, r):
            res += 'D'
            if i % 2 == 0:
                res += 'L' * (c-1)
            else:
                res += 'R' * (c-1)
        print(res)