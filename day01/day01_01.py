print("hello world!")
# 주석: 사람이 읽도록 작성한 메모
# 코드는 위에서 아래로 실행된다.
print("world hello!")

# 변수
# "=" 수학에서 사용하던 같다라는 기호가 x
# 우변에 있는 데이터를 좌변에 "대입"하시오
# 문자데이터는 쌍따옴표 안에 작성
name = "홍길동"
age = 30

print(name)
print(age)

# hello -> world
greeting = "world"
print(greeting)
print(greeting)
print(greeting)

greeting = "hello" # 재 대입
print(greeting)


# 변수 작명 방식: 변수는 띄어쓰기 x
# 파스칼 명명법: 띄어쓰기 다음문자를 대문자 ex) myName
# 스네이크 명명법: 띄어쓰기를 "_"로 표현 ex) my_name

# 기본자료형(타입)
# int: 정수 / float: 실수
# str(string): 문자열 / bool: True, False
name = "홍길동" # str
age = 30 # int
pi = 3.14 # float
isMale = True # bool

print(type(name))
print(type(age))
print(type(pi))
print(type(isMale))

# input()
# 콘솔창을 통해서 데이터를 입력
# 콘솔창에 입력한 데이터가 전달되어서 name에 대입
# name = input("이름을 입력하세요: ")
# print(name)

name = "홍길동"
age = "30"
# 문자열끼리 더하면 문자열이 이어진다.
print("이름: " + name + " 나이: " + age)

# 실습) 자기소개
# 이름(name), 나이(age)를 input으로 변수에 대입받아서
# "안녕하세요, 저는 ~이고, ~살 입니다." 출력!
name = input("이름을 입력하세요 >")
age = input("나이를 입력하세요 >")

# f-string
print(f"안녕하세요, 저는 {name}이고, {age}살 입니다.")

# format
print("안녕하세요, 저는 {}이고, {}살입니다.".format(name, age))





