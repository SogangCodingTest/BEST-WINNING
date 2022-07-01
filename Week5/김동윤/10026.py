import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline().rstrip())
map = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

visited1 =[[0]*n for _ in range(n)] # 일반
visited2 =[[0]*n for _ in range(n)] # 적록색맹님용

rdis = [-1, 1, 0, 0]
cdis = [0, 0, -1, 1]

def dfs1(row,col, color) : # 일반

    for i in range(4) :
        tmpr = row+rdis[i]
        tmpc = col+cdis[i] 

        if 0<=tmpr<n and 0<=tmpc<n and \
            visited1[tmpr][tmpc]==0 and map[tmpr][tmpc]==color: 
            # 같은 색인 경우에만 dfs
            visited1[tmpr][tmpc] = 1
            dfs1(tmpr, tmpc, color)

def dfs2(row,col, color) : # 적록색맹님용

    for i in range(4) :
        tmpr = row+rdis[i]
        tmpc = col+cdis[i] 

        if 0<=tmpr<n and 0<=tmpc<n and \
            visited2[tmpr][tmpc]==0 :

            if color=="B" : # 블루인 경우에는 map 도 블루여야 돌리기 
                if map[tmpr][tmpc]=="B" : 
                    visited2[tmpr][tmpc] = 2 
                    # 걍 구별용으로 2로 메꿔줌 (0만 아니면 되니,,)
                    dfs2(tmpr, tmpc, color)

            else : # G, R 인 경우는
                if map[tmpr][tmpc]!="B" :  # B가 아닌 G, R이면 돌리기 가능
                    visited2[tmpr][tmpc] = 1
                    dfs2(tmpr, tmpc, color)

# 일반   # 적록색맹님용
cnt1= 0 ;   cnt2= 0

for i in range(n) :
    for j in range(n) :
        if visited1[i][j]==0 :
            cnt1+=1 # 그림갯수 갱신
            visited1[i][j] = 1
            dfs1(i,j, map[i][j])

        if visited2[i][j]==0 :
            cnt2+=1 # 그림갯수 갱신
            visited2[i][j] = 1
            dfs2(i,j, map[i][j])

print(cnt1, cnt2)
