import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

a,b,v=map(int, input().split())

len=a-b
day=(v-b-1)//len+1

print(day)