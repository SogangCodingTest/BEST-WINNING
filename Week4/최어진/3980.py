# 테스트 케이스 입력
T = int(input())

#------- 문제 해석하기 -------#
# 시간 제한 : 1초
# 최대 계산 횟수 : 각 선수 별 적합한 포지션은 최대 5개, 선수는 총 11명
# ㄴ 5^11 = 125^8 < 10^8 -> 시간 제한 1초 내에 충분히 들어올 수 있는 계산량 => bruteforcing
#--------------------------#

# 재귀함수 선언
def place(squad, current, score):
    # 스쿼드가 완성되었을 때의 최대 능력치 합산 추가
    if current == 11:
        scores.append(score)
        return
    
    for i in range(len(stats[current])):
        # 해당 선수의 능력치가 0이 아니면서 배치 가능한 위치에 있다면 완전 탐색
        if stats[current][i] != 0 and squad[i] == False:
            new_squad = squad.copy()
            new_squad[i] = True
            place(new_squad, current + 1, score + stats[current][i])
    return

# 테스트 케이스 별 실행
answers = []
scores = []
stats = []

for _ in range(T):
    scores.clear()
    stats.clear()

    # 해당 테스트 케이스의 선수 스탯 입력
    for _ in range(11):
        stats.append(list(map(int, input().split())))

    # 재귀 함수를 통한 완전 탐색
    place([False, False, False, False, False, False, False, False, False, False, False], 0, 0)
    answers.append(max(scores))

# 정답 출력
for ans in answers:
    print(ans)