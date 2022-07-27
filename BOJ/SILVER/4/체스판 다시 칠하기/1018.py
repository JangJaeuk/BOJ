import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [list(input().rstrip()) for _ in range(n)]

    min_change = 2147000000

    for i in range(n-7):
        cnt = 0
        for j in range(m-7):
            cnt1 = 0
            for k in range(8):
                for h in range(8):
                    if k % 2 == 0 and h % 2 == 0 and a[k+i][h+j] != 'W':
                        cnt1 += 1
                    elif k % 2 == 0 and h % 2 == 1 and a[k+i][h+j] != 'B':
                        cnt1 += 1
                    elif k % 2 == 1 and h % 2 == 0 and a[k+i][h+j] != 'B':
                        cnt1 += 1
                    elif k % 2 == 1 and h % 2 == 1 and a[k+i][h+j] != 'W':
                        cnt1 += 1           
            cnt2 = 0
            for k in range(8):
                for h in range(8):
                    if k % 2 == 0 and h % 2 == 0 and a[k+i][h+j] != 'B':
                        cnt2 += 1
                    elif k % 2 == 0 and h % 2 == 1 and a[k+i][h+j] != 'W':
                        cnt2 += 1
                    elif k % 2 == 1 and h % 2 == 0 and a[k+i][h+j] != 'W':
                        cnt2 += 1
                    elif k % 2 == 1 and h % 2 == 1 and a[k+i][h+j] != 'B':
                        cnt2 += 1 
            cnt = min(cnt1, cnt2)
            min_change = min(min_change, cnt)
    print(min_change)