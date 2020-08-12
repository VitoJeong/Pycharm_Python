
#함수의 가변 매개변수에 대해...
#함수를 실제로 호출할 때 몇개의 인수가 전달될지 미리 알수 없다면,
#만들어져 있는 함수 호출시 매개변수의 값을 전달 할떄  사용자가 직접 매개변수의 개수를 정할수 있도록
#함수에.. 가변 매개변수를 생성해 놓을 수 있습니다.

#가변 매개변수 함수를 정의 하는 문법
#   def 함수명(매개변수,매개변수,......,*가변매개변수명 ):
#       실행할 코드1
#       실행할 코드2

#가변 매개변수를 사용할떄의 제약 조건
# - 가변 매개변수 뒤에는 일반 매개변수가 올수 없습니다.
# - 가변 매개변수는 하나만 사용할 수 있습니다.

#가변 매개변수 함수 만들기 예제
def print_n_tiems(n,*values):  #["안녕하세요","즐거운","파이썬 프로그래밍"]
    # n번 반복합니다.
    for i in range(n):
        #values는 리스트처럼 활용합니다.
        for value in values:
            print(value)
        #단순 줄바꿈
        print()

#함수를 호출 합니다
print_n_tiems(3,"안녕하세요","즐거운","파이썬 프로그래밍")

#설명 : 가변 매개변수는 뒤에는 일반 매개변수가 올수 없습니다.
# 만약  print_n_times("안녕하세요","즐거운","파이썬 프로그래밍",3) 처럼 함수를 호출 할수 있다고 하면
# 어디까지가 가변매개변수이고, 어디가 매개변수 n인지 구별 하기 힘듭니다.
#그래서 파이썬 프로그래밍 언어는 내부적으로 가변 개매변수 뒤에 일반 매개변수가 오지 못하게 막은 것입니다.

#그래서 매개변수 n을 앞으로 옮기고 가변매개변수 *values를 뒤로 밀었습니다.
#가변매개변수  *values는 리스트[]처럼 사용 하면 됩니다.
#for반복문을 두번 사용해서 출력하게 만들었습니다.







