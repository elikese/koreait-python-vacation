# day02_01.py
# 문자열 기능들 - 2

# replace("바꾸고싶은 문자열", "대체될 문자열")
a = "life is too short you need python"
a_replace = a.replace(" ", "_")
print(a_replace)
a_replace = a.replace("python", "")
print(a_replace) # 삭제

# strip - 문자열 처음과 끝에서 매칭되는 문자들을 삭제
a = "    특가 할인행사    "
a_strip = a.strip() # 기본으로 공백을 삭제한다.
print(a_strip)
a = "**특가 할인행사**"
a_strip = a.strip("*")
a_rstrip = a.rstrip("*") # 문자열 끝부분
a_lstrip = a.lstrip("*") # 문자열 시작부분
print(a_strip)

# upper, lower
a = "Hello world"
a_upper = a.upper() # 문자열을 모두 대문자로
a_lower = a.lower() # 문자열을 모두 소문자로
print(a_upper, a_lower)

# in 연산자 - 존재여부 확인
isHelloExist = "Hello" in a # bool타입 결과
print(isHelloExist)
print("world" in a) # a변수가 담은 데이터에 "world" 있나요?
print("홍길동" in "홍") # "홍길동"에 "홍"이 있나요?

# 문자열의 처음과 끝이 무엇인지 검사
# startswith(), endswith()
email = "python@py.com"
print(email.startswith("python"))
print(email.endswith(".com"))

name = "홍길동"
# 성씨가 홍인지 검사 -> true / false
# 2가지 방법 / a == b : a와 b가 같나요?
print(name.startswith("홍"))
print(name[0] == "홍")

production = "**[SALE] Apple iphone 17 Pro**"
# "apple iphone 17 pro"
# strip(), replace(), lower()
production_strip = production.strip("*")

# 문자열기능들은 원본을 바꾸지 x
print("원본:", production)
print("가공:", production_strip)

# ** 앞뒤 제거
production = production.strip("*")
# [SALE] 제거
production = production.replace("[SALE] ", "")
# 소문자처리
production = production.lower()

print(production)
# 기능들? -> 함수: 특정기능들을 실행하는 단위
# 함수의 결과가 값이면 값처럼 사용이 가능하다.
production = "Apple iphone 17 Pro"
production = production.strip("*").replace("[SALE] ", "").lower()

print(production)


