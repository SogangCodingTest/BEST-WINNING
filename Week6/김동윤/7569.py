from collections import deque
import sys

m,n,h = map(int, sys.stdin.readline().rstrip().split())

he = [0, 0, 0, 0, 1, -1]
r=[-1, 1, 0, 0, 0, 0]
c=[0, 0, -1, 1, 0, 0]

tom=[]
for i in range(h) :
    tom.append(list(list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)))


def bfs(q) :
    global day
    while q :
        
        now = q.pop()
        
        for nn in range(6) :
            tmph = now[0]+he[nn]
            tmpn = now[1]+r[nn]
            tmpm = now[2]+c[nn]

            if 0<=tmph<h and \
                0<=tmpn<n and \
                    0<=tmpm<m:
                        if tom[tmph][tmpn][tmpm]==0 :
                            tom[tmph][tmpn][tmpm]=now[3]+1
                            day=now[3]+1 #day를 자꾸자꾸 갱신해 
                            q.appendleft((tmph, tmpn, tmpm, now[3]+1))


# 정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 
# 정수 -1은 토마토가 들어있지 않은 칸


q=deque()
blank=0 # -1 인 사과 세기용 (토마토 다 익었는지 여부 검사 위해)

for i in range(h) :
    for j in range(n) :
        for k in range(m) :
            if tom[i][j][k]==1 :
                q.append((i,j,k,0))
            elif tom[i][j][k]==-1 :
                blank+=1

# 토마토가 익어있는 상태이면 (1(익은사과) + -1(없는사과) 갯수가 전체 길이라 같으면) 0 출력
if len(q)+blank==m*n*h : print(0);exit()

day=0
bfs(q)

# bfs가 q가 없어져서 끝났는데, tom 안에 0이 있다!? => -1 출력
for i in range(h) :
    for j in range(n) :
        for k in range(m) :
            if tom[i][j][k]==0 :
                print(-1);exit()

else : print(day)


