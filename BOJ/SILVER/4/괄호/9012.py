import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    
    for _ in range(n):
        a = input().rstrip()
        stack = list()
        
        is_right = True
        for i in a:
            if i == '(':
                stack.append(i)
            elif i == ')':
                if (stack and stack[-1] == ')') or len(stack) == 0:
                    is_right = False
                    break
                else:
                    stack.pop()
        if is_right:
            if stack:
                print('NO')
            else:
                print('YES')
        else:
            print('NO')