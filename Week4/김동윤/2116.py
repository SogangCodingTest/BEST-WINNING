import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline().rstrip())
dice =[]
maxi =-99999
for i in range(n) :
    dice.append(list(map(int,sys.stdin.readline().rstrip().split())))
faces=[]

def dfs(diceNum, face, res , faces) :
    global maxi

    if diceNum == n :

        if maxi < res :
            maxi = res
        return

    else : 
        faces.append(face)
        myFace = dice[diceNum].index(dice[diceNum-1][face])

        if myFace == 0 or  myFace == 5 :
            res+=(max(dice[diceNum][1:5]))
                    
            if myFace == 0:
                nextFace = 5
            else : nextFace =0

        elif myFace ==1 or myFace ==3 :
            res+=max([dice[diceNum][0],dice[diceNum][2],dice[diceNum][4], dice[diceNum][5]])

            if myFace == 1:
                nextFace = 3
            else : nextFace = 1

        else : # 2, 4
            res+=max([dice[diceNum][0],dice[diceNum][1],dice[diceNum][3], dice[diceNum][5]])

            if myFace == 2:
                nextFace = 4
            else : nextFace =2

        dfs(diceNum+1, nextFace, res, faces)
        
for i in range(6) :
    res= 0
    faces=[]
    dfs(0, i, res, faces)

print(maxi)
