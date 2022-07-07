from collections import deque
import sys
n,k= map(int, sys.stdin.readline().rstrip().split())

q=deque()
q.append((n, 0)) #시작 위치, 횟수 (초기값은 0으로 conut)
cnt=0 
visited=[-1 for _ in range(100001)] # 방문 여부 및 방문 최소 횟수를 기록 
visited[n]=0 #-1이 아닌 방문 여부 및 
case=[-1,1]

while q :
    now = q.pop()
    loc=now[0] ; time=now[1]

    if loc==k: #k 만나면 cnt 갱신 
        cnt+=1

    for i in range(3) :
            if i==2: #순간이동 경우 
                tmploc=loc*2
            else : # -1 , 1 더하는 경우 
                tmploc=loc+case[i]
            
            if 0<=tmploc<100001 and (visited[tmploc]==-1 \
                or visited[tmploc]==time+1):
                # 주의! 단순히 한번 방문했다고 무시하면 안됨
                # 이미 방문됐더라도 -
                # 방문된 아이의 최소 시간과 지금 내 시간이 같으면
                # 나도 q에 들어가기 가능 
                visited[tmploc]=time+1 # visited[tmploc]==-1 경우를 고려한 코드 
                q.appendleft((tmploc, time+1))

print(visited[k]) 
#visited에는 최소 횟수들이 기록돼있으니 k의 최소횟수 데려오면 됨 
print(cnt)
