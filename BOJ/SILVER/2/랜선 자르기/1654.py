import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    k, n = map(int, input().split())
    a = [int(input()) for _ in range(k)]
    rt = max(a)
    lt = 1
    res = 0
    while lt <= rt:
        mid = (lt + rt) // 2
        cnt = 0
        for i in a:
            cnt += i // mid
        if cnt >= n:
            res = mid
            lt = mid + 1
        else:
            rt = mid - 1
    print(res)