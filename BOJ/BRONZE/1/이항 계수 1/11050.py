import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())

    if n == k or k == 0:
        print(1)
    else:
        nn = 1
        for i in range(n, n-k, -1):
            nn *= i
        kk = 1
        for i in range(1, k+1):
            kk *= i
        print(nn // kk)