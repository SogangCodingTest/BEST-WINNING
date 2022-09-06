# 셔틀 운행 횟수 n, 
# 셔틀 운행 간격 t, 
# 한 셔틀에 탈 수 있는 최대 크루 수 m, 
# 크루가 대기열에 도착하는 시각을 모은 배열 timetable

def solution(n, t, m, timetable):
    answer = ''
    bustime = 9*60
    new_timetable = []
    dict = {}

    # HH:MM 형태를 분으로 바꿔주는 중 ~
    for time in timetable :
        hour, min = map(int, time.split(":"))
        new_timetable.append(hour*60 + min)
    
    # 빨리 도착한 사람들 순으로 줄세우기 
    new_timetable.sort()

    # 버스 시간 경우의 수 
    for i in range(n) : 
        if i>0 : 
            bustime+= t
        peopleinbus = []

        for time in range(len(new_timetable)) :
            if new_timetable[time] !=-1 and new_timetable[time]<=bustime :
                peopleinbus.append(new_timetable[time])
                new_timetable[time] = -1 # 사람 버스에 태우면 -1로 갱신 
                
            if len(peopleinbus) == m :
                break
        
        # {버스시간 : 타는 사람들 리스트 , ,,,}
        dict[bustime] = peopleinbus # 각 버스시간에 타는 사람들의 시간 배열 

    # 버스에 사람들 다 태웠고, 이제 콘이가 들어갈 자리를 찾으면 되지 
    for key in dict :
        if len(dict[key]) < m : # 아직 버스에 사람탈 수 있다면 
            dict[key] = sorted(dict[key])
            answer = key
        else : 
            # 버스에 내가 들어갈 자리없으면, 
            # 이 버스 타는 사람들 중 가장 늦게 타는 사람보다 1분 빨리! (얌체)
            answer = max(dict[key])-1

    # 아래는 answer 을 HH:MM 으로 출력해주는 과정 
    hours = str(answer//60)
    if len(hours)==1 :
        hours = "0"+hours

    minutes = str(answer-((answer//60)*60))
    if len(minutes)==1 :
        minutes = "0"+minutes

    answer = hours+":"+minutes

    return answer

print(solution(1,1,5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2,10,2, 	["09:10", "09:09", "08:00"]))
print(solution(2,1,2, 	["09:00", "09:00", "09:00", "09:00"]))
print(solution(1,1,5, 	["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(1,1,1, ["23:59"]))
print(solution(10,60,45, \
   ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"] ))

