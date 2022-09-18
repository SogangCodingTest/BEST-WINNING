import sys
from collections import deque

t= int(sys.stdin.readline())
qu=deque()

for i in range(t):
    rev=0
    p= list(sys.stdin.readline().strip())
    lenp = len(p)
    n= int(sys.stdin.readline().strip())
    qu = deque((sys.stdin.readline().strip().strip("[").strip("]").split(",")))

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
                if rev%2==0:
                    qu.popleft()
                else : 
                    qu.pop()
    if(chk==0) :
        if(rev%2==0):
            res = ','.join(s for s in qu)
            print("["+res+"]")
        else :
            res = ','.join((s) for s in reversed(qu) )
            
            print("["+res+"]")

            
