import random
f = open("input00013.txt",'w')
f.write("10 ")
for i in range(10,0,-1) : 
    targ = str(i)
    f.write(targ+" ")
f.close()