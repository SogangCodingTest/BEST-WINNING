from collections import deque
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
my = [ [] for _ in range(n+1) ]

for i in range(m) : 
    s,e,p = map(int, sys.stdin.readline().split())
    my[s].append((e,p)) 
    # s에서 갈 수 있는 후보/가는데 거리 저장 

start, end = map(int, sys.stdin.readline().split()) 

q=deque()
q.append((start, 0)) # 시작 노드 일단 넣어주고 시작!
min_price = [10000000000000000001 for _ in range(n+1)] 
# 각 점에 도착하는데 걸린 최소 비용 저장 배열
min_price[start] = 0 
# start 가 동시에 end 라면 비용 0 

while q :
    ts, pri = q.popleft() # 검사할 노드, 이 노드까지 도달하는데 걸린 비용
    if min_price[ts] >= pri : 
        # 만약 검사노드의 최소 비용 저장됐던 것이,
        # 지금 비용보다 작으면 검사할 필요 ㄴㄴ 
        # 아닐 때만 검사 ㄱ (아래 수행)
        for next,price in my[ts] :
            if min_price[next]>pri+price: 
                # next 노드에 저장된 것보다 지금 들어온 값이 더 작으면
                min_price[next] = pri+price # 이걸로 최소 비용 갱신
                q.append((next, pri+price))

print(min_price[end])
