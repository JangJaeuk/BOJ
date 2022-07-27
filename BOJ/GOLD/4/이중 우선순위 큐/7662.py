import sys
from collections import deque
import heapq as hq
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        minhp = list()
        maxhp = list()
        visited = [False] * n
        for i in range(n):
            cmd, cmdn = input().split()
            cmdn = int(cmdn)
            if cmd == 'I':
                hq.heappush(minhp, (cmdn, i))
                hq.heappush(maxhp, (-cmdn, i))
                visited[i] = True
            elif cmd == 'D': 
                if cmdn == -1:
                    while minhp and not visited[minhp[0][1]]:
                        hq.heappop(minhp)
                    if minhp:
                        tmp = hq.heappop(minhp)
                        visited[tmp[1]] = False
                elif cmdn == 1:
                    while maxhp and not visited[maxhp[0][1]]:
                        hq.heappop(maxhp)
                    if maxhp:
                        tmp = hq.heappop(maxhp)
                        visited[tmp[1]] = False
        while minhp and not visited[minhp[0][1]]:
            hq.heappop(minhp)
        while maxhp and not visited[maxhp[0][1]]:
            hq.heappop(maxhp)
        if minhp and maxhp:
            print(-maxhp[0][0], minhp[0][0])
        else:
            print('EMPTY')