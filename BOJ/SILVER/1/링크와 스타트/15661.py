import sys
from itertools import combinations
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(n)]
    m_list = list(range(n))
    
    min_dis = 2147000000
    
    for i in range(1, n//2 + 1):
        for c_m_list in combinations(m_list, i):
            link_list = list(c_m_list)
            soft_list = list(set(m_list) - set(link_list))
            
            link_score = 0
            soft_score = 0
    
            for t1, t2 in combinations(link_list, 2):
                link_score += (s[t1][t2] + s[t2][t1])
         
            for t1, t2 in combinations(soft_list, 2):
                soft_score += (s[t1][t2] + s[t2][t1])
            
            min_dis = min(min_dis, abs(link_score - soft_score))
        
    print(min_dis)          
            