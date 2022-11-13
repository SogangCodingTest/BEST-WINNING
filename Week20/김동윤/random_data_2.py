import random
f = open("input00011.txt",'w')
f.write("10000 ")
for i in range(10000,0,-1) : 
    targ = random.randint(-100, 1000000)
    targ = str(targ)
    f.write(targ+" ")
f.close()