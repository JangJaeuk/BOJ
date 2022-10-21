import sys
import heapq as hq
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def dijkstra(start):
    qlist = list()
    hq.heappush(qlist, (0, 0, start))

    time_list = [[INF] * (T + 1) for _ in range(N + 1)]

    while qlist:
        cost, time, now = hq.heappop(qlist)

        if time_list[now][time] < cost:
            continue

        for building in graph[now]:
            m_time = time + building[1]
            m_cost = cost + building[2]

            if T < m_time or M < m_cost:
                continue

            if time_list[building[0]][m_time] > m_cost:
                time_list[building[0]][m_time] = m_cost
                hq.heappush(qlist, (m_cost, m_time, building[0]))

    return min(time_list[N])


if __name__ == "__main__":
    N = int(input())
    T, M = map(int, input().split())
    L = int(input())
    graph = [[] for _ in range(N+1)]
    INF = 2147000000
    for _ in range(L):
        v1, v2, time, cost = map(int, input().split())
        graph[v1].append((v2, time, cost))
        graph[v2].append((v1, time, cost))
    R = dijkstra(1)
    print(R if R != INF and R <= M else -1)
