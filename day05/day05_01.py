# day05_01
# 반복문 - for
"""
for 변수 in 전체:
    반복실행될 코드
전체 -> 컬렉션자료형, 문자열, range() 등..
반복마다 하나씩 가져올수 있는 구조면 가능(__iter__)

변수 -> 순서대로 대입받는 변수(for문 내에서 사용)
"""
print("hello")
print() # enter키가 자동 포함
print("world")
print("hello", end=" ") # 출력끝에 enter대신 " "가 포함

print()
nums = [0, 1, 2, 3, 4]
for num in nums:
    print(num, end=" ")

print()

# range(a, b) -> a이상 b미만
# ex) range(1, 5) -> [1, 2, 3, 4]
# range(n) == range(0, n) -> 0이상 n미만
nums = list(range(5)) # 리스트로 쓰려면 형변환
print(nums)

# range(10) -> [0,1,2,....9]
for num in range(10):
    print(num, end=" ")

for _ in range(5): # 요소가 필요없으면 "_"로 표현(관행)
    print("hello world")

# 1 ~ 50까지 홀수끼리, 짝수끼리 나누어 담아보자
odds, evens = [], [] # 튜플 언패킹
for num in range(1, 51):
    if num % 2 == 0:
        evens.append(num) # evens 리스트에 num추가
    else:
        odds.append(num)
print(evens)
print(odds)

# 1~50까지 홀수는 홀수끼리, 짝수는 짝수끼리
# 더하여서 각각 출력해주세요

even_sum, odd_sum = 0, 0 # 누적합변수 초기화
for num in range(1, 51):
    if num % 2 == 0:
        even_sum = even_sum + num
    else:
        odd_sum = odd_sum + num

print(f"짝수합:{even_sum} ,홀수합:{odd_sum}")

names = ["김지수", "김길동", "박철호", "박화목", "최영희"]
# 박 성씨인 이름들만 모아주세요
parks = []
count = 0
for name in names:
    # 내부적으로 name = names[0]
    # name = names[1]...
    if name[0] == "박":
        parks.append(name)
        count = count + 1
print(parks)
# 박 성씨인 이름이 몇개인지 출력
print(count)


files = ["report.pdf", "ad.exe", "setup.bat", "memo.txt"]
# for문으로 각 파일명을 확인하면서
# .exe파일로 끝나는 파일이 있으면, "위험한 파일입니다!" 출력
# endswith() 사용
for file in files:
    if file.endswith(".exe"):
        print("위험한 파일입니다!")


# banned_files에 기록되어있는 확장자로 끝나면 "위험한 파일입니다!" 출력
banned_files = [".exe", ".bat"]
files = ["report.pdf", "ad.exe", "setup.bat", "memo.txt"]
for file in files:
    # "."의 index를 찾는다
    dot_idx = file.index(".")
    # .부터 끝까지 슬라이싱
    ext = file[dot_idx:]
    # in연산자로 banned_files에 있는지 확인
    if ext in banned_files:
        print("위험한 파일입니다!")


# 2중 for문
# 바깥 반복 한번당 안쪽 반복 전체가 도는 구조

# 일주일
for day in range(1, 8):
    print(f"{day}일 살았습니다!", end=" ")

# 한달
for week in range(1, 5):
    print(f"{week}주 시작") # 4번
    # 일주일 # 4번
    for day in range(1, 8):
        print(f"{day}일 살았습니다!", end=" ") # 4 x 7번
    print() # 엔터
    print(f"{week}주 끝") # 4번

# 구구단(2~9단)
"""
2단시작!
    2 x 1 = 2
    2 x 2 = 4
    ...
    2 x 9 = 18
2단끝!
3단시작!
3 x 1 = 3...
3단끝!
.. 9단 끝!
"""

for dan in range(2, 10):
    print(f"{dan}단 시작!")
    for num in range(1, 10):
        print(f"{dan} x {num} = {dan * num}")
    print(f"{dan}단 끝!")


