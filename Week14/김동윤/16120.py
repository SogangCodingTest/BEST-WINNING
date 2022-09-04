import sys

target = str(sys.stdin.readline().strip())

while "PPAP" in target and len(str(target))>4 : 
    target = target.replace('PPAP','P')

if target=="PPAP" : 
    print("PPAP")
else :
    print("NP")

