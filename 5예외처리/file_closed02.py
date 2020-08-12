

#try except 구문을 사용

try:
    #파일을 쓰기모드로 연다
    file = open("info.txt", 'w')
    # 예외 발생
    예외.발생()

except Exception as e:
    print(e)
finally:
    # 파일닫기
    file.close()

print("파일이 제대로 닫혔는지 확인하기")
print(file.closed)

# 코드를 실행해보면 closed속성의 반환값이 False이므로 파일이 닫히지 않았다는 것을 확인
# 따라서 finally구문을 사용하여 파일을 닫아야 함.