# 이 코드의 시간 초과 이유가 뭘까..
# ㅋㅋㅋㅋㅋ 하.. 힙에 넣을 때 순서를 잘못넣었네

import sys
import heapq as hq
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

INF = 2147000000

def dijkstra(start):
    dis[start] = 0
    hq.heappush(heap, (0, start))
    
    while heap:
        w, v = hq.heappop(heap)
        if dis[v] < w:
            continue
        
        for next_v, added_w in graph[v]:
            next_w = w + added_w
            if next_w < dis[next_v]:
                dis[next_v] = next_w
                hq.heappush(heap, (next_w, next_v))

if __name__ == "__main__":
    v, e = map(int, input().split())
    k = int(input())
    graph = [[] for _ in range(v+1)]
    dis = [INF] * (v+1)
    heap = list()
    
    for _ in range(e):
        sv, ev, w = map(int, input().split())
        graph[sv].append((ev, w))
    
    dijkstra(k)
    
    for i in range(1, v+1):
        if dis[i] == INF:
            print('INF')
        else:
            print(dis[i])
    
    