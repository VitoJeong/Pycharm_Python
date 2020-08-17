

# 사용할 모듈을 불러옴

# urlopen함수는 url에 접속하기 위한 함수
# 웹 크롤링을 위해서 반드시 사용해야하는 함수
# from문은 특정 라이브러리에서 한 부분만을 불러와서 사용할 때 사용하는 구문
# urllib.request모듈 내부에 있는 urlopen이라는 함수만 불러와서 사용하겠다는 내용
from urllib.request import urlopen

# bs4모듈의 BeautifulSoup클래스를 사용하기위해 불러옴
from bs4 import BeautifulSoup

# request모듈 내부에 있는 urlopen()함수를 이용해 기상청 페이지의 코드 내용을 읽어들임
# urlopen()함수는 URL주소의 페이지를 열어주는 함수
# urlopen()함수로 기상청의 전국 날씨를 제공하는 사이트를 열어주고 read()함수로 데이터들을 읽어들임
# decode()함수로 읽어들인 바이너리 데이터를 문자열로 반환해 얻어옴
target = \
    urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108").read().decode('utf-8')

# urllib.request.urlopen()함수는 웹 서버에 정보를 요청한 후, 돌려 받은 응답을 저장하여
# 응답 객체(HTTPResponse)를 반환
# 반환된 응답 객체의 read()메서드를 실행하여 웹 서버가 응답한 데이터를 바이트 배열로 읽어들임
# 읽어들임 바이트 배열은 이진수로 이루어진 수열이어서 그대로는 사용하기 어렵다.
# 웹서버가 응답한 내용이 텍스트 형식의 데이터라면, 바이트 배열의 decode("utf-8")메서드를 실행하여 문자열로 변환할 수 있다.

# BeautifulSoup을 사용해 웹페이지를 분석함
# target변수에 저장된 값들(읽어들인 전체 내용 html문자열)과, "html.parser"라는 문자열을
# BeautifulSoup()함수의 매개변수로 넣어주면
# 읽어들인 전체 HTML내용중 특정 부분의 데이터를 파싱할 수 있는 역할을 하는 BeautifulSoup객체로 만들어 줌으로서
# BeautifulSoup객체의 유용한 메서드(원하는 데이터 추출)를 사용하여 데이터를 뽑아낼 수 있다.
soup = BeautifulSoup(target, "html.parser")

 # 유용한 함수
 # select("선택해 가져올 태그명") 함수
 # -> HTML전체 데이터 중에서 select함수 호출시 인수로 전달한 태그명에 해당되는 태그들만 추출해서
 #      새로운 배열에 모두 담아 배열을 반환해주는 함수

location = soup.select("city")
print(location)






