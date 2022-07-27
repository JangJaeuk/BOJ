import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline 

n, m = map(int, input().split())
card_list = list(map(int, input().split()))

max_sum = -1
for i in range(len(card_list) - 2):
    for j in range(i+1, len(card_list) - 1):
        for k in range(j+1, len(card_list)):
            if max_sum < card_list[i] + card_list[j] + card_list[k] <= m:
                max_sum = card_list[i] + card_list[j] + card_list[k]

print(max_sum)