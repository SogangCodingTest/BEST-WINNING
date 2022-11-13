import sys

n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip()) # 최대 K개의 집중국
nlis = list(map(int, sys.stdin.readline().strip().split()))
distance = [0 for _ in range(n-1)] # 거리 차 담을 거임
nlis.sort() # 원점에서 가까운 순 ~ 먼순 정렬
for nn in range(n-1) :
    distance[nn] = nlis[nn+1]-nlis[nn] # 자기랑 자기 다음 사이 거리 차 담아
distance.sort() # 거리차이 작은 순 정렬
# print(distance)
# k 개의 집중국 세움 =>  n-k 개의 거리 차이만 고려하면 됨
# 6개 좌표가 있는데 ( 1 3 6 6 7 9 ) ( 거리 차 2/3/0/1/2 )
# 2개 집중국 세워 ? 제일 최소로 길이 잡으려면 
# =====> {1,3} 집중국1 담당 영역 / {6,6,7,9} 집중국2 담당 영역
# 일케 배정해주면 됨, 즉 제일 거리차이 많이 나는 (집중국 갯수-1) 갯수 빼는 것 
# 가장 거리차이 적게 나는 n-k 개 선택하면 됨

print(sum(distance[0:n-k]))

