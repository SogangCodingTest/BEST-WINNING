import heapq
import sys

v,e = map(int, sys.stdin.readline().rstrip().split())
edge = []
answer = []

for _ in range(e) :
    a,b,c = map(int, sys.stdin.readline().rstrip().split())
    heapq.heappush(edge, (c,a,b)) # 가장 낮은 가중치의 간선들 

parent = [0 for _ in range(v+1)]
# parent = [i for i in range(V+1)]

for i in range(1,v+1) :
    parent[i] = i

def find(x) :
    if parent[x]!=x : 
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b) :
    if a<b : 
        parent[find(b)] = find(a)
    else : 
        parent[find(a)] = find(b)


while edge : 
    now_cost, now_a, now_b = heapq.heappop(edge)
    # 가장 최소 비용의 간선 꺼내기 & 
    # 구성하는 두 노드가 싸이클을 이루지 않으면 얘네 둘을 이어주기 
    if find(now_a)!=find(now_b) : 
        # find 를 했을 때 다르면 사이클은 발생하지 않는다. 
        union(now_a,now_b)
        answer.append(now_cost)

print(sum(answer))

