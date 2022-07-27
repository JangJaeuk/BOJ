import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    while True:
        a = input().rstrip()
        if a == '.':
            break
        stack = list()
        for i in a:
            if i == '(' or i == '[':
                stack.append(i)
            elif i == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(i)
                    break
            elif i == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(i)
                    break
        if stack:
            print('no')
        else:
            print('yes')