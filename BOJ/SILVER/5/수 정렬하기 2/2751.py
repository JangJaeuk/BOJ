import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    arr = list()
    for _ in range(n):
        arr.append(int(input()))
    arr.sort()
    for i in arr:
        print(i)