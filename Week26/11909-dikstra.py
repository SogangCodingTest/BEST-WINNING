import heapq
import sys

n = int(sys.stdin.readline()) 
graph =[[0 for _ in range(n)]]
hq=[] # min heap
disr = [1, 0] # 오른쪽 
disc = [0, 1] # 아래
cost_save = [ [int(1e9) for _ in range(n+1)] for _ in range(n+1) ]

for i in range(n) :
    add=[0]+(list(map(int,sys.stdin.readline().split())))
    graph.append(add)

# 1≤i,j<n이라면, 상수는 A[i][j+1] 또는 A[i+1][j]로만 건너갑니다.
# i=n,1≤j<n이라면, A[i][j+1]로만 건너갑니다.
# 1≤i<n,j=n이라면 A[i+1][j]로만 건너갑니다.
# i=j=n인 경우 바로 출구 (nn)
# A[a][b]에서 A[c][d]로 건너가려면 A[a][b]>A[c][d]
# 버튼을 한 번 누르는 데에는 1원의 비용

hq.append((0,1,1)) # 비용

while hq :
    now_cost, nowr, nowc = heapq.heappop(hq)
    if cost_save[nowr][nowc] < now_cost:
        continue
    for i in range(2) :
        if 1<=nowr+disr[i]<n+1 and 1<=nowc+disc[i]<n+1 : 
            plus=0
            tmpr = nowr+disr[i]
            tmpc = nowc+disc[i]
            if cost_save[tmpr][tmpc]>=now_cost: # add
                if graph[nowr][nowc] <= graph[tmpr][tmpc] :
                        plus = graph[tmpr][tmpc]-graph[nowr][nowc]+1
                cost_save[tmpr][tmpc] = now_cost+plus
                heapq.heappush(hq,(now_cost+plus,tmpr, tmpc))

print(cost_save[n][n])