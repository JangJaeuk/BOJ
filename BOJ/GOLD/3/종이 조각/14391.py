import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [list(map(int, input().rstrip())) for _ in range(n)]
    max_sum = 0
    
    # 비트마스크로 2^(n*m) 경우의 수 고려
    for i in range(1 << n * m):
        total_sum = 0
        # 가로합 계산
        for row in range(n):
            row_sum = 0
            # 한 행에 있는 연속된 종이 조각 숫자 구하기
            for col in range(m):
                # 리스트를 1차원 리스트로 생각하여 인덱스 접근
                linear_index = m * row + col
                # 만약 해당열이 가로이면 이어 붙임
                if i & (1 << linear_index) != 0:
                    row_sum = row_sum * 10 + a[row][col]
                # 해당열이 세로이면 총합에 가로합을 더해주고 가로합 초기화
                else:
                    total_sum += row_sum
                    row_sum = 0
            total_sum += row_sum
            
        # 세로합 계산
        for col in range(m):
            col_sum = 0
            for row in range(n):
                linear_index = m * row + col
                if i & (1 << linear_index) == 0:
                    col_sum = col_sum * 10 + a[row][col]
                else:
                    total_sum += col_sum
                    col_sum = 0
            total_sum += col_sum
        
        max_sum = max(max_sum, total_sum)
        
    print(max_sum)
            
