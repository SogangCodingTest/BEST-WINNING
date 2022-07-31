import sys
sys.setrecursionlimit(10**5)
n = (sys.stdin.readline().strip())
target = list(sys.stdin.readline().strip())
candid = []

def recur(num, candidate) :
    if num==len(n) :
        candid.append("".join(candidate))
        return
    
    else :
        if candidate[-1]=='A' : 
            candidate.pop()

        elif candidate[-1]=='B' :
            candidate.pop()
            candidate = list(reversed(candidate))
        recur(num-1, candidate)

recur(len(target), target)

if n in candid : print(1)
else : print(0)
