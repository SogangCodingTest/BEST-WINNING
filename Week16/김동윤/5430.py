import sys
from collections import deque

t= int(sys.stdin.readline())
qu=deque()

for i in range(t): # 테케
    rev=0
    p= list(sys.stdin.readline().strip())
    lenp = len(p)
    n= int(sys.stdin.readline().strip())
    qu = deque((sys.stdin.readline().strip().strip("[").strip("]").split(",")))
# 시간초과를 줄일 방법
# 매번 reverse 를 진행하는 것은 비효율적
# R 이 나오면 REVERSE를 하는게 아니라, R을 축적 
    for i in range(lenp):
        chk=0
        if p[i]=="R":
            rev+=1
            #qu=deque(reversed(qu)) #qu=deque(sorted(qu, reverse=True))
        else : 
            if len(qu)==0 or n==0: 
                chk=1
                print("error") 
                break
            else : 
                if rev%2==0:# => 짝수번이라면 처음 상태 그대로니깐 popleft
                    qu.popleft()
                else : 
                    # => R이 홀수번이라면 한번 뒤집혔다고 
                    # 생각하고 맨 처음아이를 뽑는 것을 뒤에서 뽑는 것 (뒤집히면 맨 뒤가 처음이 되니깐)
                    qu.pop()
    if(chk==0) : # 에러 안 났다면 
        if(rev%2==0) : 
            res = ','.join(s for s in qu)
            print("["+res+"]")
        else :
            res = ','.join((s) for s in reversed(qu) )
            print("["+res+"]")
