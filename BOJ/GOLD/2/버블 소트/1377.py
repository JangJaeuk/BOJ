import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    a = list()
    for i in range(N):
        t = int(input())
        a.append((t, i))
    a.sort()
    cnt = -2147000000
    for i in range(N):
        cnt = max(cnt, a[i][1] - i)
    print(cnt + 1)
