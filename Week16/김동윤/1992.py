import sys

n = int(sys.stdin.readline())
mapp = list( list(map(int,sys.stdin.readline().rstrip())) for _ in range(n))

lis = []

def is_it_all_zero(rowstart,colstart,leng) :
    real = 0
    for r in range(rowstart,rowstart+leng) :
        for c in range(colstart, colstart+leng) : 
            real+=(mapp[r][c])
    return real==0

def is_it_all_one(rowstart,colstart,leng) :
    tobesame = 0
    real = 0
    for r in range(rowstart, rowstart+leng) : 
        for c in range(colstart, colstart+leng) : 
            # print(r,c, rowstart, colstart)
            real+=(mapp[r][c])
            tobesame+=1
    return real==tobesame


def chk(rowstart, colstart, leng) :
        if leng==1:
            print(mapp[rowstart][colstart], end="")
            return
        num = mapp[rowstart][colstart]

        for r in range(rowstart, rowstart+leng) :
            for c in range(colstart, colstart+leng) : 
                if num!=mapp[r][c]:
                    print("(", end="")
                    for i in range(2) :
                        for j in range(2) :
                            # 0과 1 섞인 상황
                            chk(rowstart+(i*leng//2) , colstart+(j*leng//2) , leng//2)
                    print(")", end="")
                    return   

        print(mapp[rowstart][colstart], end="")     
        return

if(is_it_all_one(0,0,n)) : 
    print(1)
    exit(0)
elif (is_it_all_zero(0,0,n)) : 
    print(0)
    exit(0)

chk(0,0,n)
