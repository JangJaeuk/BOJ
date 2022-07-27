import sys
sys.stdin = open("input.txt", "r")

count=int(input())

for i in range(count):
    li=list(input())
    bonus=0
    score=0
    
    for j in range(len(li)):
        if li[j]=='O':
            bonus+=1
            score+=bonus
        else:
            bonus=0
    print(score)