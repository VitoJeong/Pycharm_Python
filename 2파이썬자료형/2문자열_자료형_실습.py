
# 문자열은 어떻게 만들고 사용할까?

# 1> 문자열을 만드든 방법 총 4가지
    # 1. 큰따옴표 "로 양쪽 둘러 싸기
        # 예  "Hello World"
    # 2. 작은따옴표 '로 양쪽 둘러싸기
        # 예  'Hello World'
    # 3. 큰따옴표 3개 """로 연속으로 써서 양쪽 둘러싸기
        # 예  """Hello World"""
    # 4. 작은따옴표 3개 '''로 연속으로 써서 양쪽 둘러싸기
        # 예  '''Hello World'''


# 2> 문자열 안에 작은 따옴표나 큰 따옴표를 기호로 포함시키고 싶을때
    # 1. 문자열에 작은 따옴표 ' 포함시키기
food = "Python's good" # 작은 따옴표를 포함시키기위해 큰 따옴표로 둘러싸야한다.

print(food)

    # 2. 문자열에 큰 따옴표 " 포함시키기
say = '"Pythons" good' # 문자열 내부에 큰 따옴표를 기호로 표현하고 싶을때
print(say)              # 문자열 전체의 양쪽을 작은따옴표로 감싼다.

    # 3. 작은 따옴표 ' 또는 큰 따옴표 " 를 문자열에 포함시키는 또다른 방법은 백슬러시\를 사용하면 된다.
    # 즉 백슬러시 기호를 \ 작은 따옴표 ' 또는 큰 따옴표 " 앞에 삽입하면
    # 백슬러시 기호 \ 뒤에 '나 "는 문자열을 둘러싸는 기호의 의미가 아니라 문자열에 기호를 표현할 수 있다.
food = 'has\'s'
print(food)

say="has\"s"
print(say)

# 3> 여러 줄인 문자열을 변수에 대입하는 방법
    # 1. 문자열의 줄을 바꾸는 이스케이프 코드 \n 삽입하기
multiline= "Life is too short\nYou need python"
print(multiline)
    # 2. 연속된 작은따옴표 '''3개 또는 큰 따옴표 """ 3개 사용하기
multiline = '''
안녕하세요.
반갑습니다.
'''
print(multiline)

multiline="""
안녕하세요.
어서오세요.
"""

print(multiline)

#------------------------------------

# 1> 문자열 연산
head = "Python"
tail = " is fun!"
print(head + tail)

# 2> 문자열 곱하기
a = "python"
print(a * 2) # a변수에 저장된 문자열을 두 번 반복해서 연결하여 하나의 문자열로 출력

# 3> 문자열 곱하기 응용
print("=" * 50)
print("My Program")
print("="*50)

# 4> 문자열 길이 구하기
# 문자열 길이 구하기 -> len함수를 사용
a = "Life is too short"
b = len(a)

print(b) #문자열 길이 17 출력

#-----------------------------------

#문자열 인덱싱(한문자만 가리켜 얻는다)과 슬라이싱(단어를 잘라낸다)

# 1> 문자열 인덱싱
a = "Hello is"
#    01234567   <-- 문자열 중 문자의 위치를 가리키는 번호로 0인덱스 위치부터 센다.
print(a[1]) # 1위치의 문자 e를 얻어 출력
print(a[4]) # 4위치의 문자 0를 얻어 출력

b = "Hello is"
#         -2-1  <-- 전체 문자열중 뒤에서부터 문자의 위치를 가리킬때 -1부터 센다.

print(b[-1])
print(b[-2])

# 2> 문자열 슬라이싱
# 슬라이싱 기본 문법
# a[시작번호 : 끝번호] -> a변수에 저장된 문자열 문장에서 시작인덱스위치번호의 문자부터
                        # 끝 인덱스 위치번호 이전까지의 문자 단어를 잘라내어 얻어낸다.

a = "Hello is"
#    01234567
b = a[0:4]
print(b)

c = a[3:6]
print(c)

# 슬라이싱 기본 문법 2
# a[시작번호 : 생략] -> a변수에 저장된 문자열 중 시작 번호부터 끝까지 문자를 얻어낸다.

a = "Hello is"
#    01234567
c = a[1: ]
print(c)

# 슬라이싱 기본 문법 3
# a[생략: 끝번호] -> 저장된 문자열 중 처음부터 끝번호 위치까지의 문자를 얻어낸다.

a = "Hello is"
#    01234567
c=a[:7]
print(c)

# 슬라이싱 기본 문법 4
# a[생략:생략]  -> 저장된 문자열 중에서 시작번호,끝번호를 모두 생략하면
                # 처음부터 끝까지 얻어낸다.
a = "Hello is"
#    01234567
c=a[ : ]
print(c)

# 슬라이싱 기법으로 문자열 나누기 응용 예제
a = "20010331Rainy"
#    0123456789

# 연도만 출력하기
year = a[0:4]
print(year)

# '0331' 출력하기
day = a[4:8]
print(day)

# 'Rainy' 출력하기
weather = a[8:]
print(weather)

#--------------------------------
# 문자열 포매팅이란?
# 문자열 안에 어떤 값을 삽입한는 방법

# 1> 문자열 포매팅 따라하기
    #1. 숫자 바로 대입
print("I eat %d apples." %3) # %d자리에 숫자 3을 대입한 문자열 출력
    #2. 문자열 바로 대입
print("I eat %s apples." %"five") # %s자리에 문자열 five를 대입한 문자열 출력
# 결론 : 숫자를 대입할 때는 %d를 사용하고, 문자열을 대입할 때는 %s를 사용
    #3. 숫자 값을 나타내는 변수 대입
number =3
print("I eat %d apples." %number)
    #4. 문자열에 2개 이상의 값 대입
number = 1
day = "Hello"
# Hello라고 1번 인사하기
print("%s라고 %d번 인사하기" %(day,number))
# 결론 : 2개 이상의 값을 넣으려면 마지막 % 다음 괄호 안에 콤마,로 구분하여 각각의 값을 넣어 주면 된다.

# 2> 문자열 포맷코드의 종류
# %s 문자열
# %c 문자1개
# %d 정수
# %f 부동소수
# %o 8진수
# %x 16진수
# %% (문자 '%')

# 예제
# 정수갓을 문자열에 삽입하려면 %d를 사용하고
# 실수값을 문자열에 삽입하려면 %f를 사용
# %s를 사용하면 생각안해도 됨
# 왜냐하면 %s는 자동으로 %뒤의 값을 문자열로 자동으로 변환시켜 대입하기 때문

# I have 3 apples 출력
print("I have %s apples" %3)

# rate is 3.234 출력
print("rate is %s" %3.234)

# 포매팅 연산자와 %d와 %를 같이 쓸때는 %%를 사용
print("Error is %d%%" %98)

# 3> 포맷 코드와 숫자 함께 사용하기

# 1. 정렬과 공백

# 예제
# %10s는 전체 길이가 10개인 문자열 공간에서 대입되는 값을 오른쪽으로 정렬하고
# 그 앞의 나머지는 공백으로 남겨둔다.
print("%10s" %"h1")

# 예제
# 'h1'을 전체 문자열에 삽입할 때 왼쪽 정렬을 시키고 나머지는 빈 공백으로 남겨두기
print("%-10sjane" %'h1')

# 2. 소수점 표현하기
# 소수점 네번째자리 까지 나타내는 경우 .(소수점 포인트)뒤에 4개의 숫자를 출력한다는 의미
print("%0.4f" %3.14548896)

# 예제 - 전체 길이가 10개인 실수형을 소수점 네번째자리까지 표시를 하고 오른쪽정렬
print("%10.4f" %3.42134324)

# 3> format함수를 사용한 포매팅
# 설명 : 문자열의 foramt함수를 사용하면 좀 더 발전된 스타일로 문자열 포맷을 지정 가능

# 1. 숫자 바로 대입하기
# 예제
# "I eat {0} apples" 문자열 중에서 {0} 부분을 숫자 3으로 바꾸기
print("I eat {0} apples".format(3))

# 2. 문자열 바로 대입하기
print("I eat {0} apples".format("five"))

# 3. 숫자 값이 저장된 변수이름으로 대입
number = 3
print("I eat {0} apples".format(number))

# 4. 2개 이상의 값 넣기
number = 10
day = "세계"
a = "Hello {0}번 외치고 {1}여행 가자{2}".format(number,day,"하하하")
print(a)

# 5. {0},{1}과 같은 인덱스 항목 대신 더 편리한 {name}형태로 값 넣기
#       {name}형태를 사용할 경우 format()함수에 반드시 name=value와 같은 형태의 입력값이 있어야한다.
#예제
print("안녕하세요! {a}! 잘 {b}드립니다.".format(a="여러분",b="부탁"))

# 6. 왼쪽 정렬
# 예제
# :<10 표현식을 사용하면 치환되는 문자열을 왼쪽정렬하고
# 문자열의 총 자릿수를 10으로 맞출 수 있다.
print("{0:<10}".format("h1"))

# 7. 오른쪽 정렬
# 예제
# 오른쪽 정렬은 :< 대신 :> 사용하면된다.
print("{0:>10}".format("h1"))

# 8. 가운데 정렬
# 예제
# :^ 기호를 사용하여 가운데 정렬하여 삽입할 수 있다.
print("{0:^10}".format("h1"))

# 9. 정렬시 공백 문자 대신에 지정한 문자값으로 채워 넣기
# 주의할 점은 채워 넣을 문자 값은 정렬 문자 < > ^ 바로 앞에 넣어야 한다.
# 예제
# 가운데 ^로 정렬하고 빈 공간을 = 문자로 채워서 새로운 h1데이터 삽입
print("{0:!<10}".format("hi"))

# 10. 소수점 표현하기
# 예제
y = 3.42133842
print("{0:0.4f}".format(y))

# 11. { 또는 } 문자 표현
# format함수를 사용해 문자열 포매팅 할 경우
# {{}} 처럼 2개를 연속해서 사용
print("{{and}}".format())

# 12. f문자열 포매팅
# 파이썬 3.6버전 부터 f 문자열 포매팅 기능을 사용할 수 있다.
# f 문자열 포매팅은 name, age 변수 값을 생성 한 후에 그 값을 참조 할 수 있다.
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는{age}입니다.')
print(f'나는 내년이면 {age+1}살이 된다.')

# 예제
# format함수 또는 f문자열 포매팅을 사용해 "!!!python!!!" 문자열을 출력해보자
p="python"
print("{0:!^12}".format(p))
print(f'{p:!^12}')

# 4> 문자열 관련 함수
# 1. 문자 개수 세기
# 문자열 자료형은 자체적으로 함수를 가지고 있다. 다른말로 문자열 내장 함수라고 한다.
# 이 내장 함수를 사용하려면 문자열 변수 이름 뒤에 .를 붙인 다음 함수명을 써준다.

# 예제
# 문자열 중 문자 b의 개수 되돌려 받기
a = "hobby"
print(a.count('b'))

# 2. 전체 문자열 중에서 문자 또는 문자열의 시작 인덱스 위치 출력

# 예제
a = "Hello World"
b = a.find('H')
print(b)
c = a.find('V')
print(c) # V문자가 존재하지 않으므로 -1을 되돌려받는다.

# 2-2
a= "Life is too short"
print(a.index('t'))
# 만약 찾는 문자나 문자열이 존재하지 않는다면 오류를 발생시킴
# print(a.index('A'))

# 3. 문자열 삽입

# 예제
# join함수
print(",".join('abcd')) # a, b, c, d

# 4. 소문자를 대문자로 바꾸기
# upper함수는 소문자를 대문자로 변환한다.
f = "hi"
g = f.upper()
print(g)


# 5. 대문자를 소문자로 바꾸기
# lower함수는 대문자를 소문자로 변환
a = "HI"
b = a.lower()
print(b)

# 6. 왼쪾 공백 지우기
# lstrip() l은 left의미
# 문자열 중 가장 왼쪽에 있는 한 칸 이상의 연속된 공백들을 모두 제거

a = "  hi  "
print(a.lstrip())

# 7. 오른쪽 공백 지우기
# rstrip() 함수
# 문자열 중 가장 오른쪽에 있는 한 칸 이상의 연속된 공백 모두 제거
print(a.rstrip())

# 8. 양쪽 공백 지우기
# strip()함수
# 문자열 양쪽 있는 한 칸 이상의 연속된 공백 모두 제거
print(a.strip())

# 9. 문자열 바꾸기
# replace(바뀌게 될 문자열 ,바꿀 문자열) 함수
a = "A B C"
print(a.replace("A","B"))

# 10. 문자열 나누기
# split 함수는 a.split() 처럼 () 괄호 안에 아무값도 넣어 주지않으면
# 공백(스페이스,탭,엔터)기준으로 문자열을 나눔
# 만약 b.split(':') 처럼 ()안에 특정 값이 있을 경우에는 괄호 안의 기호 : 구분자 기호를 이용해
# 문자열을 나누어준다. 이렇게 나눈 값은 배열(리스트)에 나눈 값을 하나씩 저장해 리스트를 되돌려 준다.

# 예제
a = "Life is too short"
b = a.split() # 공백을 기준으로 문자열들을 나누어서 각각 []리스트에 담아 반환한다.
print(b)

b = "a:b:c:d"
c = b.split(':') # : 기호를 기준으로 문자열들을 나누어서 각각 []리스트에 담아 반환한다.
print(c)














