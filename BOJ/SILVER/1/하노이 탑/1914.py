import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def dfs(a, b, c, k):
    if k == 1:
        print(a, c)
        return
    dfs(a, c, b, k-1)
    dfs(a, b, c, 1)
    dfs(b, a, c, k-1)


if __name__ == "__main__":
    n = int(input())

    print(2 ** n - 1)
    if n <= 20:
        dfs(1, 2, 3, n)
