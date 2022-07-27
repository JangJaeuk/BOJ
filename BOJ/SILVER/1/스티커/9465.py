import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list()
        for _ in range(2):
            a.append(list(map(int, input().split())))
        for i in range(1, n):
            if i == 1:
                a[0][i] += a[1][i-1]
                a[1][i] += a[0][i-1]
            else:
                a[0][i] += max(a[1][i-1], a[1][i-2])
                a[1][i] += max(a[0][i-1], a[0][i-2])
                
        print(max(a[0][n-1], a[1][n-1]))