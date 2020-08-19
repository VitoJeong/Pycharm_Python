
# [파이썬 웹 크롤링] BeautifulSoup를 이용한 웹 크롤링 - 사진 다운로드

# 파이썬 urllib모듈을 이용하여 웹상에서 사진을 가져오는 방법에 대한 설명

# ------------ 이미지 다운로드 하기 -------------
# 크롤링 하기전에 알아야 할것은 이미지가 웹상 특정 경로에 존재하는지에 관한 유무


# 사이트 링크 : https://movie.naver.com/movie/bi/mi/basic.nhn?code=157297
#
# 사이트에 접속하면 마약왕 사진이 노출돼 있는가 확인하고
# 마약왕 사진의 URL경로 확인을 위해 F12키를 눌러 개발자 도구 창을 활성화 시킨 뒤
# 개발자 도구의 왼쪽 상단 맨 위쪽에 위치한 화살표 버튼을 클릭하고
# 소스를 알고 싶은 웹페이지의 부분을 클릭하면 자동으로 마약왕 사진이 위치한 소스영역을 보여주게됨.

import urllib.request
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/bi/mi/basic.nhn?code=157297"
res = urllib.request.urlopen(url).read()

# 읽어들인 전체 HTML소스중에서 특정 부분의 코드를 파싱하기 위해
soup = BeautifulSoup(res, "html.parser")

# 읽어들인 전체 HTML소스중에서 class속성값이 poster인 div요소영역만 추출
soup = soup.find("div", class_="poster") # find()메서드를 이용해 원하는 요소영역만 추출

# 파싱한 <div> <img> </div> 소스 중에서 <img>요소의 src경로만 찾아서 가져옵니다.
imgUrl = soup.find("img")["src"]

print(imgUrl)
# https://movie-phinf.pstatic.net/20181126_96/1543207321602QPWG8_JPEG/movie_image.jpg?type=m77_110_2

# urlretrieve(다운로드할 URL, 경로 및 파일명)함수는 다운로드 받는함수
urllib.request.urlretrieve(imgUrl, soup.find("img")["alt"] + '.jpg')




