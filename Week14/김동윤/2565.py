def star(n,x):
    out = [] # 한번 처리한 값
    if n == 3:
        return x
    else:
        for i in x: # 위에 처음 3개의 구역
            out.append(i*3)
        for i in x: # 가운데 3개의 구역 (중앙 비어있음)
            out.append(i+' '*len(x)+i)
        for i in x: # 마지막 3개의 구역
            out.append(i*3)
        return star(n//3, out)

    
n = int(input())
first = ['***', '* *', '***']
final = star(n, first)
for i in final:
    print(i)