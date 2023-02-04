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

def union(a,b) : # a,b를 합집합으로 만들어준다. (a,b 조상의 조상들을 통일해준다) 
    if find(a)  < find(b) :
        parent[find(b)] = find(a)
        # 주의점 
        # parent[b] = find(a) 가 아닌
        # parent[find(b)] =  find(a) 다.
        # 나의 조상의 조상을 합치고자 하는 애의 조상과 동일하게 해야함
    else : 
        parent[find(a)] = find(b)

for i in range(m) :

    o, a, b = map(int, sys.stdin.readline().rstrip().split())
    if o==0: # UNION : 합집합 
        union(a,b)

    else : # FIND : 두 원소가 같은 집합에 포함되어 있는지를 확인 
        if find(a) == find(b) :
            print("YES")
        else : 
            print("NO")
