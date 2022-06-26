# N과 S 입력
N = int(input())
S = list(map(int, input().split()))

#------- 문제 해석하기 -------#
# 시간 제한 : 2초
# 최대 계산 횟수 : 20개의 요소를 포함하거나, 포함하지 않고 생성할 수 있는 경우의 수 = 20개
# ㄴ 2^20 -> 시간 제한 2초 내에 충분히 들어올 수 있는 계산량 => bruteforcing
#--------------------------#

# S의 부분 합으로 만들 수 있는 자연수 여부 체크
visited = [0] * 2000000

# 완전 탐색을 위한 재귀 함수 정의
def visit(current, sum):
    # S의 마지막 요소에 도달했을 때 계산된 부분합을 기록하고 종료
    if current == N:
        visited[sum] = True;
        return
    else:
        # S의 current번째 요소를 포함하지 않은 부분 합
        visit(current + 1, sum)
        # S의 current번째 요소를 포함한 합
        visit(current + 1, sum + S[current])

# 재귀 함수로 완전 탐색 시작
visit(0, 0)

# 만들 수 없는 가장 작은 자연수를 찾기 위해 처음부터 읽어 나가기
current = 0
while visited[current] == True:
    current += 1

# 정답 출력
print(current)