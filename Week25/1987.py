import sys

R, C = map(int,sys.stdin.readline().split())
board = []
disr = [-1,1,0,0]
disc = [0,0,-1,1]
maxx = 0
alphabet = [0 for _ in range(26)]

for i in range(R) :
    board.append(list(sys.stdin.readline()))
visited = [[-1]*C for _ in range(R)]
visited[0][0] = 1
alphabet[ord(board[0][0])-65] = 1

def dfs(r, c, cnt) :
    global maxx
    if cnt>maxx :
        maxx = cnt
        
    for i in range(4) :
    
        if 0<=r+disr[i]<R and 0<=c+disc[i]<C \
            and visited[r+disr[i]][c+disc[i]]==-1:
            ascii = ord(board[r+disr[i]][c+disc[i]])-65
            if alphabet[ascii]==0 :
                visited[r+disr[i]][c+disc[i]]=1
                alphabet[ascii]=1
                dfs(r+disr[i], c+disc[i], cnt+1)
                visited[r+disr[i]][c+disc[i]]=-1
                alphabet[ascii]=0

dfs(0,0,1)
print(maxx)
