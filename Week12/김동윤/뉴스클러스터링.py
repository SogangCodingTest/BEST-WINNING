
def solution(str1, str2):

    str1 = list(str1.lower())
    str2 = list(str2.lower())

    refin1 = []
    refin2 = []

    for i1 in range(len(str1)-1) : 
        if str1[i1].isalpha() and str1[i1+1].isalpha() : 
            refin1.append((str1[i1:i1+2]))

    for i2 in range(len(str2)-1) : 
        if str2[i2].isalpha() and str2[i2+1].isalpha() : 
            refin2.append((str2[i2:i2+2]))
            
    if len(refin1) > len(refin2) :
        longer = refin1.copy()
        shorter = refin2.copy()


    else : 
        longer = refin2.copy()
        shorter = refin1.copy()
    
    # 교집합 
    inter = []
    for in1 in longer:  
        if in1 in shorter : 
            inter.append(in1)
            shorter.remove(in1)

    # 합집합 
    all = refin1+refin2

    cmp = inter.copy()
    for al in all : 
        if al in cmp : 
            all.remove(al)
            cmp.remove(al)

    if len(all) !=0 : 
        answer = (len(inter)/len(all)) * 65536
    else : 
        answer = 65536
    return int(answer)

print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "	AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))
