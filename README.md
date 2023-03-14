# BEST-WINNING (최고이김)

🚀 서강대생들끼리 코딩테스트를 함께 준비하는 공간입니다. 🚀

> Since 2022.05.26 ~ 진행 중

  - [스터디원](#collaborator)
  - [스터디 방식](#study-rule)
  - [벌금 규칙](#late-fee)
  - [저장소 관리 규칙](#repository-rule)
  - [문제풀이 진행 내역](#table-of-content)
  - [Github 사용 튜토리얼](#github-tutorial)

 <br />

 ### Collaborator

<p align="center">
<table align="center" >

<td align="center"><a href="https://github.com/myway00"><img src="https://github.com/myway00.png" width="100px;" alt=""/><br/><sub><b>김동윤</b></sub></a></td>
<td align="center"><a href="https://github.com/zbnm2005"><img src="https://github.com/zbnm2005.png" width="100px;" alt=""/><br/><sub><b>이정모</b></sub></a></td>
<td align="center"><a href="https://github.com/MarsMan13"><img src="https://github.com/MarsMan13.png" width="100px;" alt=""/><br/><sub><b>최건</b></sub></a></td>
<td align="center"><a href="https://github.com/poodlepoodle"><img src="https://github.com/poodlepoodle.png" width="100px;" alt=""/><br/><sub><b>최어진</b></sub></a></td>
  
</table>
</p>

<br />
 
### Study-Rule

- 모임 시간 : 매주 일요일 10PM _(2023.03.26 기준)_ <br>
- 분량 : 매주 4문제 _(2023.03.26 기준)_ <br>
- **스터디 중에는** 스터디원들이 각자 선정한 문제에 대한 솔루션 및 피드백 진행
- 문제에 대해 설명해야 하는 알고리즘이 있을 시, 부가적인 설명 가능
- **스터디 완료 후**, 스터디원들은 다음날 정오까지 카톡방에 자신이 이번 주차 배정받은 주제에 대해서 백준 문제를 하나 선정해 번호 및 제목 공유 <br>
- 각자 공부하는 과정에서 참고할 만한 좋은 자료가 있으면 소스(블로그) 공유

<br />

### Late-fee

- 지각 : 스터디 전(~ 10PM)까지 PR 만들기 -> 1문제 누락 당 500원
- 결석 : 사전 사유 / 통보 없이 회의 참석하지 않을 시 -> 1회당 1000원
- 총무 : <a href="https://github.com/MarsMan13">최고최건</a>
- 사용 방식 : 모인 벌금은 회식 때 사용
- 현재 개편 중

<br />

### Repository-Rule
 
- **Branch naming convention** <br />
   - 자신의 이름으로 branch를 만듭시다!
   - (ex) `git branch [자신의 Github Nickname]` 
- **Commit convention** <br />
   - Commit Message: `성명 : n주차 m번 풀이` 
   - (ex) `김동윤 : 1주차 103827번 풀이` 
- **Pull Request convention** <br />
   - PR 제목 : `김동윤 : n주차 문제풀이 ` <br />
   - (ex) `김동윤 1주차 문제풀이`
   - PR 내용 : 빈 내용 혹은 자유

 <br /> 

### Table of Content

- 문제풀이 플랫폼은 백준(acmicpc.net)을 기준으로 선정합니다.

> 1차 알고리즘 문제풀이 순서 (기간 12주)

- [1주차. 스택] (6/2) ☑
- [2주차. 큐] (6/9) ☑
- [3주차. 힙 & PriorityQueue] (6/16) ☑ 
- [4주차. 그래프 탐색-1 완전탐색] (6/23) ☑
- [5주차. 그래프 탐색-2 DFS] (6/30) ☑ 
- [6주차. 그래프 탐색-3 BFS] (7/7) ☑
- [7주차. 다이나믹 프로그래밍] (7/14) ☑
- [8주차. 구현] (7/21)  ☑
- [9주차. 그리디 알고리즘] (7/28) ☑
- [10주차. 이분탐색] (8/6) ☑
- [11주차. 분할정복] (8/11)

| 주차 | 주제 | 김동윤 | 이정모 | 최건 | 최어진 |
|------|------|--------|--------|------|--------|
| 1    | | | | | |
| 2    | | | | | |
| 3    | | | | | |
| 4    | 그래프 - 완전 탐색 | 2589번: 보물섬<br />15686번: 치킨 배달 |  | 1759번: 암호 만들기 | 14225번: 부분수열의 합 |

<br />

### Github Tutorial

1. 현재 Repository를 Clone합니다.  
```
git clone https://github.com/SogangCodingTest/SogangCodingFighter.git [새로운 폴더 이름]
cd [새로운 폴더 이름]
```

2. 자신의 Github Nickname으로 branch를 생성합니다.
```
git branch [자신의 Github Nickname]
```

3. 자신이 풀이한 문제에 대한 코드는 `Week00/본인 이름/문제번호.py`에 저장합니다. 이후 아래 컨벤션에 따라 커밋합니다. 이후 원격 저장소로 푸시합니다.
```
git add Week00/본인 이름/문제번호.py
git commit -m "1주차 9999번 풀이"
git push origin [자신의 Github Nickname]
```

4. 해당 주차의 문제풀이는 하나의 PR 단위로 제출하는 것을 원칙으로 합니다.

작성중...

<br />

---

<p align="center">
<table align="center" >

<td align="center">1차 작성자<br /><a href="https://github.com/myway00"><img src="https://github.com/myway00.png" width="80px;" alt=""/><br/><sub><b>김동윤</b></sub></a></td>
<td align="center">2차 편집자<br /><a href="https://github.com/poodlepoodle"><img src="https://github.com/poodlepoodle.png" width="80px;" alt=""/><br/><sub><b>최어진</b></sub></a></td>
  
</table>
</p>