# 나머지 분배법칙 (a * b) % c = ((a % c) * (b % c)) % c

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def calc(a, n, c):
    if n == 1:
        return a % c
    else:
        t = calc(a, n // 2, c)
        if n % 2 == 0:
            return (t * t) % c
        else:
            return (t * t * a) % c
        

if __name__ == "__main__":
    a, n, c = map(int, input().split())
    print(calc(a, n, c))