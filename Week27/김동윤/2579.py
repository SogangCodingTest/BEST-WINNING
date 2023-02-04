import sys

n = int( sys.stdin.readline().rstrip() )
st = [0]
dp = [0 for _ in range(n+1)]
for _ in range(n) :
    st.append(int( sys.stdin.readline().rstrip() ))

dp[1] = st[1]
if n>1 : 
    dp[2] = dp[1]+st[2] # n이 1인 경우 예외 발생 (index error)

for i in range(3,n+1) :
    # (1) 내 두 계단 전에서 두계단을 올라온 경우 (두 칸 전)
    # (2) 3계단 이전에서 2계단을 오르고 바로 이전 계단에서 부터 현재 계단까지 연속 (한 칸 전)
    dp[i] = max(dp[i-2], dp[i-3]+st[i-1]) + st[i]
print(dp[n])
