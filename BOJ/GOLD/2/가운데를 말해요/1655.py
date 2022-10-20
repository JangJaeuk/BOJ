import sys
import heapq as hq
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    lq = list()
    rq = list()
    for _ in range(n):
        t = int(input())
        if len(lq) == len(rq):
            hq.heappush(lq, -t)
        else:
            hq.heappush(rq, t)

        if lq and rq and -lq[0] > rq[0]:
            t1 = hq.heappop(lq)
            t2 = hq.heappop(rq)

            hq.heappush(lq, -t2)
            hq.heappush(rq, -t1)

        print(-lq[0])
