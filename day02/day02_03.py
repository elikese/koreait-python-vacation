# day02_03
# 조건 연산자(삼항 연산자)

score = 50
cut_line_score = 60
# (True일때 값) if (bool데이터) else (False일때 값)
result = "pass" if score >= cut_line_score else "fail"
print(result)

# 여러조건(중첩)
grade = "A" if score >= 90 else ("B" if score >= 80 else "C")

# 로그인
real_id = "python"
real_pw = 1234

# input()을 통해 input_id와 input_pw 입력받아 주세요
# 입력받은 데이터와 real_id / real_pw를 비교하여
# 둘다 같으면 "로그인성공", 하나라도 다르면 "로그인실패" 출력
input_id = input("아이디를 입력하세요 >>")
input_pw = input("비밀번호를 입력하세요 >>")
input_pw = int(input_pw) # (자료)형변환

isSameId = input_id == real_id
isSamePw = input_pw == real_pw # "1234" == 1234
isLogin = isSameId and isSamePw
result = "로그인성공" if isLogin else "로그인실패"
print(result)

# 상품의 가격을 입력받아 10% 할인된 가격을 출력
price = input("상품의 가격을 입력하세요 >>")
price = int(price)
sale_price = price * 0.9
print(sale_price)