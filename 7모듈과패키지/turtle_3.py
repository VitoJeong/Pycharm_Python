

# 반복 기능으로 도형을 그리는 프로그램

# 거북이 모듈 turtle 불러오기
import turtle as t

t.shape("turtle")
t.speed(2)
# 삼각형 그리기 for문 이용
for i in range(3):
    t.forward(200)
    t.left(120)

# 사각형 그리기 for문 이용
for i in range(4):
    t.forward(200)
    t.left(90)

# 원그리기 - 반지름 50
t.circle(50)