
# 주제 : 클래스 변수와 메서드
# 인스턴스가 속성과 기능을 가질수도 있지만,
# 클래스가 속성(변수)과 기능(함수)을 가질수도 있다.

# 1. 클래스 변수 만들기
# 클래스 변수는 class구문 바로 아래의 단계에 변수를 선언하기만 하면 된다.

    # class 이름:
    #   클래스변수 = 값

# 2. 클래스 변수에 접근

    # 클래스이름.변수이름

class Student:
    # 클래스 변수 선언
    count = 0
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
        print("{}번째 학생이 생성되었습니다.".format(Student.count))

# 학생 인스턴스들을 생성하여 리스트 공간에 저장
students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 100, 88, 80),
    Student("박두걸", 75, 84, 85, 92),
    Student("류성배", 84, 78, 82, 96),
    Student("백상혁", 80, 100, 44, 76),
    Student("최진룡", 66, 70, 100, 100)
]

#출력
print()
print("현재 생성된 총 학생 수는 {}명 입니다.".format(Student.count))

# Student클래스 외부에서도 클래스변수에 접근하여 클래스 변수값을 얻어 사용할때
# 클래스 이름.클래스변수이름


