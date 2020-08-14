
# 주제 : 클래스 함수
# 클래스 함수도 클래스 변수처럼 그냥 클래스가 가진 함수
# 일반적인 함수로 만드나 클래스 함수로 만드나 사용에는 큰 차이없음
# 다만 클래스가 가진 기능이라고 명시적으로 나타냄

# 1. 클래스 함수 만들기
# 방법: @classmethod 데이코레이터 라고 부르는데 이 기호를 붙여 함수 생성

    # class 클래스이름:
    #   @classmethod
    #   def 클래스함수명(cls,매개변수):
    #       함수기능


# 설명 : 클래스 함수의 첫번째 매개변수에는 클래스 자체가 들어온다.
#   일반적으로 cls라는 이르므이 변수로 선언

# 2. 클래스 함수 호출하기
#   클래스이름.클래스함수명(매개변수들로 전달할 인수들)

class Student:

    # 클래스 변수
    count = 0
    students = []

    # 클래스 함수(메서드)
    @classmethod
    def print(cls): # class Student클래스 자체가 넘어옴
        print("------학생목록------")
        print("이름\t총점\t평균")
        for student in cls.students: # Student.students클래스변수이름이라고 적어도 됨
            print(str(student)) # -> __str__(self)호출
        print("-------------------")

    # 인스턴스를 전달 받아 사용하는 함수
    # 생성자
    def __init__(self, name, korean, math, english, science):
        # 인스턴스 변수 선언후 초기화
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        # 클래스 변수에 접근하여 값을 지정
        Student.count += 1
        Student.students.append(self) #아래에서 Student()인스턴스를 생성하여
                                    # 위의 클래스변수 students = []리스트에 추가

    # 인스턴스들의 점수를 총합을 계산하여 리턴하는 메서드
    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    # 인스턴스가 가지는 점수들의 평균을 계산하여 리턴 하는 메서드
    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format(self.name,self.get_sum(),self.get_average())



# Student 인스턴스 생성
Student("윤인성", 87, 98, 88, 95)
Student("연하진", 92, 100, 88, 80)

Student.print() # 클래스 이름으로 클래스 메서드 호출