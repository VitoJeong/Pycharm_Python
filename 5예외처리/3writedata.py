

# 예제. 파일을 쓰기 모드로 열어 출력값 적기
f = open("C:/doit/새파일.txt",'w')

for i in range(1,11):    #[1,2,3,4,5,6,7,8,9,10]
    data = "%d번째 줄입니다.\n" %i
    f.write(data) # data변수에 저장된 값을 파일객체를 통하여 새파일.txt에 써라(출력)

f.close()

# 예제. 파일을 쓰기 모드로 열어 출력값 적기
# 3wrtiedata.py 파일 만들어서 실습!

# 예제. 파이썬으로 작성한 프로그램에서 외부 파일의 내용을 읽어들이는 방법으로
# readline함수 사용
# 4readline.py 파일 만들어서 실습!
