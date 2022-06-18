import sys
import heapq

n = int(sys.stdin.readline().rstrip())
cnt = 0
heap=[]
for i in range(n) :
    #  N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능    
    s,e = (map(int, sys.stdin.readline().rstrip().split()))
    # 수업이 끝난 직후에 다음 수업을 시작
    heapq.heappush(heap, (s,e)) # 끝나는 시간을 기준으로 정렬 

room=[] #회의 종료 시간 담는 방 

# 회의가 끝나는 시간보다 다음 회의의 시작시간이 빠르면
# 회의실을 하나 추가로 개설
for j in range(n) :
    s,e = heapq.heappop(heap)
    # 1) 맨 처음(암 것도 없을 때)
    if not room : heapq.heappush(room, e)

    # 2) 맨 처음 방의 종료시간보다 같거나 크면 그 방에서 회의이어서 하기 오케이
    elif s >= room[0] : 
        # room[0] (맨 처음방의) 종료시간만 비교해도 되는 것은 ,
        # 맨 처음 방의 종료시간은 가장 작은 종료시간이기 때문,
        # 가장 작은 종료시간보다도 내 시작 시간이 작다? => 당연히 뒤에 종료시간들보다도 내가 작을테니 들어갈 방 없음
        # 이건 반드시 새 방 만들어야 하는 것이지
            heapq.heappop(room) #그방에서 이제 내가 회의 시작&종료, 이전 거 빼기
            heapq.heappush(room, e) #내 종료 시간 넣기 (힙 방식으로)

    # 3) 가장 작은 종료시간보다도 시작 시간이 작으면 (앞 방에서 다 빠꾸 먹은 것)  만들어야 하는 상태 
    else :
        heapq.heappush(room, e)
print(len(room))
