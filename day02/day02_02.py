# 연산자

# 산술연산자(사칙연산)
print(20 + 20)
print(20 - 20)
print(20 * 20)
print(20 / 8) # 소숫점 표현 2.xx
print(20 // 8) # 몫: 2
print(20 % 8) # 나머지: 4
print(2 ** 4) # 2의 4승

print("홍" + "길동") # "홍길동"
print("홍" * 3) # "홍홍홍"

num = 108
# num이 2의 배수인가요?
print(num % 2 == 0)

# 실습) 한페이지당 20개의 게시글을 볼 수 있음
# 게시판의 총 게시글은 162개
# 이때 총 페이지의 갯수와
# 마지막페이지의 게시글 수 print하세요!
total_post = 162
total_page_count = total_post // 20 + 1
last_page_post_count = total_post % 20
print("총페이지: ", total_page_count)
print("마지막페이지 게시글 수: ", last_page_post_count)

# 비교연산자 -> 결과가 bool형(True, False)
x = 10
y = 20
print(x == y)
print(x != y)
print(x < y)
print(x <= y)
print(x >= y)
print(x > y)

# x > 5 and x < 20
print(5 < x < 20)

# 논리연산자
# not / or / and
a = True
b = False
print(a and b) # and: 둘다 True여야 True
print(a or b) # or: 둘중 하나만 True여도 True
print(not a) # not: bool값을 반전

# 대입연산자 - 우선순위가 가장 낮음
num = 10
# 복합대입연산자
num = num + 5
num += 5 # num = num + 5
num -= 5 # num = num - 5
num *= 5 # num = num * 5
num /= 5 # num = num / 5

# 연산자 우선순위
# () > 산술 > 비교 > 논리 > 대입