

def test():
    print("test() 함수의 첫 줄")
    try:
        print("try구문이 실행됨")
        return
        print("try구문의 return 키워드 뒤")
    except:
        print("except구문이 실행됨")
    else:
        print("else구문이 실행됨")
    finally:
        print("finally구문이 실행됨")
    print("test()함수의 마지막 줄")

test()