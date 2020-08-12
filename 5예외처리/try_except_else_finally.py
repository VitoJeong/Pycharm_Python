
# finally구문은 예외처리 구문에서 가장 마지막에 사용할 수 있는 구문
# 예외가 발생하든 발생하지 않든 무조건 실행하는 코드

# 문법:
# try:
#   예외가 예상되는 코드
# except:
#   예외가 발생했을때 실행할 코드
# else:
#   예외가 발생하지 않았을때 실행할 코드
# finally:
#   무조건 실행할 코드

# 예제
try:
    number_input_a = int(input("정수입력>"))
    # 출력
    print("원의 반지름 : ", number_input_a)
    print("원의 둘레 : ", 2*3.14*number_input_a)
    print("원의 넓이 : ", 3.14*number_input_a*number_input_a)
except:
    print("정수를 입력하지 않았습니다")
else:
    print("예외가 발생하지 않았습니다.")
finally:
    print("일단 프로그램이 어떻게든 끝났습니다.")