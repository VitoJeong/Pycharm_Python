
# 불_자료형이란 True와 False를 나타내는 자료형

a= True
b= False

# type()함수를 변수 a와 b에 사용하면
# 두 변수의 자료형 bool로 지정된 것을 확인할 수 있다.
print(type(a))

# 불 자료형은 조건문의 반환 값으로도 사용됨
# 1과 1은 같은가
# 조건문의 결괏값으로 True 또는 False에 해당되는
print(1 == 1) # 1과 1은 같으므로 true를 돌려받아 출력됨

# 2는 1보다 큰가
print(2>1) #True

# 2는 1보다 작은가
print(2<1) # False

# 참고
# while 조건문
# 반복 수행할 문장

# 설명 : 조건문이 참인 동안 조건문 안에 있는 문장을 반복해서 수행

# 참과 거짓이 프로그램에서 어떻게 쓰이는지 알아보는 예제
a = [1,2,3,4]
while a: # a변수에 리스트의 값이 저장되어있는 동안 반복
    print(a.pop())
    b = 1234


