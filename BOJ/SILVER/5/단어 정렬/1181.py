import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    a = list()
    for _ in range(n):
        a.append(input().rstrip())
    a = list(set(a))
    a.sort(key = lambda x: (len(x), x))
    for i in a:
        print(i)