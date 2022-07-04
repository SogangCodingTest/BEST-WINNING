# L과 C 입력
L, C = list(map(int, input().split()))

# C개의 문자들 입력
letters = input().split()

#------- 문제 해석하기 -------#
# 시간 제한 : 2초
# 최대 계산 횟수 : 주어진 C개의 요소를 포함하거나, 포함하지 않고 생성할 수 있는 경우의 수 = 15개
# ㄴ 2^15 -> 시간 제한 2초 내에 충분히 들어올 수 있는 계산량 => bruteforcing
#--------------------------#

# 증가하는 순서를 위해 주어진 문자 정렬
letters.sort()

# 자음 및 모음 분류를 위해 미리 만들어놓은 리스트
mos = ['a', 'e', 'i', 'o', 'u']

# 중복을 피하기 위한 정답 리스트
answers = []

# 완전 탐색을 위한 재귀 함수 정의
def generate(cipher, current, mo, ja):
    # 마지막 문자까지 고려해 L 길이의 암호가 생성되었을 시 조건에 맞다면 출력
    if len(cipher) == L:
        if mo >= 1 and ja >= 2:
            if cipher not in answers:
                answers.append(cipher)
        return
    elif current >= C:
        return
    else:
        # 현재 문자를 포함하지 않은 암호 생성 고려
        generate(cipher, current + 1, mo, ja)

        # 현재 가리키는 문자가 모음인 경우
        if letters[current] in mos:
            # 현재 문자를 포함한 암호 생성 고려
            generate(cipher + letters[current], current + 1, mo + 1, ja)
        # 현재 가리키는 문자가 자음인 경우
        else:
            # 현재 문자를 포함한 암호 생성 고려
            generate(cipher + letters[current], current + 1, mo, ja + 1)

# 재귀 함수로 완전 탐색 시작
generate("", 0, 0, 0)

# 출력하기 전 가능성 있는 생성 암호들을 사전식 정렬
answers.sort()

# 정답 출력
for ans in answers:
    print(ans)