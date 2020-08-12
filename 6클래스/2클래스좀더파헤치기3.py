
# 주제 : 클래스 내부에 선언할 수 있는 파이썬에서 제공해주는 매직 메서드
# 매직 메서드는 메서드이름 앞과 뒤에 언더스코어(__) 두개가 연속으로 붙어 있는 메서드를 말함
# 예) __메서드이름__()

# 예제1. __add__() 메서드는 +연산자 역할을 한다.
class coordinate:
    #생성자
    def __init__(self, x , y):
        self.x = x
        self.y = y

    # 더하기 + 연산자 역할을 하는 메서드
        # self는 coord1, other변수에는 coord2가 들어가서
        # self와 other로 지칭한 두 개의 숫자 묶음을 x는 x끼리, y는 y끼리 더하기를 해서
        # coordinate클래스의 객체 형태로 반환하도록 한다는 뜻
    def __add__(self, other):
        return coordinate(self.x + other.x, self.y + other.y)

coord1 = coordinate(5,7)
