import sys
sys.setrecursionlimit(10 ** 6)

n,m = map(int, sys.stdin.readline().rstrip().split())
# 사람의 수 / 친구 관계의 수 

node=[[] for _ in range(n)]
visited=[0 for _ in range(n)]
possible = False

def dfs(num, cnt) : # 검사하고 있는 사람, 관계의 길이
    global possible

    if possible : return
    if(cnt>=5) : possible = True; return 
    # 만약 cnt(관계의 길이)가 5이상이 되면 ABCDE 관계가 최소 하나 성립

    for relation in node[num] :
        # 자신의 노드 안에 있는 (자신과 맺어진 관계들) 검사
        if visited[relation]==0: 
            # 만약 나와 관계된 애들 중 내가 아직 찾아가지 않은 애면 찾아가봐야 함
            visited[relation]=1 # 그 아이 방문하니깐 방문 처리
            cnt+=1 # 관계의 길이 갱신
            dfs(relation, cnt) # DFS 로 관계의 길이 뻗어나갈 수 있는지 여부 검사 
            visited[relation]=0 # 가지 뻗었으니 이전 상태로 방문여부 초기회 
            cnt-=1 # 관계의 길이도 원상복귀 (초기화)

for i in range(m) : 
    a,b = map(int, sys.stdin.readline().rstrip().split())
    node[a].append(b) ; node[b].append(a) # 노드에 각자 저장해줌 

for j in range(n) : # 각 사람에 대해서 dfs 돌려준다.
        visited[j]=1
        dfs(j, 1) # 나를 포함해서 길이 세는 관계이므로 CNT 는 1부터 시작 
        visited[j]=0 # 가지 한번 뻗었으니깐 다시 원상복귀
        
if possible : print(1)
else : print(0)
