import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def gcd(a, b):
    p = a % b
    if p == 0:
        return b
    else:
        return gcd(b, p)

if __name__ == "__main__":
    a, b = map(int, input().split())
    r1 = gcd(a, b)
    r2 = a*b // r1
    print(r1)
    print(r2)