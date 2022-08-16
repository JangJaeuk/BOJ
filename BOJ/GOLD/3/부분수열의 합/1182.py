import sys
from itertools import combinations
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    
    res = 0
    
    for i in range(1, n+1):
        for com in combinations(a, i):
            if sum(com) == s:
                res += 1
                
    print(res)