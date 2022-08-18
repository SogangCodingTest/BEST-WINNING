def solution(n, arr1, arr2):
    mapp1 = []
    for ar1 in arr1 : 
        target = list(str(bin(ar1)[2:]))
        while len(target)<n : 
            target.insert(0, "0")
        mapp1.append(target)

    mapp2 = []
    for ar2 in arr2 : 
        target = list(str(bin(ar2)[2:]))
        while len(target)<n : 
            target.insert(0, "0")
        mapp2.append(target)

    # 어느 하나라도 벽인 부분은 전체 지도에서도 벽
    # 지도 1과 지도 2에서 모두 공백인 부분은 전체 지도에서도 공백
    final_map = list([0 for _ in range(n)] for _ in range(n))
    for r in range(n) : 
        for c in range(n) :
            if mapp1[r][c]== '0' and mapp2[r][c] == '0' : 
                final_map[r][c] = " "
            elif mapp1[r][c] == '1' or mapp2[r][c] == '1': 
                final_map[r][c] = "#"
    answer = []

    for f in final_map : 
        answer.append("".join(f))

    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
# print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))