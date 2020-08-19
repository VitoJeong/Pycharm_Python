
# 타자 게임 만들기

import random
import time

# 단어 리스트 : 여기에 단어를 추가하면 문제에 나옴
# 단어들을 리스트에 저장
w = ["cat", "dog", "fox", "monkey", "mouse", "panda", "frog", "snake", "wolf"]

# 문제번호를 저장할 변수
n = 1

# print("[타자 게임] 준비되면 엔터!")
# input() # 사용자가 엔터를 누를때까지 기다림

# 타자게임 시작한 시간 얻기
start = time.time()

# 위 w리스트에서 단어 아무거나 랜덤하게 하나 뽑아서 저장
q = random.choice(w)

# while n <= 5:
#     print("*문제",n)
#     print(q) # 문제를 보여준다.
#     x = input() # 사용자 입력을 받습니다
#     # 문제와 입력값이 같을때 (올바로 입력시)
#     if q == x:
#         print("통과!")
#         # 문제 번호를 1증가 시킴
#         n = n +1
#         # 새로운 문제를 다시 뽑아내서 얻기
#         q = random.choice(w)
#     else: #문제와 입력값이 다를때(틀렸을때)
#         print("오타~! 다시도전!")
#
# # 타자 게임이 끝난시간을 기록하여 저장
# end = time.time()
#
# # 실제로 게임활동에 걸린 시간
# et = end - start
#
# # 보기 좋게 소수점 2자리까지만 표기
# et = format(et, ".2f")
#
# print("타자시간 : ", et, "초")