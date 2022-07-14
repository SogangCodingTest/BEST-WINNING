from collections import deque
import sys

# 첫째 줄에 N
# 두 번째 줄부터 N+1번째 줄까지 N개의 줄
# 작업에 걸리는 시간, 작업에 대해 선행 관계에 있는 작업들의 개수,
# 선행 관계에 있는 작업들의 번호
# 서로 선행 관계가 없는 작업들은 동시에 수행

n = int(sys.stdin.readline().rstrip())
task = deque();time = 0

for i in range(n) :
    lis = list(map(int, sys.stdin.readline().rstrip().split()))
    t= lis[0]; precnt = lis[1]; time+=lis[0]

    if precnt>0: 
        #선행돼야 하는게 있으면, 선행 번호 리스트를 task라는 리스트에 추가
        people = lis[2:]; 
        # 4 3 [3 5 6] 이 인덱스 2부터 뒤가 선행 번호 리스트
        task.append((t, precnt, people))

    else : 
        # 선행리스트 없으면 걍 people 에 -1 넣으면 되지롱 
        task.append((t, precnt, -1))

dp = [0 for _ in range(n)] # n 만큼만 만들면 됨, 각각 끝나는 시간 기록 

for i in range(n) :
    now = task.popleft()
    #print(dp, now[0])
    if now[2]== -1:
        dp[i] = dp[i] + now[0]
    else : 
        maxx = -99999
        for p in now[2] :
            # 나보다 선행돼야 하는 애들 중 가장 끝나는 시간 늦은 애 찾아
            # 걔 다음에 수행되면 된다. 
            if maxx<dp[p-1] : maxx = dp[p-1] 
            # 나보다 선행돼야 하는 애들은 이미 수행된 상황이므로 비교 가능
        dp[i] =  + now[0]+maxx
print(max(dp)) # 각각 끝나는 애들 중 가장 늦게 끝나는 애가 이 task가 끝나는 시간
