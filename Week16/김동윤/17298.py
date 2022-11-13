import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
answer = [-1 for _ in range(n)] # 없으면 -1 
stack = []

for i in range(n):
    # stack[-1] => 지금 오큰수를 구해주고 싶은 아이의 순서(인덱스)
    while stack and arr[stack[-1]] < arr[i]: # 스택의 마지막 
        answer[stack.pop()] = arr[i] # 
    stack.append(i) # 스택에 넣어주기 

for j in range(n):
    print(answer[j], end=' ')
