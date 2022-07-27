import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n, r, c = map(int, input().split())
    res = 0
    while n != 0:
        n -= 1
        # 1
        if r < 2 ** n and c < 2 ** n:
            res += ( 2 ** n ) * ( 2 ** n ) * 0
		# 2
        elif r < 2 ** n and c >= 2 ** n: 
            res += ( 2 ** n ) * ( 2 ** n ) * 1
            c -= ( 2 ** n )
		# 3  
        elif r >= 2 ** n and c < 2 ** n: 
            res += ( 2 ** n ) * ( 2 ** n ) * 2 
            r -= ( 2 ** n )
		# 4    
        else:
            res += ( 2 ** n ) * ( 2 ** n ) * 3  
            r -= ( 2 ** n ) 
            c -= ( 2 ** n )
    print(res)