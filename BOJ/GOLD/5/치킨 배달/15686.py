import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline  

def DFS(L, s):
    global min_d
    if L == m:
        sum_d = 0
        for i in range(hsize):
            dis = 2147000000
            for j in range(m):
                x = abs(hl[i][0] - res[j][0])
                y = abs(hl[i][1] - res[j][1])
                tmp = x + y
                if tmp < dis:
                    dis = tmp
            sum_d += dis
        if sum_d < min_d:
            min_d = sum_d
    else:
        for i in range(s, csize):
            res[L] = cl[i]
            DFS(L+1, i+1)
            
if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    hl = list()
    cl = list()
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1:
                hl.append((i, j))
            elif a[i][j] == 2:
                cl.append((i, j))

    min_d = 2147000000
    hsize = len(hl)
    csize = len(cl)
    res = [0] * m
    DFS(0, 0)
    print(min_d)