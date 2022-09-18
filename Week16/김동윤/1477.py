
import sys
# 현재 휴게소의 개수 N, 
# 더 지으려고 하는 휴게소의 개수 M, 
# 고속도로의 길이 L
n,m,L = map(int, sys.stdin.readline().rstrip().split())

location = list(map(int, sys.stdin.readline().rstrip().split()))
location.append(0) # 0과 
location.append(L) # 맨 끝 점 추가해줘야 함, 여기에는 휴게소 세워질 수 없으므로 
location.sort() # 정렬

r = L
l = 0
answer=0
while l<r:
    mid=(r+l)//2 # 최대거리 후보

    # 시뮬레이션
    cnt = 0 # mid 간격으로 휴게소 추가 설치했을 때 총 휴게수 갯수
    for i in range(1,len(location)): # n에다가 내가 0이랑 맨 끝 위치 추가, 인덱스 n+1까지 생김
        # mid 를 최댓값으로 잡고 
        cnt+= (location[i]-location[i-1]-1)//mid # 현재 휴게소들 사이에 mid 간격, 
        # 1 빼야하는 이유 : <2> 3 4 5 <6> 일때, mid=2이라고 하면 결과는 휴게소 두개 지을 수 있다
        # 그러나 실제로는 4 위치에 하나밖에 못 지음, 그래서 1을 빼줘야 하는 것, 

    if cnt<=m : # mid 만큼 잡아서 충분히 휴게소 만들 수 있는 상황 => 그럼 mid 간격 줄이기
        answer = mid
        r=mid-1
    else : # mid 만큼 잡아서 휴게소 설치하면 모자라더라
        l=mid+1 # mid를 넓히자,,
        
print(answer)

