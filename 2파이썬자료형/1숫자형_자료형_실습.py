
# 숫자형 데이터는 어떻게 만들고 사용할까?

#1. 정수형(Interger)
# 양수, 음수, 0
# 예) a라는 이름의 변수 메모리 공간에 123양의 정수를 저장 할 수 있다.
a = 123
print(a)

a = -178
print(a)

a = 0
print(a)

#2. 실수형(Floating-point)
#소수점이 포함된 숫자를 말함
a=1.2
print(a)

a = -3.45
print(a)

#a라는 이름의 변수 메모리 공간에 컴퓨터 지수표현 방식으로
#4.24e10 또는 4.24E10 실수를 저장할 수 있따.
a = 4.24E10 # 4.24e10은 4.24*10의 10승의 값을 의미
print(a)

a=4.24e-10 # 4.24e-10은 4.24*10의 -10승의 값을 의미
print(a)

#8진수와 16진수
#8진수는 숫자0 + 알파벳소문자o 또는 대문자O로 시작하는 숫자 값이다.
a = 0o177
#16진수를 만들기 위해서는 0x로 시작하면된다.
a = 0x8ff
b = 0xACB
