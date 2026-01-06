# 반복문 - while문
# for문 - 반복횟수가 정해져 있는 경우
# while문 - 반복횟수를 정확히 알수 없는 경우
"""
while 조건식(bool자료형):
    반복할 코드 작성
    * 조건을 변경해주는 코드 포함되어야 한다
"""

number = 5
while number > 0:
    print(f"현재 숫자:{number}") # 실행할코드
    number -= 1 # 조건을 변경할 코드

# break로 탈출하는 형태
number = 5
while True:
    if number == 0:
        break # 0이되면 break 밟고 탈출
    print(f"현재 숫자: {number}")
    number -= 1

# flag로 탈출하는 형태
number = 5
my_flag = True
while my_flag:
    if number == 0:
        my_flag = False
    # 아래의 코드모두 실행되고 다음반복에 탈출
    print(f"현재 숫자: {number}")
    number -= 1

# 조건중심의 반복문
# 비밀번호를 3회 초과시 "문이 잠겼습니다"출력->탈출
# 매 시도마다 남은 시도횟수를 출력해주세요
password = "123123"
max_trial_count = 3 # 최대 시도횟수
trial_count = 0 # 시도횟수
while True:
    left_trial_count = max_trial_count - trial_count
    print(f"남은 시도횟수: {left_trial_count}")
    my_input = input("비밀번호 입력 >")
    trial_count += 1
    if my_input == password:
        print("문이 열렸습니다.")
        break

    if trial_count == max_trial_count:
        print("문이 잠겼습니다.")
        break

    print("비밀번호를 다시 입력하세요")

