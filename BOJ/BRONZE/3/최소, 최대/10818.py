import sys
sys.stdin = open("input.txt", "r")

n=int(input())

l=list(map(int, input().split()))
l.sort()

print(l[0], l[len(l)-1])