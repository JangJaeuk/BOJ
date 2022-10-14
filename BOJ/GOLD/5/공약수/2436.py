import sys
import math
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def get_gcd(a, b):
    p = a % b
    if p == 0:
        return b
    else:
        return get_gcd(b, p)


if __name__ == "__main__":
    gcd, lcm = map(int, input().split())
    div = lcm // gcd  # a * b

    for a in range(int(math.sqrt(div)), 0, -1):
        b = div // a

        if div % a == 0 and get_gcd(a, b) == 1:
            print(a * gcd, b * gcd)
            break
