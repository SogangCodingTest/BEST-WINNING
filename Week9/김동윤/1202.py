import sys
import heapq
n, k = map(int, sys.stdin.readline().rstrip().split())
jewerq=[]; bag = []

for nn in range(n) :
    m,v = (map(int,sys.stdin.readline().strip().split()))
    heapq.heappush(jewerq, (m,v))

for bb in range(k) : 
    bag.append(int(sys.stdin.readline().strip()))

bag.sort()

tmp =[]
res = 0
for i in range(k) : # 가방은 가장 작은 가방부터
    now_bag = bag[i]

    while jewerq and now_bag >= jewerq[0][0] : # 현재 가방 무게가 보석 무게보다 크면 
        now_jewe_kg, now_jewe_price = heapq.heappop(jewerq) # 가장 가치 큰 보석 peek 
        heapq.heappush(tmp, -now_jewe_price) # 가장 가격이 높은 보석 최대힙 만들기
    
    if tmp : 
        res-=heapq.heappop(tmp) # 마이너스로 저장해놔서 더하기 위해서 -

print(res)
