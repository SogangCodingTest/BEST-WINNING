import heapq
import sys

n = int(sys.stdin.readline().strip())
candlis = []
for i in range(n) :
    heapq.heappush(candlis,int(sys.stdin.readline().strip()))
res = 0

while len(candlis)>1 :
        now=(heapq.heappop(candlis)+heapq.heappop(candlis))
        res+=now
        heapq.heappush(candlis,now)

print(res)
