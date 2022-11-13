from collections import deque
import sys

n,m = map(int, sys.stdin.readline().split())
ladder = []
snake = []
for i in range(n) : 
    x,y = map(int, sys.stdin.readline().split())
    ladder.append((x,y))
for j in range(m) :
    u,v = map(int, sys.stdin.readline().split())
    snake.append((u,v))

start = 1
q=deque()
q.append((start,0))
dis = [1000 for _ in range(101)]
dis[1] = 0
while q :
    now, cost = q.popleft()
    if dis[now] <= cost :
        for i in range(1,7) :
            if now+i<=100: 
                if dis[now+i] > cost+1 :
                    dis[now]=cost+1
                    q.append((now, cost+1))
        for j in range(n) :
            now_ladder_s, now_ladder_e = ladder[j]
            if now == now_ladder_s :
                if dis[now_ladder_e] > cost+1:
                    dis[now_ladder_e] = cost+1
                    q.append((now_ladder_e, cost+1))
        for k in range(m) :
            now_snk_s, now_snk_e = snake[k]
            if now == now_snk_s :
                if dis[now_snk_e] > cost+1:
                    dis[now_snk_e] = cost+1
                    q.append((now_snk_e, cost+1))

print(dis[100])
