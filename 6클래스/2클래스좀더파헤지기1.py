
# 클래스 내부에 존재하는 생성자란?
# 클래스 이름과 같은 함수를 생성자라고 부른다.
# 클래스 내부에 __init__라는 함수를 만들어 객체를 생성할때 처리할 내용 작성.

    # 문법
    # class 클래스이름:
    #      def__init__(self,추가적인 매개변수):
    #         코드자성

# 메서드란?
# 클래스가 가지고있는 함수를 메서드라 한다.
    # 문법
    # class 클래스이름:
    #     def 메서드이름(self,추가적인 매개변수);
    #       코드작성

# 예제1. 인스턴스가 생성될 때 자동으로 허추뢰어
#   변수를 초기화 해주는 __init--생성자 및 메서드 선언하여 클래스 만들기
class Dog:

    # 매개변수 self는 Dog클래스로 부터 생성한 자기자신의 Dog객체를 전달받아 사용
    # self.name구문은 Dog객체에 객체변수 name이 새롭게 생성되고,
    # self.name = name구문 중에서 name은 (self,name)구문중 매개변수 name으로부터 전달받은 값을
    # Dog객체의 객체변수 name에 저장하는 구문
    def __init__(self,name):
        self.name = name

    # bark(self) 메서드
    # 설명 : 매개변수 self에는 클래스 자신의 객체인 Dog객체를 전달받음
    # print()구문은 생성한 Dog객체의 객체변수 name에 저장된 값을 참조하여 출력
    def bark(self):
        print(self.name + "가 멍멍하고 짖는다.")

my_dog = Dog("삼식이") # 인스턴스 생성(객체 생성)시 매개변수가 하나인 생성자를 호추러하여
                        # name변수값을 초기화

my_dog.bark() # 인스턴스의 메서드 호출

# 예제2. 클래스 내부에 생성자, 메서드 선언
class Student:
    #생성자
    def __init__(self,name,korean,math,english,science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    # 메서드 : 점수 합 구하기
    # 참고 : \ 줄바꿈을 하지 않고 계속해서 그줄에 이어 나간다는 뜻
    def get_sum(self):
        return self.korean + self.math + \
               self.english + self.science
    # 메서드 : 평균을 구하기
    def get_avarage(self):
        return self.get_sum() / 4

    # 메서드
    def to_string(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_avarage())
# -----------------------------------------------------

# Student인스턴스를 생성하여 리스트에 저장
students = [
    Student("윤인성", 84, 96, 78, 92), #인스턴스 생성
    Student("연하진", 90, 100, 80, 78),
    Student("구지연", 78, 72, 66, 100),
    Student("나선주", 98, 92, 96, 88),
    Student("윤아린", 95, 88, 84, 75),
    Student("윤명월", 64, 88, 92, 78)
]

# 학생 한 명의 정보씩 반복하여 출력
print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student.to_string())

# 예제3. 클래스 변수와 인스턴스 변수
#   클래스에서도 변수가 선언된 위치에 따라 변수의 유효범위가 달라지며,
#   이에 따라 다음과 같이 구분할 수 있다.
    # 1. 클래스 변수
    #   해당 클래스에서 생성된 모든 인스턴스가 값을 공유하는 변수
    # 2. 인스턴스 변수
    #   __init__ 생성자 내에서 선언된 변수
    #   인스턴스가 생성될 때 마다 새로운 값이 할당되는 변수

class Dog:
    # 클래스 변수 선언
    sound = "멍멍"
    # 생성자 선언
    def __init__(self,name):
        # 인스턴스 변수 선언
        self.name = name

    # 일반 메서드 선언
    def bark(self):
        print(self.name + "가 멍멍하고 짖는다.")

# 인스턴스 생성
my_dog = Dog("삼식이")
your_dog = Dog("콩이")

#클래스 변수 접근
print(my_dog.sound)
#인스턴스 변수에 접근
print(my_dog.name)

#클래스 변수 접근
print(your_dog.sound,end="")
#인스턴스 변수에 접근
print(your_dog.name)

