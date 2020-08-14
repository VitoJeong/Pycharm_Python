
# 주제 : getter/setter메서드

# 클래스 외부에서 직접 __radius속성에 접근할 수 없기때문에
# 간접적으로 접근할 수 있는 방법을 찾아야한다.
# getter/setter메서드는 프라이빗으로 선언된 변수의 값을 추출하거나
# 변경할 목적으로 간접적으로 속성에 접근가능

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

    # getter/setter메서드 선언
    def get_radius(self):
        return self.__radius

    def set_radius(self,value):
        #__radius인스턴스 변수에 저장할 값을 양의 숫자로만 한정
        if value <= 0:
            raise TypeError("길이는 양의 정수야야 합니다.")
        self.__radius = value

#------------------------------------------------------------------------

# 원의 둘레와 넓이를 구함
circle = Circle(10)
print("# 원의 둘레와 넓이를 구함")
print("원의 둘레 : ", circle.get_circumference())
print("원의 넓이 : ", circle.get_area())

print()

# 클래스 외부에서 __radius프라이빗 인스턴스 변수에 접근
print("# __radius 프라이빗 인스턴스 변수의 값")
# print(circle.__radius)
print(circle.get_radius())

circle.set_radius(2)
print("# 원의 둘레와 넓이를 구함")
print("원의 둘레 : ", circle.get_circumference())
print("원의 넓이 : ", circle.get_area())