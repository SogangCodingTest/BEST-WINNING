import sys

n = int(sys.stdin.readline())
s = "moo"
i=1
while len(s)<n : 
    s = (str(s+ "m"+ "o"*(i+2) + s))
    if len(s)>n : 
        break
    i+=1
print(s[n-1])  
