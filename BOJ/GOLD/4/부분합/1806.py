import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    
    lt = 0
    rt = 0
    min_cnt = 2147000000
    
    tsum = a[rt]
    
    while lt <= rt:
        if tsum < s:
            rt += 1
            if rt == n:
                break
            tsum += a[rt]
        elif tsum >= s:
            min_cnt = min(min_cnt, rt - lt + 1)
            tsum -= a[lt]
            lt += 1
    
    if min_cnt == 2147000000:
        print(0)
    else:
        print(min_cnt)