import sys
sys.stdin = open("input.txt", "r")

count=int(input())

for i in range(count):
    i_count, st=input().split()
    i_count=int(i_count)
    for j in range(len(st)):
        for k in range(i_count):
            print(st[j], end="")
    print()