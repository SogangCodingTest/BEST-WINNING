import sys

T = int(input())
answers = []

for _ in range(T):
    commands = list(input().rstrip())

    N = int(sys.stdin.readline())
    arr = sys.stdin.readline().rstrip()
    q = arr[1:-1].split(',') if N != 0 else []

    if N == 0:
        start = 0
        end = 0
    elif N == 1:
        start = 1
        end = 1
    else:
        start = 1
        end = N

    forward = True
    error = False

    for com in commands:
        if com == 'R':
            start, end = N-1 - end, N-1 - start
            forward = not forward
        elif com == 'D':
            if start == end:
                error = True
                break

            start += 1

    if error:
        answers.append("error")
        # print("error")
        continue

    if not forward:
        start, end = N-1 - end, N-1 - start

    answer = q[start : end+1]
    if not forward:
        answer.reverse()
    answers.append(f"[{ ','.join(answer) }]")
    #     start, end = N - 1 - start, N - 1 - end

    # answers.append(f"[{ ','.join(q[start : end+1]) }]")


for ans in answers:
    print(ans)
