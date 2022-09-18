import sys

# 기본 재귀함수 깊이 10^5로 설정
sys.setrecursionlimit(10**5)

T = int(sys.stdin.readline())

answers = []

def solve(N):
    if N == 1:
        return 1

    if N == 2:
        return 1

    return 2 * solve(N - 1)

for _ in range(T):
    N = int(sys.stdin.readline())


    answers.append(solve(N))

for answer in answers:
    print(answer)