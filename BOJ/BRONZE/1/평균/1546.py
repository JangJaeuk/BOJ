import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

count=int(input())

score=list(map(int, input().split()))
score.sort()
result=0
for i in range(count):
    result+=(score[i]/score[count-1])*100
result/=count
print(result)