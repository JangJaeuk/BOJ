import sys
from itertools import combinations
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(range(1, n))
    p = combinations(a, k)
    for item in p:
        for i in item:
            print(i, end=' ')
        print()