import sys
from collections import deque

n,m=map(int, sys.stdin.readline().split())

dcard=deque()
scard=deque()

dground=deque()
sground=deque()

for i in range(n) :
    #카드 배열의 맨 마지막이 윗쪽! 위를 꺼내려면 pop으로 꺼내면 됨
    d,s=map(int, sys.stdin.readline().split())
    dcard.append(d)
    scard.append(s)
winner = 0 

for i in range(m) :

######## 카드 내기
    if (i%2==0) : #짝수는 도도 차례 (0,2,4,,)
        dground.append(dcard.pop())
        present=dground[-1]

    else : # 홀수는 수연 차례(1,3,5,,)
        sground.append(scard.pop())
        present=sground[-1]

######## 1차 검사
    if not scard : #만약 냈는데, 수연 카드가 없다
        winner = "do"
        break

    if not dcard : #만약 냈는데, 도도카드가 없다
        winner = "su"
        break
    
######## 2차 검사

    if (present==5) : # 방금 낸 것이 5라면 다 도도꺼 
        #상대방의 그라운드에 있는 카드 더미를 뒤집어 자신의 덱 아래로 그대로 합친 후 
        for j in sground:
            dcard.appendleft(j) 

        #자신의 그라운드에 있는 카드 더미 역시 뒤집어 자신의 덱 아래로 그대로 가져와 합
        for k in dground:
            dcard.appendleft(k) 

        #그라운드 비워주기 
        sground=deque()
        dground=deque()

    elif (dground and sground) :
        #둘다 그라운드에 존재하고
        if (dground[-1]+sground[-1])==5 : 
            #그라운드의 합이 5라면 수연이꼬          

            for j in dground:
                scard.appendleft(j) 
            #상대방의 그라운드에 있는 카드 더미를 뒤집어 자신의 덱 아래로 그대로 합친 후 

            for k in sground:
                scard.appendleft(k) 
            #자신의 그라운드에 있는 카드 더미 역시 뒤집어 자신의 덱 아래로 그대로 가져와 합

            sground=deque()
            dground=deque()


if winner!=0:
    #내다가 카드 0 된 경우엔 winner에 저장돼있음 
    print(winner)

else : #그게 아니라면 길이 비교로 승패 결정!
    if len(scard) > len(dcard) :
        winner = "su"
    elif len(scard) < len(dcard) :
        winner = "do"
    else :
        winner = "dosu"

    print(winner)
