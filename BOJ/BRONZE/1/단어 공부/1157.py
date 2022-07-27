import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

a=input().rstrip()
di=[0]*26
for i in range(len(a)):
    for j in range(26):
        if ord(a[i])==97+j or ord(a[i])==65+j:
            di[j]+=1
            break
max=0
index=-1
is_t=False
for i in range(26):
    if max<di[i]:
        max=di[i]
        index=i+65
        is_t=False
    elif max==di[i]:
        is_t=True
    
if not is_t:
    print(chr(index))
else:
    print("?")