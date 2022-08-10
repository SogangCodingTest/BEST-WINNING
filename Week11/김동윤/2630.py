import sys
n = int(sys.stdin.readline().strip())
paper = []
white = 0
blue = 0
for i in range(n) : 
    paper.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 여기로 보내진 애들은 합이 안맞는 애들의  쪼개짐 후보들
def recur(r,c, width) :
    global white
    global blue
    
    if all_same_color(r,c,width)==True: 
        if paper[r][c] ==0 : 
            white+=1
        else : 
            blue+=1
        return

    else : 
        # print(r,c,n//2)
        recur(r,    c,      width//2)
        recur(r,    c+width//2,     width//2)
        recur(r+width//2,   c,      width//2)
        recur(r+width//2,   c+width//2,     width//2)
        return
#####################################

def all_same_color(r,c, width) :
    cnt = 0
    summ = 0
    for rr in range(r,r+width) : 
        for cc in range(c,c+width) : 
            cnt+=1
            summ+= paper[rr][cc]
    return (summ == cnt or summ==0)

#######################################

recur(0,0,n)
print(white)
print(blue)
