import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    rt = max(a)
    lt = 1
    res = 0
    while lt <= rt:
        mid = (rt + lt) // 2
        len_t = 0
        for i in a:
            if i > mid:
                len_t += i-mid
        if len_t >= m:
            res = mid
            lt = mid + 1
        else:
            rt = mid - 1
    print(res)