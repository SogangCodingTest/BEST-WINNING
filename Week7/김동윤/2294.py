import sys

n,k = map(int, sys.stdin.readline().rstrip().split()) 
# 각각의 동전은 몇 개라도 사용
# 동전의 가치는 100,000보다 작거나 같은 자연수
price =[1000001 for _ in range(k+1)] # 가격만큼 배열 만들어
price[0]=0

for co in range(n) :
    value = int(sys.stdin.readline().rstrip()) #동전 가격
    for i in range(value, k+1) : # 내 가치 이상부터  ~
        price[i] = min(price[i], price[i-value]+1)

# 마지막 칸이 갱신안된 상태면 -1 
if price[-1]!=1000001 : print(price[-1])
else : print(-1)
