import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    a = list()
    for _ in range(n):
        age, name = input().split()
        age = int(age)
        a.append((age, name))
    
    a.sort(key = lambda x: x[0])
    for age, name in a:
        print(age, name)