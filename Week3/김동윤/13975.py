from heapq import heapify
import sys
import heapq

t = int(sys.stdin.readline().rstrip())

for i in range(t) :

    # 소설을 구성하는 장의 수를 나타내는 양의 정수 K
    k = int(sys.stdin.readline().rstrip()) 

    # 1장부터 K장까지 수록한 파일의 크기를 나타내는 양의 정수
    klis = list(map(int, sys.stdin.readline().rstrip().split()))

    heapify(klis) # 최소 힙으로 되게 정렬
    cost = 0 # 비용

    while len(klis)>1 : 
        #파일이 하나 남기 전까지 (하나 남아야 합치기 완료된 것)
        tmp1 = heapq.heappop(klis)
        tmp2 = heapq.heappop(klis)
        cost += tmp1+tmp2
        heapq.heappush(klis,tmp1+tmp2)

    print(cost)


