from collections import deque
import sys

n,m = map(int, sys.stdin.readline().split())
dict = {} # 관계 결과 담아줄 사전 (인접 노드)
q = deque() # dfs 돌려줄 스택 
res = [0 for _ in range(n+1)] # 결과 (각 경우 별로 몇 개 해킹가능한 지)

for k in range(1,n+1) :
    dict[k] = []

for _ in range(m) :
    a,b = map(int, sys.stdin.readline().split())
    dict[b].append(a)

for i in range(1,n+1) :
    visited = [0 for _ in range(n+1)]
    q.append(i)
    visited[i] = 1
    while q : 
        res[i]+=1
        now = q.pop()
        # print(q, now)
        for j in range(len(dict[now])): 
            if(visited[dict[now][j]] == 0) : 
                visited[dict[now][j]] = 1
                q.append(dict[now][j])
                    
# print(res)
# [0, 4, 4, 3, 1, 1]
max_num = max(res)

for r in range(1,n+1) : 
    if res[r] == max_num : 
        print(r, end = " ")

# defaultdict