import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    l = int(input())
    a = input().rstrip()

    sum_n = 0
    for i in range(l):
        sum_n += (ord(a[i])-96)*(31**i)
    print(sum_n % 1234567891)