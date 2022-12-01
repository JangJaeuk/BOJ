import sys
import heapq as hq
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

INF = 2147000000


def dijkstra(start, end):
    dis[start] = 0
    pq = list()
    hq.heappush(pq, (0, start))

    while pq:
        d, node = hq.heappop(pq)

        if dis[node] < d:
            continue

        for connected_node in graph[node]:
            c_n, c_d = connected_node
            if d + c_d < dis[c_n]:
                dis[c_n] = d + c_d
                hq.heappush(pq, (dis[c_n], c_n))

    print(dis[end])


if __name__ == "__main__":
    N = int(input())
    graph = [[] for _ in range(N + 1)]
    dis = [INF] * (N + 1)
    M = int(input())
    for _ in range(M):
        s, e, d = map(int, input().split())
        graph[s].append((e, d))

    ts, te = map(int, input().split())
    dijkstra(ts, te)
