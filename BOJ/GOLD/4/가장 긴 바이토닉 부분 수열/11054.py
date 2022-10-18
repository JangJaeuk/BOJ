import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    a_reverse = a[::-1]

    lis = [1] * n
    lds = [1] * n

    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j]:
                lis[i] = max(lis[i], lis[j] + 1)
            if a_reverse[i] > a_reverse[j]:
                lds[i] = max(lds[i], lds[j] + 1)

    lds = lds[::-1]

    max_len = 0

    for i in range(n):
        max_len = max(max_len, lis[i] + lds[i])

    print(max_len - 1)
