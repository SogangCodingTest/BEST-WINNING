from collections import deque
import sys
import heapq

# 아이들과 거점지를 방문한 횟수 n
n = int(sys.stdin.readline().rstrip())

# 선물 상자
present = []

for i in range(n) :
    # a가 들어오고, 
    # 그 다음 a개의 숫자가 들어온다
    lis = deque(map(int, sys.stdin.readline().rstrip().split()))

    # 맨 앞에 담긴 애가 a
    a = lis.popleft()

    if a == 0 : # 선물 꺼내줄 시간
        if not present : #근데 선물 상자 비면 -1
            print(-1)

        else : # 자신이 들고있는 가장 가치가 큰 선물
            absa, a = heapq.heappop(present) # -5 5  형태로 출력됨, 뒤에가 찐
            print(a) 

    else : # 충전 시간 
        for i in range(a) :
            heapq.heappush(present, (-lis[i] , lis[i])) 
            # 가장 큰게 root에 지정될 수 있게 하기 (-5,5) (-3,3) 형태로 저장되게
    