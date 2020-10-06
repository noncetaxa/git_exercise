# test 3 브랜치 

## 어떻게 나오는가 확인해보겠다

- clone: 원격 저장소에서 복사해오기
- add: 스테이지에 파일을 추가
- commit: 스테이지에 추가된 파일들 상태를 저장
- push: 원격 저장소에 저장된 것을 보내기

## 파일 내용 되돌리기

- 특정 파일 내용을 마지막 커밋으로 돌리려면 파일내용 확인 창에서 '코드뭉치 버리기'.

## branch

- 갈래치기. 기능을 이름을 쓰는 것을 권장함.

## 병합하기(merge)

- fast-forward: head branch(current) 가 master에서 바로 나온 것일 때 그대로 병합하는 것
- master에서 가지치기를 여러 번 하고 head를 옮겨다니면서 각기 수정했을 때 병합하면 충돌이 일어날 가능성이 크다

## 되돌리기 1 - reset

- "초기화"시키고 hard를 선택. 쉽지만 중간 커밋이 모두 사라짐.
- 강제 push로 저장소에 등록해야 하는데, 소스트리에서는 강제 push가 안 됨
- CLI에서 강제로 푸시만 가능: git push --force

## 되돌리기 2 - branch

- branch를 만들어 branch상에서 작업한 후(head가 branch에 있는 상태)
- master로 checkout해서(head를 master로 옮김)
- branch의 작업 내용을 병합

## 되돌리기 3 - revert

- 되돌리기할 때는 이것이 기본인 듯?

## revert test

- 리버트해서 사라질 내용