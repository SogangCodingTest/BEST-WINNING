import sys

n = int(sys.stdin.readline())
tpsave=[]
tpsave.append((0,0)) # 인덱스 0 인 자리 단순 채움용
dp = [0 for _ in range(n+2)]

for j in range(n) :
    t,p = map(int, sys.stdin.readline().split())
    # 걸리는 상담 시간, 보상 가격 순으로 저장 
    tpsave.append((t,p))

# 1일차부터 n일차까지 돌아줄 것임 
for i in range(1,n+1) :
    # (1) 만약 상담하기로 선택하면 비교해주기
    target = i+tpsave[i][0]
    if target<=n+1 :  # n+1도 포함시켜줘야 한다 ..
        # 왜냐면 주어진 n=7이고 그때 소요 시간이 1일이면 상담 가능임
        # 7일 하루를 쓰는 거니깐,
        # 그리고 이는 8일에 기록돼야 하므로 target 은 n+1까지 가능
        dp[target] = max(dp[target], tpsave[i][1]+dp[i])

    # (2) 선택 안하는 경우 (while 문을 안써도 되는 이유)
    dp[i+1] = max(dp[i+1], dp[i]) 

# n+1 일째 되는 날 퇴사하니깐 n+1일 째의 보상을 출력
print(dp[n+1])
