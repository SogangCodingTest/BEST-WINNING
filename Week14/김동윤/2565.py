import sys
maxa = -1
n = int(sys.stdin.readline())
rel = [0 for _ in range(501)]
for i in range(n) : 
    a,b = map(int, sys.stdin.readline().split())
    rel[a] = b
    if a>maxa : maxa=a

dp = list(0 for _ in range(maxa+1))
# 케이블이 꼬이지 않은 상태 => 키 값이 증가할수록 값도 증가해야 한다. 
# (증가하는 부분 수열) 
# 가장 긴 증가하는 부분 수열의 길이 찾으면 ,
# 이 길이를 전체 케이블 갯수에서 빼주면 되는 것이지 . 
# print(rel)
for i in range(1,maxa+1) : 
    for j in range(i) : # 나보다 앞에 서있는 애들 
        if rel[i] > rel[j] : # 
            dp[i] = max(dp[i], dp[j]+1)
# print(rel[:11])
# print(dp)
print(n-(max(dp)))

# for i in range(1,n) : # 내가 지금 수열에서 만난 숫자 
#     for j in range(i) : # 나보다 앞에 있던 애들 
#         if nlis[i] > nlis[j] : # 나보다 작은 애를 만나면, 걔 뒤에서 내가 이어질 수 있으므로 그때 비교 
#             dp[i] = max(dp[i], dp[j]+1)
# print(max(dp))