

# 파일객체의 read()함수는 파일의 내용 전체를 읽어 문자열로 돌려준다.
file=open("C:\doit\새파일.txt","r")

data = file.read() # 파일 내용 전체를 읽어 문자열로 반환

print(data)

file.close()