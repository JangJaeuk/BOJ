import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        root = list(range(n+1))
        adj_list = [[] for _ in range(n+1)]
        for _ in range(m):
            n1, n2 = map(int, input().split())
        print(n-1)