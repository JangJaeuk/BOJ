import sys
sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    def is_possible_attach(x, y, size):
        for i in range(size):
            for j in range(size):
                if paper[x + i][y + j] == 0:
                    return False
        if paper_cnt_list[size] > 0:
            return True
        else:
            return False

    def attach_paper(x, y, size):
        paper_cnt_list[size] -= 1
        for i in range(size):
            for j in range(size):
                paper[x + i][y + j] = 0

    def detach_paper(x, y, size):
        paper_cnt_list[size] += 1
        for i in range(size):
            for j in range(size):
                paper[x + i][y + j] = 1

    def dfs(x, y, cnt):
        global total_cnt

        while paper[x][y] == 0:
            y += 1
            if y == SIZE:
                y = 0
                x += 1
                if x == SIZE:
                    total_cnt = min(total_cnt, cnt)
                    return
        if cnt >= total_cnt:
            return
        for k in range(5, 0, -1):
            if x + k <= SIZE and y + k <= SIZE and is_possible_attach(x, y, k):
                attach_paper(x, y, k)
                dfs(x, y, cnt + 1)
                detach_paper(x, y, k)

    SIZE = 10
    INF = 2147000000
    paper = [list(map(int, input().split())) for _ in range(SIZE)]
    paper_cnt_list = [0, 5, 5, 5, 5, 5]
    total_cnt = INF
    dfs(0, 0, 0)

    if total_cnt == INF:
        print(-1)
    else:
        print(total_cnt)
