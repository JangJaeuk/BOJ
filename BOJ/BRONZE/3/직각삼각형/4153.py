import sys
sys.stdin = open("input.txt", "r")

while True:
    a,b,c=map(int, input().split())
    if a==0 and b==0 and c==0:
        break
    t=[a,b,c]
    t.sort()
    
    if (t[0]**2)+(t[1]**2)==t[2]**2:
        print("right")
    else:
        print("wrong")