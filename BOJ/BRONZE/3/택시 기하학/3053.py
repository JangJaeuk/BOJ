import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    r = int(input())
    PI = 3.14159265359
    
    print("%.6f" % (PI * (r ** 2)))
    print("%.6f" % (2 * (r ** 2)))
