def solution(m, n, board):
    
    answer = 0
    for b in range(m) : 
        board[b] = list(board[b]) # 리스트로 변환해주기

    dir = [
        [(-1,-1), (-1,0), (0,-1), (0,0)], # 1사분면 
        [(-1,0), (-1,1), (0,0), (0,1) ], # 2사분면 
        [(0,-1), (0,0), (1,-1), (1,0)], # 3사분면 
        [(0,0), (0,1), (1,0), (1,1)] # 4사분면 
    ]

    possible = True

    while possible : # 한번이라도 제거되는 사분면있으면 계속 진행
        poplist = [] # 매 회차마다 제거될 아이들 

        for r in range(m) :
            for c in range(n) : 

                target = board[r][c] #현재 검사 대상
                if target!=0 : 
                    for i in range(4) :# 한 타일에서 사분면 탐색 

                        cnt_tobe_four = 0 # 2*2 가 다 똑같은건지 판별해줄 아이
                        # 합이 4면 4개가 모두 똑같다는 것

                        save =[]

                        for j in range(4) : 


                                # 범위체크
                                # 0이 아니고, 현재검사대상이랑 똑같으면
                                # 후보에 계속 더하고, 집어넣어주기
                            if 0<=r+dir[i][j][0]<m and 0<=c+dir[i][j][1]<n \
                                and board[r+dir[i][j][0]][c+dir[i][j][1]] !=0 \
                                and board[r+dir[i][j][0]][c+dir[i][j][1]] == target : 
                                cnt_tobe_four+=1
                                save.append((r+dir[i][j][0],c+dir[i][j][1]))

                            else : # 한번이라도 아니라면 바로 제외
                                break

                        if cnt_tobe_four==4 : # 한 사분면 2*2 pop 조건 성립 ! 
                            for s in save : 
                                poplist.append(s) # (r,c) 형태로 보관됨 

        if poplist : # pop 될 대상들 
            for pop in poplist :
                    if board[pop[0]][pop[1]] !=0 :
                        # 이미 pop 된게 아닌 경우에
                        answer+=1
                        board[pop[0]][pop[1]] = 0

            # 0 으로 빠진 애들 자리 있으면 메꿔줘야지
            for col in range(n) :
                for row in range(m-1,-1,-1) :
                    if board[row][col] == 0 :
                        # 비어있는 자리 만나면 나보다 위에 있는 행들 중
                        # 0이 아닌 애 만나면 걔를 내 자리로 이끌어주기
                        for rr in range(row-1, -1,-1) : 
                            if board[rr][col] !=0 :
                                board[row][col] = board[rr][col]  
                                board[rr][col] = 0
                                break

        else : # 아무것도 pop 되지 않았다면 이제 할 거 없어 멈춰
            possible = False

    return answer

# print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))
# print(solution(6,6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]	))
print(solution(8,5,["HGNHU", "CRSHV", "UKHVL", "MJHQB", "GSHOT", "MQMJJ", "AGJKK", "QULKK"]))
