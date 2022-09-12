from collections import deque
import sys

톱니 = []
for _ in range(4) :
    lis = list(sys.stdin.readline().strip())
    lis = (map(int,lis))
    톱니.append(deque(lis))

def clock(deq) :
    deq.appendleft(deq.pop())

def counter_clock(deq) :
    deq.append(deq.popleft())

def check_주변(num,dir,visit) : 
    if 0<=num-1<4 and visit[num-1]==0:
        if 톱니[num-1][2] != 톱니[num][6] :
            visit[num-1]=1
            #방향이 1인 경우는 시계 방향이고, -1인 경우는 반시계 방향
            if dir==-1 :
                # 나는 반대 방향으로 돔
                check_주변(num-1, 1, visit)
                clock(톱니[num-1])
                
            else : 
                check_주변(num-1, -1, visit) # 체크 먼저 해주고 그 다음에 바퀴 돌려야한다! 
                counter_clock(톱니[num-1])
                

    if 0<=num+1<4  and visit[num+1]==0:
        if 톱니[num+1][6] != 톱니[num][2] :
            visit[num+1]=1
            if dir==-1 :
                # 나는 반대 방향으로 돔
                
                check_주변(num+1, 1, visit)
                clock(톱니[num+1])
                
            else : 
                check_주변(num+1, -1, visit)
                counter_clock(톱니[num+1])
                

k = int(sys.stdin.readline())

for i in range(k) :

    num, dir = map(int, sys.stdin.readline().split())
    visit = [0 for _ in range(4)]
    visit[num-1] = 1
    check_주변(num-1, dir,  visit )
    if dir==-1 :
        counter_clock(톱니[num-1])
    else : 
        clock(톱니[num-1])
    # print(톱니)

res = 0
if 톱니[0][0] == 1 : res+=1
if 톱니[1][0] == 1 : res+=2
if 톱니[2][0] == 1 : res+=4
if 톱니[3][0] == 1 : res+=8
print(res)
