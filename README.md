# previous

안쓰는 저장소를 모아놓는 공간!

<br><br>

<h3> github repository 합치는 방법(윈도우 기준) </h3>

1. 먼저 여러 저장소를 합칠 메인저장소를 하나 만들어준다(readme.md 파일까지 생성해주기)

2. 깃허브 설치후 "Git Bash"를 실행시킨다.

3. 잠시 파일을 저장할 임시 로컬폴더를 만들어준 후 해당 로컬폴더에 들어간다.

4. "git clone [메인저장소 주소]" 를 쳐서 로컬폴더에 메인저장소를 클론한 후 클론된 폴더에 들어(중요!)간다.

5. "git pull"로 git 메인저장소와 파일 최신화를 한번 진행한다.

6. git subtree add --prefix=기존레포지토리명(또는 사용할 저장폴더 이름) 기존레포지토리주소(깃허브에서 주소 복사해오기) 기존메인브랜치명(보통 master)로 필요한 저장소들을 로컬에 전부 저장한다.
    -> example) git subtree add --prefix=aeiou https://github.com/hahw94/aeiou.git master / git subtree add --prefix=ising https://github.com/hahw94/ising-model.git master

7. 모두 완료됐다면 "git push"로 파일을 모두 업로드하고 잘 업로드 됐는지 확인한다. 잘됐으면 끝!
