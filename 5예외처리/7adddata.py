
# 파일을 파일의 마지막에 새로운 내용을 추가하기위해 추가모드로 연다.
f=open("C:\doit\새파일.txt","a")

for i in range(11,20): # 11부터 19까지 i변수에 대입
    data = "%d 번째 줄입니다.\n" %i
    f.write(data) # 새파일.txt파일의 마지막에 data변수의 값을 추가로 쓴다.

f.close()