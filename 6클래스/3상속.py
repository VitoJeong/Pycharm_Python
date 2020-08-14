# 상속이란?
#   새로운 클래스를 만들때 기존에 만들었던 클래스의 기능을 그대로 상속하면서
#   새로운 기능을 추가하는 것
#   이때 기존에 만들었던 클래스를 부모클래스 또는 기초클래스라 부르며,
#   상속을 통해서 새롭게 생성되는 클래스를 자식클래스 또는 파생클래스라 부름

# 클래스 상속하기 문법
    # class 자식클래스명(부모클래스명):

    # 설명 : 파이썬에서 클래스를 선언할때 다른 클래스를 상속받고 싶다면?
    #   소괄호()를 사용하여 그 안에 상속받고 싶은 클래스명을 넣어 전달함으로써
    # 해당 클래스의 모든 멤서를 상속받음

# 예제
class Bird:

    def __init__(self):
        self.flying = True

    def birdsong(self):
        print("새소리")

class Sparrow(Bird): # Sparrow클래스가 Bird클래스를 상속받음

    def birdsong(self):
        print("짹짹")

my_pet = Sparrow()

print(my_pet.flying)

my_pet.birdsong()
#----------------------------------------------------------------------
# 메서드 오버라이딩이란?
#   - 상속관계에 있는 부모클래스에서 이미 정의된 메서드를 자식클래스에서 같은 이름으로 사용하되
#       메서드의 구현부만 재정의해서 사용하는 것

class Bird:

    def __init__(self):
        self.flying = True

    def birdsong(self):
        print("새소리")

class Sparrow(Bird): # Sparrow클래스가 Bird클래스를 상속받음

    def birdsong(self):
        print("짹짹")

# 클래스 선언시 Bird클래스의 모든 멤버를 상속받음
class Chicken(Bird):

    # 생성자
    def __init__(self):
        self.flying = False
#----------------------------------------------------------------------

my_sparrow = Sparrow()

my_chicken = Chicken()

my_sparrow.birdsong()

my_chicken.birdsong()