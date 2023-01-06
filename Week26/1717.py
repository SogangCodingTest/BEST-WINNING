from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)
n,m = map(int, sys.stdin.readline().rstrip().split())
parent = defaultdict(int) 

for i in range(n+1) : # 0~n : n+1개의 집합
    parent[i] = i # n원소는 n이라는 집합에 속함
    
def find(x) : # x의 조상(x가 속한 집합)을 찾는다.
    if parent[x]!=x : # 만약 x의 조상이 최종 조상이 아니라면
        parent[x] = find(parent[x]) # x의 조상의 조상을 x의 조상으로 삼는다
    return parent[x] # x의 조상이 최종 조상이 될 때 비로소 최종 조상을 반환한다. 

def union(a,b) : # a,b를 합집합으로 만들어준다. (a,b 조상을 통일해준다) 
    pa  = find(a) 
    pb = find(b)
    # 둘의 조상 중 둘 중 더 작은 조상으로 통일해준다.
    if pa < pb :
        parent[pb] = pa
    else : 
        parent[pa] = pb

for i in range(m) :

    o, a, b = map(int, sys.stdin.readline().rstrip().split())
    if o==0: # UNION : 합집합 
        union(a,b)

    else : # FIND : 두 원소가 같은 집합에 포함되어 있는지를 확인 
        if find(a) == find(b) :
            print("YES")
        else : 
            print("NO")
