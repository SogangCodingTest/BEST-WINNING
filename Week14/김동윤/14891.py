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

def check_주변(num,dir) : 
    if 0<=num-1<4 :
        if 톱니[num-1][2] != 톱니[num][6] :
            #방향이 1인 경우는 시계 방향이고, -1인 경우는 반시계 방향
            if dir==-1 :
                # 나는 반대 방향으로 돔
                clock(톱니[num-1])
                check_주변(num-1, 1)
            else : 
                counter_clock(톱니[num-1])
                check_주변(num-1, -1)

    if 0<=num+1<4 : 
        if 톱니[num+1][6] != 톱니[num][2] :
            if dir==-1 :
                # 나는 반대 방향으로 돔
                clock(톱니[num+1])
                check_주변(num+1, 1)
            else : 
                counter_clock(톱니[num+1])
                check_주변(num+1, -1)

k = int(sys.stdin.readline())

for i in range(k) :
    num, dir = map(int, sys.stdin.readline().split())
    check_주변(num-1, dir)
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
