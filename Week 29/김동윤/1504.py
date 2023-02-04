from collections import defaultdict 
import heapq
import sys

N,E = map(int,sys.stdin.readline().rstrip().split())
road = defaultdict(list)

for _ in range(E) :
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    road[a].append((b,c))
    road[b].append((a,c))

v1, v2 = map(int,sys.stdin.readline().rstrip().split())

# 주어진 두 정점은 반드시 통과하며 1번 정점에서 N번 정점으로 최단 거리
# 1번 - v1 - v2 - N 
# 2번 - v2 - v1 - N
# 1번, 2번 중 더 최단거리 출력

# a에서 b로 가는 최단거리를 반환값으로 돌려주는 다익스트라 알고리즘 
def dikstra(a,b ) : 
    if a==b : # 출발지와 도착지가 같은 경우 우선 처리 
        return 0
    hq = []
    min_cost = [int(1e9) for _ in range(N+1)]
    min_cost[0] = 0 # 나에게서 나로 가는 비용은 0으로 처리  
    heapq.heappush(hq,(a,0)) # 시작 정점 / 시작 비용
    while hq : 
        now_node, now_cost = heapq.heappop(hq)
        if now_cost > min_cost[now_node] :
            continue                                                                                                                                  

        for next_node, next_cost in road[now_node] : 
            if min_cost[next_node] < now_cost + next_cost :
                continue
            else : 
                min_cost[next_node] = now_cost + next_cost
                heapq.heappush(hq,(next_node, now_cost + next_cost))
                
    return(min_cost[b])

# 1번 - v1 - v2 - N 
cand1 = dikstra(1,v1 ) + dikstra(v1,v2 ) + dikstra(v2,N )
# 2번 - v2 - v1 - N
cand2 = dikstra(1,v2 ) + dikstra(v2,v1 ) + dikstra(v1,N )
# 갈 수 없는 경우
if cand1>=int(1e9) and cand2>=int(1e9):
    print(-1)
else : 
    print(min(cand1 ,cand2))
    