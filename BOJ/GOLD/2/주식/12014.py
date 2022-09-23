import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    t = int(input())
    for t_index in range(1, t+1):
        n, k = map(int, input().split())
        table = list(map(int, input().split()))
        lis = [0]
        
        for i in range(n):
            if table[i] > lis[-1]:
                lis.append(table[i])
            else:
                lt = 0
                rt = len(lis) - 1
                while lt <= rt:
                    mid =(lt + rt) // 2
                    
                    if lis[mid] < table[i]:
                        lt = mid + 1
                    else:
                        rt = mid - 1
                lis[rt + 1] = table[i]
        print('Case #%d' % (t_index))
        if len(lis) >= k:
            print(1)
        else:
            print(0)