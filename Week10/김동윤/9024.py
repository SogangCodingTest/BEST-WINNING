import sys

t = int(sys.stdin.readline().strip())
for i in range(t) : 
    n,k = (map(int, sys.stdin.readline().rstrip().split()))
    lis = list(map(int, sys.stdin.readline().rstrip().split()))
    lis.sort()
    cnt = 0; save=k
    # S 에 속하는 서로 다른 두 개의 정수의 합이 
    # K 에 가장 가까운 두 정수
    # K 에 가장 가까운 두 정수의 조합의 수를 출력
    s,e = 0,n-1
    minim = 200000002
    while s<e : 
        cmp = lis[s] + lis[e]
############### 여기서 현재 cmp 가 차이가 가장 적게 나는 상탠지 검증 
        if minim > (abs(k-cmp)) : # 차이가 가장 적다면 
            minim = (abs(k-cmp)) # 얘로 갱신 
            cnt = 0 # cnt 초기화 (이제 이 차이값 기준으로 조합 세야해서 )
################################################################
        if cmp < k : # 너무 작아, k 가 되기엔 , so 좀 키워야 해 
            if (abs(k-cmp)) == minim : cnt+=1 
            # 근데 만약 얘가 minim 경우였다면 cnt 갱신
            s+=1

        elif cmp > k : # 너무 커, k 가 되기엔 , so 좀 줄여햐해 
            if (abs(k-cmp)) == minim : cnt+=1
            e-=1

        else : # 이거에 들어오면 (k랑 같아지면)
        # 무조건 얘 기준으로 minim 갱신되어있고
        # cnt 올려주면 됨 
            cnt+= 1
            s+=1

    print(cnt)
