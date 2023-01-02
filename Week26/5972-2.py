from collections import defaultdict
import heapq
import sys
# N개의 헛간 / 소들의 길 M개
n,m = map(int,sys.stdin.readline().split()) 
mini_hq= []
rel = defaultdict(list) # defaultdict 리스트로 초기화 
# 다익스트라는 초기 비용을 무한대로 초기화 
visit_answer = [int(1e9) for _ in range(n+1)]
for i in range(m) : 
    a,b,c = map(int,sys.stdin.readline().split())
    heapq.heappush(rel[a] , (c,b)) # 관계 기록
    heapq.heappush(rel[b] , (c,a))
# < 초기화 > : 시작은 1번 노드, 이때 비용은 0원 (1번->1번은 0의 비용) 
mini_hq.append((0,1)) # 비용 , 노드 로 집어넣어줌


while mini_hq :
# 검사대상이 존재할 동안 돌려준다.
    
    now_cost , now_node = heapq.heappop(mini_hq) 
    # 가장 비용이 작은 노드부터 검사 => 그래야 비용이 작은 순으로 채워짐
    # 한번 방문한 now_node 는 재방문 X => 먼저 방문된 now_node는 비용 가장 작았던 순이므로
    # 한번 pop 됐던 now_node는 이미 visit_answer에 반영돼있음 

    for tmp_cost, tmp_node in rel[now_node] : 
        # 나랑 이어져있는 노드들 검사 
        # 기존 : 이것도 min heap 으로 pop 해주었음
        # 변경 : for 문으로 검사 
        if visit_answer[tmp_node] > now_cost+tmp_cost :
        # 방문 겸 정답 리스트에 기록된 비용 VS 현재노드 거치는 비용 중 더 작은 것 선택 
            visit_answer[tmp_node] = now_cost+tmp_cost
            heapq.heappush(  mini_hq, (now_cost+tmp_cost , tmp_node))
        # 갱신된 값의 노드를 넣어주기

print(visit_answer[n])
