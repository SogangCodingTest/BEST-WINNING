import sys
from collections import deque
n=int(sys.stdin.readline().strip()) 
s=list(sys.stdin.readline().strip()) # A,B,C,D,E 포함한 식

r=[]
qu = deque()

for i in range(n): # r은 숫자 (1,2,3,4,5)
    r.append(int(sys.stdin.readline().strip()))

for i in range(len(s)): # 식의 길이만큼 돌기
    if s[i].isalpha() : # 본래 식에서 문자 발견하면 (A,B,C,D,E 등 받으면)
        qu.append(r[ord(s[i])-65]) 
        # A면 0번째, B면 1번째로 인덱스변경 
        # r에서 인덱스에 해당하는 값을 qu에 담아주기

    else :
        #적절하게 연산 수행
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

#소수점 두자리로 출력하기
print(format(qu[0], ".2f"))