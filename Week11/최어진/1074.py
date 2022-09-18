# sys.stdin.readline 사용
import sys

# 2차원 배열의 가로 크기 N, 타겟 행 r, 타겟 열 c 입력
N, r, c = map(int, sys.stdin.readline().rstrip().split())
# 정답 변수 초기화
answer = None

# 분할 탐색을 위한 solve() 함수 정의
def solve(N, r_begin, r_end, c_begin, c_end, range_begin, range_end):
    global r, c, answer

    # 주어진 범위를 4분할해서 타겟 위치를 포함하지 않을 시 해당 분할은 탐색 종료
    if r_begin > r or r > r_end or c_begin > c or c > c_end:
        return

    # 더 이상 쪼갤 수 없는 분할 단위(2 x 2)인 경우 정답 출력
    if N == 1:
        if r == r_begin:
            answer = range_begin if c == c_begin else range_begin + 1
        else:
            answer = range_begin + 2 if c == c_begin else range_end
        return

    ###########
    #  1 | 2  #
    #----+----#
    #  3 | 4  #
    ###########

    # 4개 분할로 나눌 때의 새롭게 나눠지는 분할 단위의 범위 길이

    step = (range_end - range_begin + 1) // 4
    # 1
    solve(N - 1, r_begin, (r_begin + r_end) // 2, c_begin, (c_begin + c_end) // 2, range_begin, range_begin + step - 1)
    # 2
    solve(N - 1, r_begin, (r_begin + r_end) // 2, (c_begin + c_end) // 2 + 1, c_end, range_begin + step, range_begin + step * 2 - 1)
    # 3
    solve(N - 1, (r_begin + r_end) // 2 + 1, r_end, c_begin, (c_begin + c_end) // 2, range_begin + step * 2, range_begin + step * 3 - 1)
    # 4
    solve(N - 1, (r_begin + r_end) // 2 + 1, r_end, (c_begin + c_end) // 2 + 1, c_end, range_begin + step * 3, range_begin + step * 4 - 1)

# 분할 탐색 수행
solve(N, 0, 2**N - 1, 0, 2**N - 1, 0, 2**N * 2**N - 1)

# 정답 출력
print(answer)