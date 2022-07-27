# 플로이드 워셜 문제 무난

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

INF = 2147000000

if __name__ == "__main__":
    n = int(input())
    graph = [[INF] * (n+1) for _ in range(n+1)]
    m = int(input())
    for i in range(1, n+1):
        graph[i][i] = 0
    for _ in range(m):
        sv, ev, w = map(int, input().split())
        graph[sv][ev] = min(graph[sv][ev], w)
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
                
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] == INF:
                print(0, end = ' ')
            else:
                print(graph[i][j], end = ' ')
        print()