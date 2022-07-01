# 기본 재귀함수 깊이 10^5로 설정
import sys
sys.setrecursionlimit(10**5)

# 직원 수 N, 칭찬 수 M 입력
N, M = list(map(int, input().split()))

# 직원의 상사 정보 입력 -> links 리스트
links = list(map(int, input().split()))
# links 리스트를 이용해 연결된 부하를 가리키는 down_links 리스트 생성
down_links = [list() for _ in range(N)]
for i in range(len(links)):
    if links[i] != -1:
        down_links[links[i] - 1].append(i)

# 각 사원 별 칭찬 리스트 초기화 -> goods 리스트
goods = [0] * N
for _ in range(M):
    # 입력받은 칭찬은 아래로 전달하지 않고 해당 사원에게만 달아놓음
    person, new_good = list(map(int, input().split()))
    goods[person - 1] += new_good

# DFS를 위한 재귀 함수 정의
def praise(idx, current_good):
    # 위에서부터 내려온 칭찬을 현재 사원의 칭찬에 합산
    goods[idx] += current_good

    # 현재 사원에게 달린 후배들에게 모두 재귀함수 호출
    for link in down_links[idx]:
        # 현재 사원까지 합산된 칭찬을 연결된 후배들에게 전달
        praise(link, goods[idx])

# DFS 시작
praise(0, 0)

# 정답 출력
print(' '.join(list(map(str, goods))))