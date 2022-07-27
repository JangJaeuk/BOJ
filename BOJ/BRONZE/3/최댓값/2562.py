import sys
sys.stdin = open("input.txt", "r")

index=1
max=0
for i in range(9):
    a=int(input())
    if i==0:
        max=a
    else:
        if a>max:
            max=a
            index=i+1
print(max)
print(index)