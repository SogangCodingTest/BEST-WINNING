import sys
# 손가락의 가장 적게 움직이는 회수를 구하는 프로그램
n,p = map(int, sys.stdin.readline().split())
lis=[]
lis2=[[] for _ in range(7)]  #각 줄 
cnt =0 #손가락을 움직 횟수

for i in range(n) :
    lineno, pno  = map(int, sys.stdin.readline().split())
    lis.append([lineno, pno])

#이전 음이 나보다 낮은 / 같은 음이면 안 움직여도 되지만, 
## 여기서부턴 lis2에다가 연주음 넣는것이지
# 같은 줄을 만났으면 스택에서 빼주기, 각 줄에 하나씩만
#print("lis : " , lis,"\n")
for l,p in lis : 
    #print(l,p)
    if not lis2[l] : # 아무것도 없음 내가 첫음~
        lis2[l].append(p)
        cnt+=1
    else :
        if lis2[l][-1]<p:
                lis2[l].append(p)
                cnt+=1
        elif lis2[l][-1] == p:
            continue
            
        else : #이전 음이 나보다 높은 음이면 움직여
            for j in range(len(lis2[l])-1,-1,-1) : 
                if lis2[l][j] < p :
                    lis2[l].append(p)
                    cnt+=1
                    break

                elif lis2[l][j]> p :
                    #print(lis2[l])
                    lis2[l].pop()
                    cnt+=1

                else : #떼다보니깐 나랑 똑같은 수 => 안움직여도됨
                    break

            if not lis2[l] :
                lis2[l].append(p)
                cnt+=1

    #print("lis2 : " ,lis2)
print(cnt)

