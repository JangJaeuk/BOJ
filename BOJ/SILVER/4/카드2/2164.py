import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
a = list(range(1, n+1))
a = deque(a)

while len(a) > 1:
    a.popleft()
    a.append(a.popleft())

print(a.popleft())