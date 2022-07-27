import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    res = 0

    for i in range(1, n+1):
        a = list(map(int, str(i)))
        res = i + sum(a)
        if res == n:
            print(i)
            break
        if i == n:
            print(0)