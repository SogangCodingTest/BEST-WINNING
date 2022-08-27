from collections import deque
import sys
sys.setrecursionlimit(10**5)

n,m = map(int, sys.stdin.readline().split())
people = []
for i in range(n+1) :
    people.append([]) 
    
def find_parent(target) :
    cand = deque()
    cand.append(target)
    while cand : 
        now = cand.popleft()
        for idx in range(len(people[now])) : 
            if visit[people[now][idx]]==0 :
                visit[people[now][idx]] = visit[now]+1
                cand.append(people[now][idx])
                
for i in range(m) :
    p1,p2 = map(int, sys.stdin.readline().split())
    # 1단계만에 서로 아는 아이들을 각자의 리스트에 더해짐  
    people[p1].append(p2) 
    people[p2].append(p1)

bacon = []
for ii in range(1,n+1) : # 각행마다 돌아주면서
    # 그 행의 관계들 쭉 검사용 
    visit = [0 for _ in range(n+1)]
    visit[ii] = 0
    find_parent(ii)
    bacon.append(sum(visit))

print(bacon.index(min(bacon))+1)
