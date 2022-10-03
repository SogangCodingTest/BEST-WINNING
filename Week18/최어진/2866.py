# sys.stdin.readline() 사용
import sys

# 단어 갯수 R, 단어 길이 C 입력
R, C = map(int, sys.stdin.readline().rstrip().split())

# R x C 크기의 테이블 입력
table = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

# 1. 문제 해석
#
# 만약 가장 위의 행을 지워도 테이블의 열을 읽어서 문자열이 중복되지 않는다면, 가장 위의 행을 지워주고 count의 개수를 1 증가시키는 과정을 반복한다.
# 만약 동일한 문자열이 발견되는 경우, 반복을 멈추고 count의 개수를 출력 후 프로그램을 종료한다.
# 
# 요약 : 처음으로 중복이 발생하는 행 번호 - 1 출력하기

# 2. 초기 접근
# 
# 제한 시간 : 1초
# R, C의 최댓값 : 10^3
# 10^3 길이의 문자열 10^3개가 중복되지 않는지를 검사하는 횟수를 10^3번 반복
# 문자열을 슬라이싱해서 set에 넣고 중복 체크한다고 했을 때 -> 최대 10^9로 초과

# count = 0

# while count < R:
#     S = set()
#
#     for c in range(C):
#         string = ''
#         for r in range(count + 1, R):
#             string += table[r][c]
#         S.add(string)

#     if len(S) != C:
#         break

#     count += 1

# # 시간 초과
# print(count)

# 3. 개선된 접근
# 
# 단어들의 len이 R부터 1까지 줄어든다고 했을 때, 처음으로 중복되기 시작하는 idx를 K라고 하면
# K + 1, K + 2, ... 모두 당연히 중복됨. 따라서 처음으로 중복되기 시작하는 K를 찾는 방법 필요 -> 이분 탐색
# start = 0, end = R - 1

# 정답 변수 초기화
count = 0
# 이분 탐색 범위 : 0 ~ R - 1
start = 0
end = R - 1

# 이분 탐색
while start <= end:
    middle = (start + end) // 2

    # set을 이용한 문자열들의 중복 여부 검사
    S = set()
    stop = False
    for c in range(C):
        string = "".join([table[r][c] for r in range(middle, R)])
        
        if string not in S:
            S.add(string)
        else:
            stop = True
            break

    # 만약 문자열이 특정 글자에서 중복되었다면
    if stop:
        # 이전 글자부터 중복될 수 있었는지 탐색
        end = middle - 1
    else:
        count = middle
        start = middle + 1

# 정답 출력
print(count)
