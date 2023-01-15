import heapq
import sys

v,e = map(int, sys.stdin.readline().rstrip().split())
edge = []
answer = []

for _ in range(e) :
    a,b,c = map(int, sys.stdin.readline().rstrip().split())
    heapq.heappush(edge, (c,a,b))

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
    if find(now_a)!=find(now_b) : # find 를 했을 때 다르면 사이클은 발생하지 않는다. 
        union(now_a,now_b)
        answer.append(now_cost)

print(sum(answer))

