import sys
# 현재 휴게소의 개수 N, 
# 더 지으려고 하는 휴게소의 개수 M, 
# 고속도로의 길이 L
n,m,l = map(int, sys.stdin.readline().split())

location = list(map(int, sys.stdin.readline().split()))
location.append(0)
location.sort()
maxlen, maxstart, maxend = -1,-1,-1

for i in range(len(location)-1) : 
        if location[i+1]-location[i] > maxlen : 
            maxlen = location[i+1]-location[i]
            maxstart = location[i]
            maxend = location[i+1]

for _ in range(m) : 
    cont=True
    while maxstart<=l and maxend<=l and maxstart< maxend and cont : 
        mid = (maxstart+maxend)//2
        print("start : ", maxstart, "/end : " , maxend, "/mid : " , (maxstart+maxend)//2 , "/maxlen : ", maxlen, "/location : ", location)

        if (mid-maxstart) > (maxend-mid) and (mid-maxstart < maxlen) : 
                # print("첫 케이스")
                maxlen = mid-maxstart
                maxend = mid-1

        elif (mid-maxstart)<=(maxend-mid) and (maxend-mid < maxlen) : 
                # print("두 케이스")
                maxlen = (maxend-mid)
                maxstart = mid+1
        cont=False

    location.append(mid)
    location.sort()

    for i in range(len(location)-1) : 
        if location[i+1]-location[i] > maxlen : 
            maxlen = location[i+1]-location[i]
            maxstart = location[i]
            maxend = location[i+1]

for i in range(len(location)-1) : 
        if location[i+1]-location[i] > maxlen : 
            maxlen = location[i+1]-location[i]
            maxstart = location[i]
            maxend = location[i+1]

print("최종    start : ", maxstart, "/end : " , maxend, "/mid : " , (maxstart+maxend)//2 , "/maxlen : ", maxlen, "/location : ", location)
print(maxlen)
