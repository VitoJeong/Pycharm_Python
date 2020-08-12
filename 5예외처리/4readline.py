

# 특정 파일의 첫번째 줄을 읽어오는 예제
# f = open("C:\doit\새파일.txt","r") # 이미 생성되어있는
# line = f.readline() # readline()메서드를 사용해 파일의 첫번째 줄 읽어옴
# print(line) # 파이참 출력공간에 출력


# 특정 파일의 모든 줄을 읽어오는 예제
f = open("C:\doit\새파일.txt","r")

while True:
    line = f.readline() # 한 줄을 읽어와 line변수에 저장
    if not line: #만약 더이상 읽을 줄이 없으면?
        break #반복문 빠져나감
    print(line) #한줄 단위로 읽어 들인 내용을 출력

f.close() # File객체 자원 해제

