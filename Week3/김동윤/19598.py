import heapq
import sys

n = int(sys.stdin.readline().rstrip())

times=[] #s,t 담아놓을 공간 (작은 시작시간부터)
room=[]

for i in range(n) :
    s,e = map(int, sys.stdin.readline().rstrip().split())
    times.append((s,e)) # 끝시간, 시작 시간으로 넣어둠

# times 에는 시작 시간이 작은 아이들부터 쭉 정렬 
times.sort()

# 시간 정렬은 시작 시간 기준으로 정렬 필요 ! (끝 시간 정렬하면 X)
# 방 정렬은 끝 시간 기준 정렬 (root 에 최소 종료 시간 오게)

for i in range(n) :
    s,e = times[i] 

    if not room : # 방에 암 것도 없으면 방하나 디폴트로 생성 
        room.append((e,s)) # 방에서는 root에 종료 시간 가장 빠른 것 와야 해
    else :
        # room은 힙이라 맨 앞에 있는 애가 최소 회의 end 시간
        smallestEnd, start = room[0] 

        # 최소 종료 시간의 회의실 끝나는 시간이 내 시작 시간보다 크면 
        # 기존 방들의 끝나는 시간은 내 시작 시간보다 모두 큰 상태
        # 따라서 new 방 필요
        if smallestEnd > times[i][0] : 
            # 새로 방 만들어주기
            heapq.heappush(room, (e,s) )

        else : # 아니라면 그 회의실은 내꼬
            # 회의시간은 내가 이어 넘겨받기
            heapq.heappop(room) #기존 회의실 시간 나로 대체할 거니깐 없애고
            heapq.heappush(room, (e,s)) # 대체재로 내 시간 넣기

print(len(room))

