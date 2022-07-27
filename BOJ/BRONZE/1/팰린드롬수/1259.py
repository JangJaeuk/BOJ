import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    while True:
        a = input().rstrip()
        if a == '0':
            break
        if a == a[::-1]:
            print('yes')
        else:
            print('no')