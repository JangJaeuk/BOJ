import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

a = int(input())
box = 0
while True:
    if (a % 5) == 0:
        box +=(a//5)
        print(box)
        break
    a -= 3
    box += 1
    if a < 0:
        print("-1")
        break