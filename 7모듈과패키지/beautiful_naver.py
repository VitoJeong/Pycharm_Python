

# 주제 : 파이썬으로 네이버 실시간 뉴스정보 크롤링하기

# 1. 웹 크롤링이란?
# 웹을 돌아다니며 유용한 정보를 찾아 특정 데이터베이스로 수집해오는 작업. 또는 그러한 기술

# 2. 웹 크롤링에 필요한 모듈 설치 방법
# bs4모듈 -> HTML요소들을 우리가 쉽게 사용할 수 있도록 파싱해 줄 수 있는 BeautifulSoup클래스가 존재하는 모듈

# 설치방법
# 명령프롬포터 창을 열어 pip install bs4 입력후 엔터키

# requests모듈 -> 파이썬에서 웹사이트에 http요청을 하기 위한 모듈
# 설치 방법
# 명령프롬포터 창을 열어 pip install requests 입력 후 엔터키

# 3. 네이버 실시간 뉴스정보 크롤링을 위한 목적지 찾는방법
# 목적지 페이지 : https://naver.com/ 로 접속해서 F12키를 누름

# 네이버 사이트에 접속하면 중간 쯤에 연합뉴스 <--- 실시간 최신정보 크롤링

import requests
from bs4 import BeautifulSoup

# 네이버 사이트에 요청하기 위해 requests모듈의 get()를 호출하여 네이버 사이트의 전체 HTML소스를 불러옴
# .text를 이용해서 문자열
source = requests.get("https://naver.com/").text

# 일련의 문자열만 가지고는 원하는 데이터를 가지고 올 수 없기 때문에 BeautifulSoup을 이용한다
# 요청해서 받은 source변수의 데이터를 가지고 BeautifulSoup객체에 html소스로 파싱해야한다고 옵션을 정하고
# 그 옵션을 통해 파싱한 결과값을 soup변수에 저장
soup = BeautifulSoup(source, "html.parser")
# BeautifulSoup을 사용해 웹페이지를 분석
# source변수에 저장된 값들(읽어들인 전체 내용 html문자열)과, "html.parser"라는 문자열을
# BeautifulSoup() 메서드의 매개변수로 넣어주면
# 읽어들인 전체 HTML내용중 특정 부분의 데이터를 파싱할 수 있는 역할의 BeautifulSoup객체로 만들어 줌으로써
# BeautifulSoup객체의 유용한 메서드(원하는 데이터를 추출)를 사용하여 데이터를 뽑아낼 수 있다.

# HTML태그들을 이쁘게 파싱한 soup변수 내부에서 전체 HTML태그들 중에서
# .클래스 속성 값이 issue인 <a class="issue">추출할 뉴스정보</a> 요소들을 모두 찾아서 가져오는데
# select를 하게되면 해당 <a>요소들을 새로운 리스트의 각 인덱스 위치에 담아서 리스트를 반환해준다.
hotKeys = soup.select(".issue")

# hotKeys 리스트 내부에 저장된 하나하나의 최신 뉴스정보 순서를 부여하기위해 변수를 선언
index = 0

# hotKeys 리스트 내부에 저장되어 있는 <a class="issue">...</a>요소들의 갯수만큼 반복하게되는데
# hotKeys 리스트의 0번째 인덱스 위치의 <a></a>요소부터 끝인덱스 위치에 저장된 <a></a>요소들을 각각 꺼내어
# key 변수에 저장해서 사용
for key in hotKeys:
    #최신 뉴스정보 순서 번호 부여
    index +=1
    # key.text를 통해서 <a class="issue">추출할 뉴스정보</a>중에서 추출할 뉴스정보 텍스트 노드값만 얻어 출력
    print(str(index)+". " + key.text)
    
    






