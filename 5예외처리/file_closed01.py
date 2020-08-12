
# 예제. 파일을 열고 있으면 해당 파일을 이동하거나 덮어 씌우거나 하는것이 불가능
#   따라서 프로그램에서 파일을 열었으면 무조건 닫아야한다.
#   파일을 제대로 닫았는지 파일객체의 closed속성으로 알 수 있다.

try:
    # 새로운 파일을 생성하는 동시에 쓰기모드로 열기
    file=open("info.txt",'w')

    # 여러가지 처리를 수행
    # file.write(dasda)

    # 파일닫기
    file.close()
except Exception as e:
    print(e)

print("파일이 제대로 닫혔는지 확인하기")
print("file.close : ",file.closed)


