import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    irons = input().rstrip()
    stack = list()
    answer = 0

    for i in range(len(irons)):
        if irons[i] == ')':
            stack.pop()
            # 레이저이면
            if irons[i-1] == '(':
                answer += len(stack)
            else:
                answer += 1
        else:
            stack.append(irons[i])

    print(answer)
