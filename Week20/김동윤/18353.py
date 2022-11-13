import sys
n = int(sys.stdin.readline())
lis = list(map(int, sys.stdin.readline().split()))
dp = [1 for _ in range(n)]

for i in range(1, n) : # dp[i] 를 결정할거야
    for j in range(0, i): 
        # 이전 애들 싹dp[0]~dp[i-1] 을 간볼거야

        # 앞에 애들 중 내가 이어받을 수 있는 경우는
        #(1) 나보다 큰 애 뒤에 오기 (2) 나부터 시작하기
        if lis[i]<lis[j]: # 이전 애가 나보다 높은 경우
        # 나부터 시작 vs 내 이전애 이어받기
            dp[i] = max(dp[i], dp[j]+1) 
#print(dp)
print(n-max(dp))

