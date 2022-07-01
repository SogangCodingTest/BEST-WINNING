import sys
sys.setrecursionlimit(10**6)
n,m = map(int, sys.stdin.readline().rstrip().split())

node = [[] for _ in range(n+1)] # 직원 n명의 직속상사 담는 리스트
sangsa = list(map(int, sys.stdin.readline().rstrip().split()))
compliment = [0 for _ in range(n+1)]

def dfs(num) : # 내 직속부하들에게도 점수를 상속해주기 
    for k in node[num] : # num의 직속부하들에 대해서 
            compliment[k]+=compliment[num] # 내가 가진 칭찬을 더해주고 
            dfs(k) # 걔네도 칭찬 나눠주도록 보내기 

for i in range(1,n+1) :
    if sangsa[i-1]!=-1 : 
        node[sangsa[i-1]].append(i) 
        # 각 상사마다 가지는 직속 부하들을 담아주기 

# 칭찬의 총 갯수 M마다 dfs를 돌면 시간초과가 
# 사람 i에 대한 칭찬을 미리 모두 더한 뒤
# dfs를 돌려야 한다 (출처 : https://leesh111112.tistory.com/124)

for j in range(m) : # 먼저 각 사람이 받은 칭찬 저장 후 
    happyPerson, w = map(int, sys.stdin.readline().rstrip().split())
    compliment[happyPerson]+= w 

dfs(1) # 사장님부터 칭찬 상속 검사 돌리면 된다. 

compliment = compliment[1::]
for i in compliment :
    print(i, end=" ")
    