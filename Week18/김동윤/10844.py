import sys
# 1~9 12 89 98 
# 1 2 3 4 5 6 7 8 9 - (+) 10 ## # 01 
n = int(sys.stdin.readline().strip())

dp = [[0] * 10 for _ in range(n + 1)] # 0 1 2 3 4 5 6 7 8 9

# 한자리수는 0을 제외하고(0이 시작으로 올 수 없음) 
# dp[1][0] 자리는 0으로 그대로 냅둬 
# 모두 하나 뿐이므로 1(개)로 초기화

for r in range(1,10):
    dp[1][r] = 1 

for i in range(2, n+1) :
    for j in range(10) :
        if j==0 : # 뒷자리가 0 이면 앞에 1만 옴
            dp[i][0] = dp[i-1][1] # dp[i][j] = dp[i][j+1]
            
        elif j==9 :
            dp[i][9] = dp[i-1][8] # dp[i][j] = dp[i][j-1]

        else : 
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % 1000000000)
for d in dp :
    print(d)