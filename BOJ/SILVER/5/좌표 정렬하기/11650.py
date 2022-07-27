import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    a = list()
    for _ in range(n):
        a.append(list(map(int, input().split())))
    a.sort(key = lambda x: (x[0], x[1]))
    for x, y in a:
        print(x, y)