import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    k = int(input())

    lt, rt = 0, k

    res = 0

    while lt <= rt:
        mid = (lt + rt) // 2

        cnt = 0
        for i in range(1, n+1):
            cnt += min(mid // i, n)

        if cnt >= k:
            res = mid
            rt = mid - 1
        else:
            lt = mid + 1

    print(res)
