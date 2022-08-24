import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    res_list = list()
    index_list = [0] * n
    lis = list()
    
    for i in range(n):
        if not res_list or a[i] > res_list[-1]:
            res_list.append(a[i])
            index_list[i] = len(res_list) - 1
        else:
            lt = 0
            rt = len(res_list) - 1
            while lt <= rt:
                mid = (lt + rt) // 2
                if a[i] > res_list[mid]:
                    lt = mid + 1
                else:
                    rt = mid - 1
            res_list[rt + 1] = a[i]
            index_list[i] = rt + 1
            
    t = max(index_list)
    max_len_index = index_list.index(t)
    
    while max_len_index >= 0:
        lis.append(a[max_len_index])
        t -= 1
        if t < 0:
            break
        while t >= 0 and t != index_list[max_len_index]:
            max_len_index -= 1 
            
    lis = lis[::-1]
    print(len(res_list))
    print(*lis)