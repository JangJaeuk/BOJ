import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    n_list = [0] * 8001

    sum_n = 0
    for _ in range(n):
        k = int(input())
        sum_n += k
        if k < 0:
            k = 4000 - k
        n_list[k] += 1
    if sum_n >= 0:
        avg_n = int((sum_n / n) + 0.5)
    else:
        avg_n = int((sum_n / n) - 0.5)
    
    cnt = 0
    mid_n = 0
    mid_break = False
    max_bin_v = max(n_list)
    bin_list = list()
    max_bin = 0
    n_list2 = list()
    for i in range(8000, 4000, -1):
        if n_list[i] != 0:
            n_list2.append(4000-i)
            cnt += n_list[i]
            if cnt >= n // 2 + 1 and not mid_break:
                mid_n = 4000 - i
                mid_break = True
            if n_list[i] == max_bin_v:
                bin_list.append(4000-i)
    for i in range(4001):
        if n_list[i] != 0:
            n_list2.append(i)
            cnt += n_list[i]
            if cnt >= n // 2 + 1 and not mid_break:
                mid_n = i
                mid_break = True
            if n_list[i] == max_bin_v:
                bin_list.append(i)
    if len(bin_list) >= 2:
        max_bin = bin_list[1]
    else:
        max_bin = bin_list[0]
    bum = n_list2[-1] - n_list2[0]

    print(avg_n)
    print(mid_n)
    print(max_bin)
    print(bum)