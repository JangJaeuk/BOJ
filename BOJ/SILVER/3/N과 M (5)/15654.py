import sys
from itertools import permutations
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    p = permutations(a, k)
    for item in p:
        for i in item:
            print(i, end=' ')
        print()