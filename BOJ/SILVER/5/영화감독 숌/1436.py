import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    name = 666
    cnt = 0

    while True:
        if "666" in str(name):
            cnt += 1
            if cnt == n:
                print(name)
                break
        name += 1