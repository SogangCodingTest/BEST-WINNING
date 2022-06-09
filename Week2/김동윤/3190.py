from collections import deque
import sys

#내가 바라보고 있는 방향
loc = [[-1,0], [0,1], [1,0], [0,-1]] 
#북->R->동->R-남->R->서 순서 
#R들어오면 loc[present+1]
#L들어오면 loc[present-1]


####################################################################
n = int(sys.stdin.readline().rstrip())
mapp = list([[0]*n for _ in range(n)]) #n*n map 만들기

####################################################################

k = int(sys.stdin.readline().rstrip()) #사과의 수
for i in range(k) :
    r,c = map(int,sys.stdin.readline().rstrip().split())
    mapp[r-1][c-1]=1 #사과 표시

####################################################################
l = int(sys.stdin.readline().rstrip())
save=[] #시간, 방향 저장할 리스트
for i in range(l) :
    sec, lr = list(sys.stdin.readline().rstrip().split())
    save.append([int(sec),lr])

####################################################################

sec=0
now=1 # 처음에 바라보는 방향이 동쪽 (loc의 인덱스)

row=0 #스네이크의 현재 위치 (row)
col=0 #스네이크의 현재 위치 (colimn)
tmprow=0
tmpcol=0

snake=deque() #스네이크의 몸통이 담겨있는 위치를 표시할 곳! 
snake.append([0,0]) #처음 위치 초기화

while True : 
    # print("sec : ", sec)
    # print(snake)
    # for i in range(n):
    #     print(mapp[i])

    sec+=1
    if save and save[0][0]<sec :#초가 지나면 방향 바꾸기
        if save[0][1] == "L" : #왼쪽 -1 
            now-=1#동이면 북쪽으로 갱신
            if(now<0) : now+=4
        else : 
            now+=1#동이면 남쪽으로 갱신
            if(now>3) : now-=4
        save.pop(0) #방향 바꾸고 나서 이 방향은 반영했으니 없애주기

    #현재 위치 모의 갱신 (1초에 방향 기준으로, 한칸 이동)
    tmprow+=loc[now][0]
    tmpcol+=loc[now][1]

    if [tmprow,tmpcol] in snake : #자기 몸통에 부딪히면
        break

    elif (tmpcol<n and tmpcol>-1) and (tmprow<n and tmprow>-1) : #몸통 아니고 벽 아니면 
        col=tmpcol #진짜 위치 갱신 
        row=tmprow
        snake.append([row,col]) #뒤에다가 더하기
    
    else :# 만약 갱신한 값이 벽이라면? (벽은 인덱스가 )
        break

####################################################################
    #갱신했는데 그곳의 사과 여부에 따라 꼬리 없앨지 말지 결정됨, 

    if mapp[row][col] != 1 : #사과 없다면 뒤의 꼬리 없애기
        snake.popleft() #맨 처음에 있던 애(==꼬리, 큐 맨 앞) 는 삭제 
    
    else : #사과라면 사과 먹고 꼬리 냅두기 !
        mapp[row][col] = 0


print(sec)

