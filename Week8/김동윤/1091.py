import sys
# N개의 카드를 이용
n = int(sys.stdin.readline().strip())

# 각 카드가 어떤 플레이어에게 가야하는지 정보
p = list(map(int,sys.stdin.readline().strip().split()))

# target라는 곳에 각 사용자들이 (0,1,2) 받아야하는 카드 정보 기록
# 결국 target 이라는 배열과 똑같아야지, 우리가 찾고자 한 것을 찾아야 함 
target=[[] for _ in range(3)]
for k in range(n) :
    target[p[k]].append(k)

# 카드 순서 결정해주는 s 배열
s = list(map(int,sys.stdin.readline().strip().split()))

# 카드 담기 0부터 n-1까지의 카드
# 현재 카드 순서대로 담는 배열
card_seq=[]
for i in range(n) :
    card_seq.append(i) 

initcard = card_seq.copy()  

# 처음엔 0,1,2,3,4..n-1 로 배열, 
# 이 초기 순서 저장
# (-1 식별에 필요)

# 카드 섞 횟수
cnt = 0

while True :
    # cmp_with target 은 카드 섞은 뒤, 각 0,1,2 에게 
    # 할당해준 아이 - target이랑 비교할 아이지
    cmp_with_target=[[] for _ in range(3)]

    # 각 사람에게 배치해주기
    for j in range(n) :
        cmp_with_target[j%3].append(card_seq[j])

    # 이걸 해줬어야해, 
    for v in range(3) :
        cmp_with_target[v].sort()

    # 만약 똑같으면 카드 섞다가 우리가 찾고자 하는 target 찾은 것이지
    if cmp_with_target==target: print(cnt) ; exit()

    else : 
        cnt+=1
        tmps = card_seq.copy()
        for c in range(n) : 
            card_seq[s[c]] = tmps[c]
            # i번째 위치에 있던 카드는 S[i]번째 위치로 이동

        if card_seq==initcard:
            print(-1); exit()
            