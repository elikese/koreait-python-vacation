# 딕셔너리(dict)
# 리스트와 튜플은 index(숫자)로 데이터를 보관
# 딕셔너리는 라벨(데이터)-key 로 데이터-value를 보관
mr_park = {
    "이름": "박철수",
    "나이": 30,
    "성별": "남자",
    "취미": ["코딩", "쇼핑", "음악감상"]
}

# 생성자방식
mr_park = dict(
    이름 = "박철수",
    나이 = 30,
    성별 = "남자",
    취미 = ["코딩", "쇼핑", "음악감상"]
)
# key는 중복x, 불변자료형은 key로 사용가능

# 요소접근(읽기)
print(mr_park["이름"]) # 직접접근, key가없으면 에러
print(mr_park.get("이름")) # 간접접근, key가없으면 None

# 추가, 수정
# 있었던 key에 value를 대입하면 수정
# 없어던 key에 value를 대입하면 추가
mr_park["나이"] = 31
mr_park["직장"] = "학교"

# 추가수정 한번에
mr_park.update({
    "나이": 32, # 수정
    "국적": "대한민국" # 추가
})

# 요소 제거
name = mr_park.pop("이름") # 꺼내온다
del mr_park["국적"] # 삭제

# 실습)
menu = {
    "김밥": 3000,
    "라면": 4000,
    "돈까스": 7000
}
# menu에 떡볶이 5000원을 추가 -> 추가
# 라면가격을 5000으로 인상 -> 수정
# 김밥과 라면을 먹었을때 내야할 금액을 출력
menu.update({
    "떡볶이": 5000, # "떢볶이" key 없었음 -> value 추가
    "라면": 5000 # "라면" key 있었음 -> value 수정
})
print(menu["김밥"] + menu["라면"])

# dict와 in연산자 -> key가 있는지 검사
print("김밥" in menu)
print("라면" in menu)
# len
print(len(menu)) # 데이터 총 갯수

tel_book = {
    "김철수": "010-1111-1111",
    "박철수": "010-2222-1111",
    "이철수": "010-3333-1111",
}
# key들만 모아보자
# ["김철수", "박철수"...]
names = tel_book.keys()
names = list(names) # 형변환하여 재대입

# value들만 모아보자
tels = tel_book.values()
tels = list(tels)

# items(): (key, value) 쌍을 튜플로 묶어서 리스트로 만들어줌
print(tel_book.items())
# [(k,v), (k,v)... (k,v)]

# key로 tuple을 사용할 수 있다.
coord_data = {
    (5, 10): "맛집1",
    (10, 10): "맛집2",
    (15, 10): "맛집3",
    (5, 20): "맛집4",
}
# (15, 10)좌표가 맛집인지 확인하는 조건문을 작성
# if문 + in연산자, 맛집이면 이름출력
if (15, 10) in coord_data:
    print(coord_data[(15, 10)])
