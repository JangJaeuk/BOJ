import sys
from collections import Counter
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    counter = Counter(list(map(int, input().split())))
    m = int(input())
    a = list(map(int, input().split()))
    for i in a:
        if i in counter:
            print(counter[i], end=' ')
        else:
            print(0, end=' ')