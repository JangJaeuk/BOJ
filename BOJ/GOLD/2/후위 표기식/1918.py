import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    op1 = ['(', ')']
    op2 = ['*', '/']
    op3 = ['+', '-']

    inorder = input().rstrip()
    stack = list()
    res = ''

    for i in inorder:
        if i in op1:
            if i == '(':
                stack.append(i)
            else:
                while stack and stack[-1] != '(':
                    res += stack.pop()
                stack.pop()
        elif i in op2:
            while stack and stack[-1] in op2:
                res += stack.pop()
            stack.append(i)
        elif i in op3:
            while stack and (stack[-1] in op2 or stack[-1] in op3):
                res += stack.pop()
            stack.append(i)
        else:
            res += i
    while stack:
        res += stack.pop()
    print(res)