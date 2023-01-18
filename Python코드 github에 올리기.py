#!/usr/bin/env python
# coding: utf-8

# In[1]:


# python 파일을 github에 올리는 걸 기록하겠음.

# python 파일 (py, ipynb 등)을 github에 등록하기 위해서는 github가입과 git 프로그램을 다운받아야함.

# git은 https://git-scm.com 여기에서 다운로드 가능, Mac OS 에서는 Homebrew를 통해 다운로드 가능

# github 가입한 후에, Repository를 생성해줌.

# github에서 repository 생성한 후에, gitbash를 github초기설정을 해줘야 함. (gitbash는 git을 다운로드하면 자동으로 같이 다운로드 됨.)

# (%)$ git config --global user.name " "
# (%)$ git config --global user.email " "    <-- 초기설정은 다음과 같이 해줌. user.name은 알아서 ""사이에 기입하면 되고, email은 github가입 이메일을 적어야함.
# git config --list 를 입력하여 내가 작성한 username과 email이 맞는지 확인해줌.

# cd 를 통해서, 업로드할 파일경로를 설정해줌. ex) cd Documents/Data/gitWorldbank (나의 경우 이렇게 경로가 설정되어있음)

# 경로 설정후, 이제 코드를 github에 공유할거임. 

# echo "# git-test">> README.md   <-- 데이터 혹은 코드 관련 설명들을 첨부할 수 있음
# git init                        <-- git에 코드나 파일을 업로드 할 수 있게 준비시킴
# git add README.md               <-- 필요한 파일 형태만 올리겠다는 뜻, 파일의 형식 상관없이 폴더에 있는 모든 데이터 업로드 하고싶을때는, git add . 만 입력하면 됨.
# git commit -m "first commit"    <-- "first commit"은 첫번째로 올린다는 뜻 (뒤에서 "second commit" 설명하면서 다시 얘기하겠음. -m은 메세지의 줄임말.)
# git branch -M main              <-- 여기서 main 은 Master의 뜻을 가짐.
# git remote add origin https://github.com/사용자이름/레파지토리주소. git  <-- 이거는 내 github repository에 나와있는 거 복사하면 됨. 내 컴퓨터와 github repository를 연결시킴.
# git remote -v  (잘 연결되었는지 확인, 내가 연결한 주소값이 나오면 연결성공.)
# git push -u origin main         <-- 데이터 혹은 코드를 업로드

#여기서 push 하고나서 username과 password를 입력하라는 요구를 받을때가 있는데, 여기서 username은 github 가입이메일이고,
# password는 내 github비밀번호가 아니라, github - setting - deleloper setting 들어가서, personal access token을 generate하고
# 받은 암호를 입력하는거임. token 설정할때, repo랑 delete repo 체크 해줘야 함.

# 이러면 파일을 github에 공유할 수 있는데, 혹시 파일을 수정했거나, 폴더에 새로운 파일이 추가된 경우도 github에 업로드 시키고 싶을시, 
# 즉, 내 컴퓨터 폴더&파일을 github에 최신화 시키고 싶을 경우, terminal을 열어서, 위에처럼 세팅해주고
# git status 를 입력하면 github에 있는것과, 내 폴더사이에 변화를 체크해줌. 그 다음에, 
# git commit -m "second commit" 를 입력해서 두번째 버전을 만들어 준 뒤, (first commit)의 첫번째로 올린다는 뜻이 초안의 느낌을 줘서 first commit이라고 함.
# git push origin main 으로 데이터를 다시 업로드 시켜주면 끝.

# 새로운 branch 만드는 방법  (코드를 수정했는데 완벽하지 않거나, 원래 코드위에 덮으면 안되는 경우에, 다른사람과 공동작업할때)
# git add .
# git commit -m "new commit"
# git chechout -b newbranch
# git push -u origin newbranch
# 최종 검토후 merge 누르면 이 새로운 코드와 기존의 코드가 합쳐짐.

# github에서 코드 불러와서 내가 수정한거와 합친 후 다시 github에 올리기. (다른사람과 공동작업할때)
# git add .
# git commit -m "third commit"  <-- 이렇게 기존의 내 코드를 먼저 저장해줌.
# git pull origin main          <-- github에 있는 (누군가가 수정했을 수도 있는) 코드를 불러들여옴
# 여기서 내가 지금 수정한거를 기준으로 github에 있는 코드를 불러서 합침.
# git push origin main          <-- 내꺼까지 더해서 다시 github에 올림.

# https://hackmd.io/@oW_dDxdsRoSpl0M64Tfg2g/ByfwpNJ-K (참고)

