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
dices = []
# for _ in range(N):
#     dices.append(list(map(int, input().split())))

# 더미 데이터 입력
dices.append(list(map(int, "2 3 1 6 5 4".split())))
dices.append(list(map(int, "3 1 2 4 6 5".split())))
dices.append(list(map(int, "5 6 4 1 3 2".split())))
dices.append(list(map(int, "1 3 6 2 4 5".split())))
dices.append(list(map(int, "4 1 6 5 2 3".split())))

# for문을 통한 완전 탐색
max_sum = 0
for i in range(6):
    current_sum = 0
    bottom = dices[0][i]
    bottom_idx = dices[0].index(bottom)
    top_idx = (bottom_idx + 3) % 6
    top = dices[0][top_idx]
    
    available_values = [k for k in dices[0] if k != bottom and k != top]
    current_sum += max(available_values)

    for j in range(1, 5):
        bottom = top
        bottom_idx = dices[j].index(bottom)
        top_idx = (bottom_idx + 3) % 6
        top = dices[j][top_idx]

        available_values = [k for k in dices[j] if k != bottom and k != top]
        current_sum += max(available_values)

    if max_sum < current_sum:
        max_sum = current_sum

# 결과 출력
print(max_sum)