
# 주제 : 프라이빗 변수
# 파이썬은 클래스 내부의 변수를 클래스 외부에서 사용하는 것을 막고 싶을때
#   인스턴스변수이름을? __변수명 형태로 선언

# math라는 이름의 모듈을 불러옴
import math

#클래스 선언
class Circle:

    def __init__(self,radius):
        self.__radius = radius # 인스턴스 변수 -> __변수명으로 선언후 값을 저장

    def get_circumference(self): # 메서드
        return 2 * math.pi * self.__radius

    def get_area(self): #메서드
        return math.pi * (self.__radius ** 2) # 인스턴스 변수에 저장된 값을 사용

#------------------------------------------------------------------------

# 원의 둘레와 넓이를 구함
circle = Circle(10)
print("# 원의 둘레와 넓이를 구함")
print("원의 둘레 : ", circle.get_circumference())
print("원의 넓이 : ", circle.get_area())

print()

# 클래스 외부에서 __radius프라이빗 인스턴스 변수에 접근
print("# __radius 프라이빗 인스턴스 변수의 값")
print(circle.__radius)

# 결론 : 클래스 내부에서 __radius를 사용하는 것은 아무 문제 없지만,
#       클래스 외부에서 __radius를 사용하려 할 때 '속성이 없다'라는 오류출력