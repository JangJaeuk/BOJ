import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n, m, b = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    res_t = 2147000000
    res_h = -1

    for h in range(257):
        max = 0
        min = 0
        for i in range(n):
            for j in range(m):
                if a[i][j] < h:
                    min += (h - a[i][j])
                else:
                    max += (a[i][j] - h)
        cur_b = max + b
        if cur_b < min:
            continue
        time = 2 * max + min
        if time <= res_t:
            res_t = time
            res_h = h
    print(res_t, res_h)