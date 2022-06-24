from operator import indexOf
import sys
from itertools import combinations
# L개의 알파벳 소문자로 이뤄진 암호
# C개의 알파벳 제공 
l,c = map(int, sys.stdin.readline().rstrip().split())
lis = list(sys.stdin.readline().rstrip().split())

# 최소 한 개의 모음(a, e, i, o, u)
# 최소 두 개의 자음
mo = ['a', 'e', 'i', 'o', 'u']

lismo = [] # lis 내 모음

liscpy = lis.copy() #본래 lis 에서 pop 할 예정이라 하나 더 복사해둔 것임 

for i in range(c) :
    if liscpy[i] in mo : 
        lismo.append(lis.pop(lis.index((liscpy[i])))) 
        
# 위 for 문을 돌고나면 lis 에는 자음만 남게 된다.

totallis = []
# 총 문자열 담을 리스트 선언

# 모음 가능한 최대 갯수는 l-2
for i in range(1, l-1) : #자음이 두개는 들어가야 해서
    lismocomb = []
    lisjacomb = []
    lismocomb.append(list(combinations(lismo,i)))
    lisjacomb.append(list(combinations(lis,l-i)))
    
    # print("\n i번째, " ,i, l-i)
    # print(list(lismocomb))
    # for k in lismocomb :
    #     print("mo", k)
    # print(list(lisjacomb))
    # for j in lisjacomb :
    #     print("ja", j)

    for k in lismocomb :
        for kk in k : 
            for j in lisjacomb :
                for jj in j :
                    res=list(kk+jj)
                    res.sort()
                    totallis.append("".join(res))

totallis.sort()

for i in totallis :
    print(i)
