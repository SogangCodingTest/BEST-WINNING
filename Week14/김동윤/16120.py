import sys

target = str(sys.stdin.readline().strip())
stk = []

for t in target :
    stk.append(t)
    if stk[-1]=="P" and len(stk)>=4 :
        if "".join(stk[-4:])=="PPAP" : 
            for i in range(3) : 
                stk.pop()
                
if "".join(stk)=="P" : 
    print("PPAP")
else :
    print("NP")
