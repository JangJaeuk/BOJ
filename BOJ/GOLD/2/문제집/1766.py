import sys
import heapq as hq
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    degrees = [0] * (n+1)

    hl = list()

    for _ in range(m):
        sv, ev = map(int, input().split())
        graph[sv].append(ev)
        degrees[ev] += 1

    for i in range(1, n+1):
        if degrees[i] == 0:
            hq.heappush(hl, i)

    while hl:
        t = hq.heappop(hl)
        print(t, end=' ')
        for cv in graph[t]:
            degrees[cv] -= 1
            if degrees[cv] == 0:
                hq.heappush(hl, cv)
