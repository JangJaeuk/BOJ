import sys
import heapq as hq
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N, K = map(int, input().split())
    ruby = [list(map(int, input().split())) for _ in range(N)]
    bags = [int(input()) for _ in range(K)] 
    ruby.sort()
    bags.sort()
    
    ruby = deque(ruby)
    res_list = list()
    res = 0
    
    for bag in bags:
        while ruby and bag >= ruby[0][0]:
            hq.heappush(res_list, -ruby[0][1])
            ruby.popleft()
        if res_list:
            res += -hq.heappop(res_list)
        elif not ruby:
            break
    print(res) 