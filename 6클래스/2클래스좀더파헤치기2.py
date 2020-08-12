
# 주제 : 객체(인스턴스)가 어던 클래스로부터 만들어 졌는지 확인할 수 있도록하는 isinstance()함수

# 문법
# isinstance(인스턴스,클래스)
# 설명 : 함수의 첫번째 매개변수에 객체(인스턴스), 두번째 매개변수에는 클래스를 입력합니다
# 이때 인스턴스가 해당 클래스를 기반으로 만들어졌다면 True,
# 전혀 상관이 없는 인스턴스와 클래스 관계라면 False를 리턴

# 학생 클래스 선언
class Student:
    def study(self):
        print("공부를 합니다.")

# 선생님 클래스 선언
class Teacher:
    def teach(self):
        print("학생을 가리킵니다.")

# 교실 내부의 객체 리스트를 생성
classroom = [Student(), Student(), Teacher(), Student(), Student()]

# 반복을 적용해서 적절한 함수를 호출
for person in classroom:
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()

