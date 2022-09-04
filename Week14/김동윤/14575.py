import sys

n,t = map(int, sys.stdin.readline().strip().split())
people = []
llis = 0 ; rlis = 0
maxl = -1 
maxr = -1
res = 10**10 # 

for _ in range(n) :
    l,r = map(int, sys.stdin.readline().strip().split())
    people.append((l,r, r-l)) 
    # r-1 은 내 최대주량 - 최소주량, 
    # 최대 주량이 커버쳐줄 수 있는 양, 즉 최소주량 마시고 남은 주량  

    llis+=l # 최소 주량 다 더했는데 t보다 큰 경우 불가능 체크용 !  
    rlis+=r # 최대 주량 다 더했는데 t보다 작은 경우 불가능 체크용 !  

    if maxl < l : maxl = l
    if maxr < r : maxr = r

# 최소양들 다 더했는데 t보다 큰 경우
# 최대양들 다 더했는데 t보다 작은 경우
# => 불가능
if llis > t or rlis < t :
        print(-1)
        exit(0)

# 불가능 아닌 경우엔 이분 탐색 

l,r = maxl, maxr 
# 최소 주량들 중 max 인 아이 (최소 후보) 부터
# 최대 주량 중 max 인 아이 (최대 후보) 
# 후보 범위

while l<=r : 
    mid = (l+r)//2 
    chk = t # 술 할당량
    cover = 0 # 술 커버 가능 여부 측정 

    for p in people : 
        pl,pr, pcover = p[0], p[1], p[2] 
        # 최소 주량, 최대 주량, 최소 주량 마시고 더 마실 수 있는 양
        
        # 전부 일단 최소 주량부터 마시게 해야함
        chk-=pl # 할당량에서 최소주량 빼
        # chk에는 모자란 수만 남음 (채워야하는 술할당량)

        cover+= min(mid-p[0], p[2]) # 이 부분에서 비교가 필요 !! 
        # 지금 정해놓은 주량에서 최소 주량 뺀 것 vs 사용자의 최대 주량에서 최소주량 뺀 것
        # 중 더 작은 범위
        # ex : (정해놓은 주량이 7잔이고 최소 주량이 3잔) vs (최대 주량 8잔 최소 주량 3잔)
        # 이 경우는 전자
        # ex : (정해놓은 주량이 7잔이고 최소 주량이 3잔) vs (최대 주량 5잔 최소 주량 3잔)
        # 이 경우는 후자

    if cover >= chk : # 사람들이 더 마셔줄 수 있는 상황이면 mid 값 이하 ok
        # 더 적은 mid 값으로도 사람들이 감당가능한 지 검사 위해서
        # r 을 줄여줌
        if res > mid : 
            res = mid
        r=mid-1

    else : 
        # 사람들이 감당할 수 없다면~
        # 조금 더 주량을 늘려라~
        l=mid+1

else : print(res)
