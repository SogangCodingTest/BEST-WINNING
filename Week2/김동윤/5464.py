import sys
from collections import deque

n,m=map(int,sys.stdin.readline().rstrip().split())
fee=deque()
car=deque()

for i in range(n) : #주차 공간 차 무게당 요금
    fee.append(int(sys.stdin.readline().rstrip()))

for j in range(m) : #차 무게, 인덱스가 식별자 / 0 1 2 3 
    car.append(int(sys.stdin.readline().rstrip()))

park=[0]*n #주차공간
wait=deque() #기다리는 차량 
here= -99999 
#다 찼으면 -99999 주고, 
# 자리 있으면 그 중 제일 작은 수 인덱스 줄거야
money=0
#돈
for i in range(2*m) :
    #print(park)
    target = int(sys.stdin.readline().rstrip())

    # 1) 나가는 애라면 차있던 말던 상관 없삼 
    if target<0 : #-3 이면 3을 주차장에서 없애주기 
            park[park.index(-target)]=0

    # 주차장 찼는지 여부 검사
    for j in range(n) :
        if park[j]==0 :
            here = j
            break
    else : here = -99999
    # print("target : ", target)
    # print("herer : ", here)
    # print("park : ", park)
    # print("wait : " ,wait)


    # 2) 주차장 자리 존재하면 
    if (here!=-99999) : #자리 있고, 가장 작은 자리는 here 
        if wait : #대기 리스트가 있으면 
            targetwait = wait.popleft() #타켓으로 가장 오래 기다린 사람 넣어주기
            park[here]= targetwait
            money+=car[targetwait-1]*fee[here]
            #근데 타켓이 들어오려고 했던 애라면 , 대기 리스트에 넣어주기
            if target>0:
                wait.append(target)
        
        elif target>0 :
            park[here]=target
            money+=car[target-1]*fee[here]
            #요금계산

    # 3) 주차장 자리 차있으면 
    else : # 그리고 들어오려고 하면 => 대기리스트에 넣어주기 
        if target>0 :
            wait.append(target)

print(money)
        