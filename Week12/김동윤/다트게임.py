def solution(dartResult):
    dartResult = list(dartResult)
    startidx = 0
    divide_three = []
    # (1) 세개로 뽀개는 과정 
    for d in range(len(dartResult)) : 
            if (dartResult[d].isdigit() and not ((d>0 and dartResult[d-1]=='1') and dartResult[d]=='0')) : 
                endidx = d-1
                if endidx > 0 and len(dartResult[startidx:endidx+1])>1:
                    divide_three.append(dartResult[startidx:endidx+1]) 
                startidx = d
            
            elif d==len(dartResult)-1 : # 맨 마지막에 오면
                # if dartResult[-4].isdigit() : # 10 에다가 옵션 있는 경우
                #     divide_three.append(dartResult[len(dartResult)-4:len(dartResult)])
                # elif dartResult[-3].isdigit() :
                #     divide_three.append(dartResult[len(dartResult)-3:len(dartResult)])
                # else : # 뒤에서 두자리가 숫자지
                #     divide_three.append(dartResult[len(dartResult)-2:len(dartResult)])
                divide_three.append(dartResult[endidx+1:len(dartResult)])

    # print(divide_three)

    # (2) 점수 계산 과정 
    total = [] # 점수 (get) / S D T (sdt) / 보너스 (bonus)
    bonus = False # 보너스가 false 면 보너스 없는 것, false 아닐 때 연산 

    for dt in range(len(divide_three)) : 
        # print(total)
        if divide_three[dt][0]=='1' and divide_three[dt][1]=='0' :
            get = 10
            sdt = divide_three[dt][2]
            if len(divide_three)>3 :
                bonus = divide_three[3]
        else : 
            get = int(divide_three[dt][0])
            sdt = divide_three[dt][1]
            if len(divide_three[dt])>2 :
                bonus = divide_three[dt][2]
        # 2-1 ) sdt 따라서 제곱 처리 ~ 
        if sdt == 'S' :
            get**=1
        elif sdt == 'D' :
            get**=2
        else : 
            get**=3

        # 2-2 bonus 처리 
        if bonus!=False : 
            
            if bonus == "*" :
                if dt>0 : # 처음 아니라면 
                    total[dt-1]*=2
                    get*=2
                else : # 처음이라면
                    get*=2

            else : # 보너스가 샵 인 경우 
                get*=-1
        
        total.append(get)
    
        bonus = False # 보너스 다시 False 처리 

    # print("tot : " , total)
    answer = sum(total)
    return answer


print(solution("1D2S3T*"))
