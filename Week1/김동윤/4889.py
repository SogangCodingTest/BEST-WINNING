import sys

cnt = 0
seq = 0

while True:
    inp = list(sys.stdin.readline().rstrip()) # 항상 길이는 짝수 !
    cnt = 0 
    seq+= 1 #몇번째인지
    stk=[]
    if "-" in inp:
        break

    else : 
        for i in inp:

        # 여는 괄호를 닫는 괄호로 바꾸거나, 
        # 닫는 괄호를 여는 괄호로 바꾸는 것          
        
            if i=="{" :
                stk.append(i)
            else :
                if stk :  
                    stk.pop()
                else : #stk이 없는 경우면 닫는 괄호 -> 여는 괄호로 
                    stk.append("{")
                    cnt+=1

        # for 문 다 돌았을 때 남아있으면 , 여는 괄호 -> 닫힌 괄호로 
        if stk :
            cnt+=len(stk)//2

    print(str(seq)+". " +str(cnt))
    