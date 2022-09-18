# 주사위의 갯수 N 입력
# N = int(input())
N = 5

#------- 문제 해석하기 -------#
# 시간 제한 : 2초
# 최대 계산 횟수 : 주사위는 최대 10000개, 첫 번째 주사위를 고정할 수 있는 경우의 수는 6개,
#               나머지 주사위들은 자동으로 4가지 중 하나의 가장 큰 수를 선택할 수 있음
# ㄴ 6 * (10000 - 1) -> 시간 제한 2초 내에 충분히 들어올 수 있는 계산량 => bruteforcing
#--------------------------#

# 순서대로 1번째부터 N번째까지의 주사위의 숫자 입력
dices = [list(map(int, input().split())) for _ in range(N)]

# 재귀함수를 통한 완전 탐색
max_sum = -1

def place(current_dice, top, current_sum):
    if current_dice >= N:
        max_sum = current_sum if current_sum > max_sum else max_sum
        return

for i in range(6):
    place(0, -1, max())