import sys

strr = str(sys.stdin.readline().strip())
explode = str(sys.stdin.readline().strip())
stack=[]

for s in strr : 
    stack.append(s)
    if stack[-1]==explode[-1] and len(stack)>=len(explode) :
        if "".join(stack[-len(explode):len(stack)])==explode :
            #stack = stack[0:len(stack)-len(explode)]
            for i in range(len(explode)) :
                stack.pop()
            
if len( "".join(stack)) ==0 :
    print("FRULA")

else : print("".join(stack))
