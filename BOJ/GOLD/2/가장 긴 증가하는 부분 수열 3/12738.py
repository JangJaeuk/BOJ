import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    res_list = [0]
    
    for i in range(n):
        if a[i] > res_list[-1]:
            res_list.append(a[i])
        else:
            lt = 0
            rt = len(res_list) - 1
            while lt <= rt:
                mid = (lt + rt) // 2
                if a[i] > res_list[mid]:
                    lt = mid + 1
                else:
                    rt = mid - 1
            res_list[rt+1] = a[i]
    print(len(res_list)-1)