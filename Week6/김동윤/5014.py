
import sys
from collections import deque

F, S, G, U, D = map(int,sys.stdin.readline().rstrip().split())
#총 F층으로 이루어진 고층 건물에 사무실이 있고, 
#강호가 지금 있는 곳은 S층이고,
#이제 엘리베이터를 타고 G층으로 이동하려고 한다.

updown = [U, -D]
impossible = True # 그 층 도달하면 false로 변경됨 

def bfs(q) :
    global impossible
    while q :
        #print(q)
        now = q.pop()
        
        if now[0]==G:
            impossible = False
            print(now[1])
        for j in range(2) : #up, down 두 버튼의 경우를 체크 
            tmps = now[0]+updown[j]
            if 0<tmps and tmps<F+1 and visited[tmps]==0 : 
                visited[tmps]=1
                q.appendleft((tmps, now[1]+1))
                # append 로 하면 틀림, fifo 로 bfs 탐색하도록 하기 

# mini=99999 => 처음에 이 변수랑 now[1]이랑 비교한 후 
# mini를 갱신시켜주는 것으로 했다가 틀렸다. 
# 최대 1000000까지 나올 수 있어서,,^.^

q=deque()

q.append((S,0)) # q에 넣을 것 ( 현재 층수, 버튼 누른 횟수 ) 
visited = [0 for _ in range(F+1)]
visited[S]=1

bfs(q)

if impossible : print("use the stairs")
