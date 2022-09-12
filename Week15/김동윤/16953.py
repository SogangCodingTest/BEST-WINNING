from collections import deque
import sys
# A를 B로 바꾸는데 필요한 연산의 최솟값
a,b = map(int, sys.stdin.readline().split())
visit = [] # 방문 여부 체크 
q=deque()
q.append((a,0)) # 값, 연산을 수행한 갯수
visit.append(a) 
# 한번 도달했던 값은 visit 이라는 배열에 추가 
chk = False 
# 가능, 불가능 여부 체크 

while q :
    now, cnt = q.popleft()
    if now==b : 
        # 만약 지금 검사하는 애가 우리가 찾던 애라면 그 연산횟수+1 출력, 프로그램 종료
        chk = True
        print(cnt+1)
        exit(0)
    elif now<=b : 
        # 만약 지금 검사하는 애가 b보다 작거나 같은 아이라면 (b보다 크면 거기에 2곱하거나 1붙이면 nono)
        if now*2<=b and now*2 not in visit : 
            # 2를 곱하는 것 - b보다 안 크고 안 같고, 방문 안했다면
            q.append((now*2, cnt+1))
            visit.append(now*2)
        if int(str(now)+"1")<=b and int(str(now)+"1") not in visit  : 
            # 1을 붙이는 것 - b보다 안 크고 안 같고, 방문 안했다면
            q.append((int(str(now)+"1"), cnt+1))
            visit.append(int(str(now)+"1"))
if chk==False : # 만약 빠져나왔는데 chk가 거짓이면 이미 글러먹은 것 
    print(-1)
