import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

a=list(str(input().rstrip()))
result=0
checkindex=0
isSum=True
for i in range(len(a)):
    if a[i]=='-' or a[i]=='+':
        if isSum:
            result+=int(''.join(a[checkindex:i]))
        else:
            result-=int(''.join(a[checkindex:i]))
        checkindex=i+1
        if a[i]=='-':
            if isSum:
                isSum=False
    if i==len(a)-1:
        if isSum:
            result+=int(''.join(a[checkindex:i+1]))
        else:
            result-=int(''.join(a[checkindex:i+1]))
print(result)