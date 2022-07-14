import sys
n = int(sys.stdin.readline().rstrip())
dp = 1  # 사자를 한 마리도 배치하지 않는 경우도 하나의 경우의 수
chk = 2

# 처음에 리스트로 저장했었는데 그럼 메모리초과 -> 매번 갱신시키기 
for i in range(1,n+1) : 
    olddp = dp
    dp = dp + chk #dp[i-1](이전 아이) + chk[i-1](체크)
    chk = chk + olddp*2
    # chk[i] = chk[i-1] + dp[i-1]*2
print(dp%9901)

