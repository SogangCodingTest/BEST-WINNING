from collections import deque
import sys
import heapq
n, k = map(int, sys.stdin.readline().rstrip().split())
jewer = []; bag = []

for nn in range(n) :
    m,v = (map(int,sys.stdin.readline().rstrip().split()))
    jewer.append((m,v))

for bb in range(k) : 
    bag.append(int(sys.stdin.readline().rstrip()))

bag.sort()
bag=deque(bag)
jewerq=[];bagq=[]

#내림차순 정렬 (가장 큰 가치/무게 -> ... )
for mm,vv in jewer :
    heapq.heappush(jewerq, (-vv,mm,vv))

tmp =[]
res = 0

for i in range(k) : # 가방은 가장 작은 가방부터
    now_bag = bag.popleft()

    while jewerq and now_bag > jewerq[0][1] : # 현재 가방 무게가 보석 무게보다 크면 
        just_for_sort, now_jewe_kg, now_jewe_price = heapq.heappop(jewerq) # 가장 가치 큰 보석 peek 
        heapq.heappush(tmp, -now_jewe_price) # 가장 가격이 높은 보석 최대힙 만들기
    
    if tmp : 
        res-=heapq.heappop(tmp) # 마이너스로 저장해놔서 더하기 위해서 -

    elif not jewerq: 
            break #담을 수 없는 보석이 하나도 없다면 
    # 어차피 이 가방 이후에
        
print(res)
