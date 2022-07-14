import sys

s1 = list(sys.stdin.readline().rstrip()) 
s2 = list(sys.stdin.readline().rstrip())
# 공통 문자열은 연속 X 

dp = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]

for i in range(len(s1)+1) :
    for j in range(len(s2)+1) : 
        
        if i==0 or j==0 : # 여백 처리 
            dp[i][j] = 0

        else : 

            if s1[i-1] == s2[j-1] : # 문자가 같은 경우라면 
                dp[i][j] = dp[i-1][j-1]+1 # 내 왼쪽 대각선 (즉 내 이전 순서) 아이에 누적 1
                # 이유 : 내 이전 순서 아이에는 이미 최대 길이가 담겨있음 

            else : # 문자가 다른 경우라면 
                # 내 위와 아래 중에서 큰 것 get 
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

for d in dp : print(d)             
res = -1
for i in range(1,len(s1)+1) :
    if dp[i][len(s2)]>res: res=dp[i][len(s2)]

print(res)
