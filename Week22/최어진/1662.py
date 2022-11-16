import sys
from collections import deque

def input(): return sys.stdin.readline().rstrip()

string = input()
q = deque()

for letter in string:
    if letter == ')':
        cnt = 0
        pull = q.pop()
        while pull != '(':
            if pull[0] == 'x':
                cnt += int(pull[1:])
            else:
                cnt += 1
            pull = q.pop()

        mul = int(q.pop())
        q.append('x' + str(mul * cnt))
    else:
        q.append(letter)

    # print(q)

cnt = 0
for letter in q:
    cnt += 1 if letter[0] != 'x' else int(letter[1:])
print(cnt)
