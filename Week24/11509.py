import sys

n = int(sys.stdin.readline()) 
hlis = list(map(int,sys.stdin.readline().split()))
arrow = []
cnt = 0
# 반드시 왼쪽 아이부터 터뜨려야 한다.
# 왼쪽부터 차례로 검사한다.
for i in range(len(hlis)):
    # 현재 풍선 터뜨릴 화살이 ARROW에 있으면 그거 꺼내쓰고 H-1로 갱신
    if hlis[i] in arrow :
        arrow[arrow.index(hlis[i])]-=1
    # 없으면 H 의 화살 하나 더 써야한다.
    else :
        cnt+=1
        arrow.append(hlis[i]-1)
# 총 화살의 갯수 출력
print(len(arrow))
