import sys
from itertools import combinations

inp=list(map(str,sys.stdin.readline().rstrip()))
save=[] #인덱스 순서쌍 저장 
stk=[] #"(" 저장할 공간 
for i in range(len(inp)) :
    if inp[i]=="(" :
        stk.append(i)
    elif inp[i]==")" :
        save.append([stk.pop(),i])

res=[] #결과 담을 리스트 

for i in range(1,len(save)+1): #나온 순서쌍 갯수만큼 돌면서 
    #세쌍의 괄호 순서쌍이 있다면 
    # 하나 뽑을 때, 두개 뽑을 때, 세개 뽑을 때,,각 조합의 경우 구하기
    aftercombination= list(combinations(save, i))
    #print(list(aftercombination))
    for j in aftercombination : # 조합의 경우를 돌면서, 해당 인덱스를 발견한다면 
        #print(j)
        inpcpy2 = inp.copy()
        #원본 인풋을 복사해놓은 인풋의 값에서 조합 인덱스 해당하는 괄호 없애주기
        #print(inpcpy)
        for e,s in j :
            #print(e,s)
            inpcpy2[e]=""
            inpcpy2[s]=""
            res.append("".join(inpcpy2))

#print(res)
res=list(set(res)) 
#중복 제거해주기 위해 집합으로 바꿨다가
#정렬 위해 다시 리스트로 변경
res.sort()
#사전 순 정렬을 위해 진행 (안해주면 틀리더라)
for i in res:
    print(i)
