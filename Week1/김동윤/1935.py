import sys
from collections import deque
n=int(sys.stdin.readline().strip())
s=list(sys.stdin.readline().strip())
r=[]
qu = deque()

for i in range(n):
    r.append(int(sys.stdin.readline().strip()))

for i in range(len(s)):#식의 길이만큼 돌면서
    if s[i].isalpha() :
        qu.append(r[ord(s[i])-65])

    else :
        b=qu.pop()
        a=qu.pop()
        if s[i]=="+":
            qu.append(a+b)
        elif s[i]=="-":
           qu.append(a-b)
        elif s[i]=="/":
           qu.append(a/b)
        elif s[i]=="*":
            qu.append(a*b)

#소수점 두자리 형식을 맞춰서 출력해주기
print(format(qu[0], ".2f"))