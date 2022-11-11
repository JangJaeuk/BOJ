import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]
    a_check = [[True] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                if i == j or j == k or i == k:
                    continue
                elif a[i][j] > a[i][k] + a[k][j]:
                    print(-1)
                    exit()
                elif a[i][j] == a[i][k] + a[k][j]:
                    a_check[i][j] = False

    res = 0
    for i in range(N):
        for j in range(i+1, N):
            if a_check[i][j]:
                res += a[i][j]

    print(res)
