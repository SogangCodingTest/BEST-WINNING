from collections import deque

N = int(input())

pillars = [list(map(int, input().split())) for _ in range(N)]
pillars.sort(key=lambda x:x[0])
pillars = deque(pillars)

print(pillars)

max_pillar = [-1, -1]
for left, height in pillars:
    max_pillar = [left, height] if height > max_pillar[1] else max_pillar

stack = deque()

while pillars[0] != max_pillar:
    left, height = pillars.popleft()

    if len(stack) == 0:
        stack.append([left, height])
    else:
        if stack[-1][1] < height:
            stack.append([left, height])

stack.append(pillars.popleft())

while len(pillars) != 0:
    left, height = pillars.popleft()

    if stack[-1][1] > height:
        stack.append([left, height])

print(stack)

# for _ in range(N):
#     left, height = map(int, input().split())

#     while len(stack) > 0:
#         top = stack[-1]

#         # if len(top) != 1:
#         #     stack.pop()
#         #     continue

#         if top[0] > left:
#             temp_stack.append(stack.pop())
#         else:
#             break

#     stack.append([left, height])

#     while len(temp_stack) > 0:
#         stack.append(temp_stack.pop())

#     print(stack)
    