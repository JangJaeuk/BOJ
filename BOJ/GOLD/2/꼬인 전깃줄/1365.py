import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    li = list(map(int, input().split()))
    res = [0]

    for i in range(n):
        lt = 0
        rt = len(res) - 1

        while lt <= rt:
            mid = (lt + rt) // 2

            if res[mid] > li[i]:
                rt = mid - 1
            else:
                lt = mid + 1

        if rt >= len(res) - 1:
            res.append(li[i])
        else:
            res[rt + 1] = li[i]

    print(n - len(res) + 1)
