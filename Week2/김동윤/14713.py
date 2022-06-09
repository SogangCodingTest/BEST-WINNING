import sys
from collections import deque

lis=deque()
n=int(sys.stdin.readline().rstrip())
for i in range(n) : 
    lis.append(deque(sys.stdin.readline().rstrip().split()))
#print(lis)

l=list(sys.stdin.readline().rstrip().split())
lcpy=l.copy()

for i in l :
    for j in lis :
        if i in j  : 
            if j[0]==i :
                lcpy.remove(j.popleft())
                break
            else :
                break
chk=0 
if lcpy :
    chk=1
    print("Impossible")
else : 
    for i in lis :
        if len(i)!=0 :
            chk=1
            print("Impossible")
            break
if chk==0:  
    print("Possible")

