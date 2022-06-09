import sys
from collections import deque

n,w,l = map(int, sys.stdin.readline().split())

# 트럭 무게 담기
tr = list(map(int, input().split()))

bridge=[0]*w #다리길이
sec = 0 #시간

while bridge :
    # print("trucks : " , tr)
    # print("before bridge : ", bridge)
    sec+=1 #시간 일초 갱신 
    bridge.pop(0) # 다리 위에 있는 맨 앞에 트럭 보내주기(다리 건니기 완료 처리)

    # print("medium bridge : ", bridge)
    if tr : #그럼에도 다리에 뭐가 있으면 
        if (sum(bridge) + tr[0] <= l): 
            #만약 현재 다리 무게 + 트럭(지금 순서)
            # 가 한계무게보다 적은 경우면 
            bridge.append(tr.pop(0))
            #다리에 지금 순서의 트럭을 더해주기 
        else:
            bridge.append(0)
            # 만약 무게가 넘으면, 아무 트럭도 넣어주지 않기
    
    if not bridge :
        break
    # print("after bridge : ", bridge)
    # print('\n')

print(sec)
