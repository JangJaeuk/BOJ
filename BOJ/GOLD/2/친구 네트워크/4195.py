import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return
    parent[b] = a
    visited[a] += visited[b]


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        parent = dict()
        visited = dict()

        for _ in range(n):
            f1, f2 = input().split()
            if f1 not in parent:
                parent[f1] = f1
                visited[f1] = 1
            if f2 not in parent:
                parent[f2] = f2
                visited[f2] = 1

            union(f1, f2)
            print(visited[find(f1)])
