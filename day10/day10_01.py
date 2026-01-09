# file 입출력
# 메모리(ram) -
# 실행도중에만 데이터 존재(칠판에 적었다가 지운다)
# 파일(HDD / SSD) -
# 반영구적으로 존재(노트에 적어서 보관)

file = open("./example.txt", "w", encoding="utf-8")
file.write("Hello world!")
file.close()

# open(파일경로, 파일모드, 인코딩)
"""
- 경로(절대경로, 상대경로)
절대경로(드라이브부터 실제 파일위치까지)
c:/koreait-python-vacation/day10/day10_01.py

상대경로(../, ./)
../: 현재 파일위치에서 한단계 상위 폴더
./: 현재파일이 속한 폴더

day10_01.py는 "./example.txt" 상대경로로 접근할 수 있다.
day10_01.py는 "../day09/함수심화.py" 상대경로로 접근할 수 있다.

- 파일모드
r: read
w: write

- 인코딩
컴퓨터는 숫자만 알아 들음
글자들을 숫자로 바꿔줘야함
이때 필요한 규칙(인코딩)
ascii(영어만), euc-kr(옛), cp949(옛), utf-8(웹표준)
"""

# 파일 읽기
# open이 리턴을 해주는건 실제 데이터가아니라 특수한 자료형
file = open("./example.txt", "r", encoding="utf-8")
my_text = file.read()
file.close() # 자료형 반납
print(my_text)

# day05폴더에 있는 test.txt파일을 읽어서 콘솔에 출력!
test_path = "../day05/test.txt"
test_file = open(test_path, "r", encoding="utf-8")
text_text = test_file.read()
print(text_text)
test_file.close() # 반납

# day01폴더 안에 test 폴더안에 있는 test2.txt 읽고 출력
test2_path = "../day01/test/test2.txt"
test2_file = open(test2_path, "r", encoding="utf-8")
test2_text = test2_file.read()
print(test2_text)
test2_file.close() # 반납

with open(test_path, "r", encoding="utf-8") as f:
    # with ~ as: 자동으로 자원 반납
    test2_text = f.read()
    print(test2_text)

# 문자열(txt)말고, python 자료형들을 저장할 파일형식이 필요함
# [{},{}...{}] 이런경우가 많다.
# 참고) csv, xml, yml
# JSON 파일형식 - 웹, 소프트웨어에서 데이터를 주고받는 용도
"""
{
    "name": "홍길동",
    "age": 30,
    "is_student": False
}
"""

dict_data = {
    "name": "홍길동",
    "age": 30,
    "is_student": False
}

import json # 코드 빌려오기

# json파일 쓰기
# "w"는 덮어쓰기
with open("./data.json", "w", encoding="utf-8") as f:
    # json.dump(파이썬데이터, f(파일), 아스키, 들여쓰기)
    # 아스키: 한글이 포함되면 False로 지정
    # 들여쓰기: 4칸 들여쓰겠다.
    json.dump(dict_data, f, ensure_ascii=False, indent=4)

# json파일 불러오기
with open("./data2.json", "r", encoding="utf-8") as f:
    new_dict_data = json.load(f)
    print(new_dict_data)

# menu.json에 메뉴가 존재합니다
# 해당 메뉴를 불러와서 "떡볶이: 5000원" 추가
# 라면가격을 5000원으로 인상하여
# 다시 menu.json으로 저장해주세요

# menu.json 불러오기
with open("./menu.json", "r", encoding="utf-8") as f:
    menu_data = json.load(f)

# dict 수정하기
menu_data["떡볶이"] = 5000 # 없던key -> 추가
menu_data["라면"] = 5000 # 있던key -> value 수정

menu_data.update({
    "떡볶이": 5000,
    "라면": 5000
})

# menu.json 덮어쓰기
with open("./menu.json", "w", encoding="utf-8") as f:
    json.dump(menu_data, f, ensure_ascii=False, indent=4)


# 함수: 반복되는 코드저장

# json 불러오기 함수
def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        json_data = json.load(f)
        return json_data

load_json("./menu.json")

# json 저장하기 함수
def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

nums = [1,2,3,4,5]
save_json("./nums.json", nums)
print(load_json("./nums.json"))