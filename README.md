# git-study

Git PR이랑 충돌 해결 연습해보려고 만든 레포입니다.
각자 시간 맞출 필요 없이 편할 때 진행하면 됩니다.

## 토이 프로젝트 내용

브랜치 파서 PR 올려보고, 그 과정에서 충돌 한번 겪어보고 해결하는 게 목표입니다.
git_study_checklist.py 파일 하나로 다 됩니다.

## 파일 설명

- git_study_checklist.py : 다들 여기 STATUS 딕셔너리에 자기 이름 한 줄씩 추가하면 됨
- docs/assignment.md : 순서대로 뭐 하면 되는지 적어놓음

## 충돌 발생 원인

다들 STATUS 딕셔너리 같은 자리(마지막 줄 위)에 자기 줄 추가하게 해놨어요.
그래서 누구든 먼저 merge 되면, 그 다음 사람은 push할 때 충돌 뜹니다.
일부러 그렇게 만든 거니까 뜨면 오히려 좋습니다.

## 순서

1. clone
   git clone (레포 주소)
   cd git-study

2. 브랜치 만들기
   git checkout -b feature/이름

3. git_study_checklist.py 열어서 STATUS에 한 줄 추가
   "이름_완료": "완료 (날짜)",

4. 확인
   python git_study_checklist.py

5. 커밋 + push
   git add .
   git commit -m "이름: 체크리스트 업데이트"
   git push origin feature/이름

6. GitHub에서 main으로 PR 올리기

## 충돌 뜨면

1. main 최신화
   git checkout main
   git pull

2. 내 브랜치로 와서 merge
   git checkout feature/이름
   git merge main

3. 파일 열면 이런 마커 보임
   <<<<<<< HEAD
   =======
   >>>>>>> feature/이름

4. 보통 둘 다 살리면 해결됨.

5. 다시 커밋 + push
   git add .
   git commit -m "충돌 해결"
   git push origin feature/이름

6. PR에서 충돌 표시 없어졌는지 확인하고 merge

## 충돌 났을 때 채팅방에 이런 형식으로 공유

충돌 났어요
- 파일: git_study_checklist.py
- 내 브랜치: "이름_완료": "완료 (07/14)"
- main: "다른이름_완료": "완료 (07/13)"
- 둘 다 살리는 걸로 하려는데 괜찮나요?

## 다 하고 나서

각자 스크린샷  남겨주세요 (충돌 난 화면, 해결한 화면, git log --oneline --graph).
