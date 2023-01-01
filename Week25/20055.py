import sys
from collections import deque
n, k  = map(int, sys.stdin.readline().split()) 
q = deque(map(int,sys.stdin.readline().split()))
zero=0 
# 내구도 0의 갯수

for i in q :
    if i==0:
        zero+=1
robot_location = [] 
stage = 1

# 얘도 회전시키기 편하게 큐로 하려했는데
# 가장 먼저 벨트에 올라간 로봇을 알아야해서 리스트로 구현
# 리스트 앞에 있을 수록 먼저 올라간 로봇 

# 컨베이어 벨트를 회전 시키고 로봇을 얹는다고 합니다.
# 박스 모양 로봇을 하나씩 올리려고 한다.
while(True) :
    
    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    q.appendleft(q.pop()) # 벨트 회전
    for i in range(len(robot_location)) : # 로봇 위치 한 칸 이동
        robot_location[i] = robot_location[i]+1
    
    while n-1 in robot_location:
        robot_location.remove(n-1)

    # 2. 가장 먼저 벨트에 올라간 로봇부터 (리스트 앞부터), 벨트가 회전하는 방향으로 
    # 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
        #   2-1 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 
        #   그 칸의 내구도가 1 이상 남아 있어야 한다.
        
    for i in range(len(robot_location)):
        if ((robot_location[i]+1) not in robot_location and q[(robot_location[i]+1)]>0) : 
            robot_location[i]+=1
            q[robot_location[i]]-=1
            if(q[robot_location[i]]==0):
                zero+=1
            
    while n-1 in robot_location:
            robot_location.remove(n-1)
    
    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.

    if q[0]>0 :
        robot_location.append(0)
        q[0]-=1
        if(q[0]==0):
            zero+=1

    # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
    if zero>=k :
        print(stage)
        exit(0)
    else : 
        stage+=1
        