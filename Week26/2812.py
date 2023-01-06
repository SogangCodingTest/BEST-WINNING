import sys

n,k = map(int,sys.stdin.readline().rstrip().split())
lis=list(map(int,sys.stdin.readline().rstrip()))
stack = []
cnt = 0

for i in range(n) : 
    while stack : 
        if cnt<k and stack[-1] < lis[i]: 
            # 내가 스택 마지막 애보다 크면 스택 마지막 애 제거 
            # ( 내 이전 애들은 나보다 커야하므로 )
            stack.pop()
            cnt+=1
        else : break
    stack.append(lis[i])

# k개만큼 제거 안됐을 시엔 k개만큼 뒤에서부터 제거
while cnt<k : 
    stack.pop()
    cnt+=1

for j in stack :  
    print(j,end="")
