import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    a = list()
    op_list = list()
    stack = list()
    for i in range(n):
        a.append(int(input()))

    num = 1
    is_possible = True
    for i in range(n):
        while num <= a[i]:
            stack.append(num)
            op_list.append('+')
            num += 1
        while stack and stack[-1] != a[i]:
            stack.pop()
            op_list.append('-')
        if stack and stack[-1] == a[i]:
            stack.pop()
            op_list.append('-')
        else:
            is_possible = False
            break
    if is_possible:
        for op in op_list:
            print(op)
    else:
        print('NO')