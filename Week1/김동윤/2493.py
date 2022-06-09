# 성공 코드
n = int(input())
top = list(map(int, input().split()))
stack = []
answer = [0 for i in range(n)]

for i in range(n):
    print(stack)
    while stack:
        if stack[-1][1] > top[i]:
            answer[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i, top[i]])

for i in answer :
    print(i, end=" ")
