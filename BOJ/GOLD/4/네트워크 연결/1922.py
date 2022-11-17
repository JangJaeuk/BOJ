import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def find(v):
    if roots[v] != v:
        roots[v] = find(roots[v])
    return roots[v]


def union(v1, v2):
    if v1 < v2:
        roots[v2] = v1
    else:
        roots[v1] = v2


if __name__ == "__main__":
    N = int(input())
    M = int(input())
    edges = list()
    roots = [x for x in range(N+1)]
    for _ in range(M):
        edges.append(tuple(map(int, input().split())))
    edges.sort(key=lambda x: x[2])
    edges = deque(edges)
    min_w = 0
    while edges:
        v1, v2, w = edges.popleft()
        v1 = find(v1)
        v2 = find(v2)
        if v1 != v2:
            union(v1, v2)
            min_w += w
    print(min_w)
