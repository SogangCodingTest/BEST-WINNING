import sys

n = int(sys.stdin.readline()) 
graph =[[0 for _ in range(n+1)]]
cost_save = [ [0 for _ in range(n+1)] for _ in range(n+1) ]

for i in range(n) :
    add=[0]+(list(map(int,sys.stdin.readline().split())))
    graph.append(add)

# 1≤i,j<n이라면, 상수는 A[i][j+1] 또는 A[i+1][j]로만 건너갑니다.
# i=n,1≤j<n이라면, A[i][j+1]로만 건너갑니다.
# 1≤i<n,j=n이라면 A[i+1][j]로만 건너갑니다.
# i=j=n인 경우 바로 출구 (nn)
# A[a][b]에서 A[c][d]로 건너가려면 A[a][b]>A[c][d]
# 버튼을 한 번 누르는 데에는 1원의 비용

for i in range(1,n+1) : # 왼쪽이랑 위만 검사하면 됨 
    for j in range(1,n+1) : 
        cost_up = int(1e9)
        cost_left = int(1e9)

        if i-1<1 and j-1<1 : #왼쪽이나 위가 존재하지 않음 
            continue 

        # 위 가능하면 
        if i-1>=1 :
            cost_up = cost_save[i-1][j]
            # 위의 아이(graph[i-1][j])가 나(graph[i][j])보다 커야지 그냥 내려옴
            # 내가 더 크다면 위의 아이를 나보다 크게 만들어줄 비용 발생 
            if graph[i][j] >= graph[i-1][j] : 
                cost_up+=(graph[i][j]-graph[i-1][j])+1
                
        # 왼쪽 가능하면 
        if j-1>=1 :
            cost_left = cost_save[i][j-1]
            if graph[i][j] >= graph[i][j-1] : 
                cost_left+=(graph[i][j]-graph[i][j-1])+1
                
        # 둘 중 더 작은 애를 내 비용으로 
        cost_save[i][j] = min(cost_up, cost_left)

print(cost_save[n][n])
