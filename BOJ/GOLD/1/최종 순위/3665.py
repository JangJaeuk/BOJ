import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        ranks = list(map(int, input().split()))
        graph = [[] for _ in range(N + 1)]
        degrees = [0] * (N + 1)
        for i, rank in enumerate(ranks):
            graph[rank] = ranks[i + 1:]
        M = int(input())
        for _ in range(M):
            v1, v2 = map(int, input().split())
            if v1 in graph[v2]:
                graph[v1].append(v2)
                graph[v2].remove(v1)
            elif v2 in graph[v1]:
                graph[v2].append(v1)
                graph[v1].remove(v2)
        for i in range(1, N+1):
            for v in graph[i]:
                degrees[v] += 1

        s_v = -1
        for i in range(1, N+1):
            if degrees[i] == 0:
                s_v = i

        is_possible = True
        is_clear = True
        res = list()

        if s_v == -1:
            is_possible = False
        else:
            dq = deque()
            dq.append(s_v)

            while dq:
                v = dq.popleft()
                z_cnt = 0
                res.append(v)

                for c_v in graph[v]:
                    degrees[c_v] -= 1
                    if degrees[c_v] == 0:
                        z_cnt += 1
                        dq.append(c_v)

                is_z = True
                for degree in degrees:
                    if degree != 0:
                        is_z = False
                        break

                if z_cnt == 0 and not is_z:
                    is_possible = False
                    break
                elif z_cnt > 1:
                    is_clear = False
                    break

        if not is_possible:
            print('IMPOSSIBLE')
        elif not is_clear:
            print('?')
        else:
            print(*res)
