# 매직 메서드
# 파이썬의 거의 대부분은 클래스로부터 만들어진 객체다

# 모든 클래스의 공통 조상 -> object클래스
# object를 상속받고 있다면, object의 메서드를 호출할수있다.

# object 상속은 생략가능
# Person() -> __init__ 호출됨
class Person(object):
    # __어쩌고__() -> 매직메서드
    # object에 정의되어있던 __init__() 오버라이드하고 있었음
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self): # 객체를 출력할때(문자열화)
        return f"이름={self.name}, age={self.age}"

    def __eq__(self, other): # == 연산시 호출
        if isinstance(other, Person):
            return self.age == other.age
        elif isinstance(other, int):
            return self.age == other

    # less than -> __lt__ -> "<"
    # greater than -> __gt__ -> ">"
    # less than or equal -> __le__ -> "<="
    # greater than or equal -> __ge__ -> ">="
    def __lt__(self, other): # < 연산시 호출
        print("나이 비교")
        if isinstance(other, Person):
            return self.age < other.age
        elif isinstance(other, int):
            return self.age < other

    # + 연산시, 나이를 더한 Person객체가 나오길 바람
    # + 연산 -> __add__()
    # - 연산 -> __sub__()
    # * 연산 -> __mul__()
    # / 연산 -> __div__()
    def __add__(self, other):
        if isinstance(other, int):
            new_age = self.age + other
            name = self.name
            # 제3의 객체를 리턴
            return Person(name, new_age)

p1 = Person("홍길동", 20)
p2 = Person("김길동", 20)
print(p1 == p2)
print(p1 < 30)
p3 = p1 + 5
print(p3) # 리턴받은 제3의 객체
print(p1)

# 좌표 클래스
class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # 같은 Coord 객체끼리
    # == 연산시 x, y좌표 동일하면 true
    def __eq__(self, other):
        if isinstance(other, Coord):
            is_same_x = self.x == other.x
            is_same_y = self.y == other.y
            return is_same_x and is_same_y
    # + 연산시, x좌표 y좌표가 각각 더해지게
    def __add__(self, other):
        if isinstance(other, Coord):
            new_x = self.x + other.x
            new_y = self.y + other.y
            return Coord(new_x, new_y)
    # - 연산시, x좌표 y좌표가 각각 빼지도록
    def __sub__(self, other):
        if isinstance(other, Coord):
            new_x = self.x - other.x
            new_y = self.y - other.y
            return Coord(new_x, new_y)
    # 객체출력시, "현재좌표: ({x좌표}, {y좌표})"
    def __str__(self):
        coord_str = f"현재좌표: ({self.x},{self.y})"
        return coord_str

c1 = Coord(1, 2)
c2 = Coord(1, 2)
c3 = Coord(2, 4)
print(c1 == c2)
print(c1 == c3)
print((c1 + c2) == c3)
print(c1 + c2)
print(c1 - c3)

print("hi" * 50) # str 클래스에서 __mul__을 오버라이딩한거였음
print([1,2,3] + [4,5,6]) # list 클래스에서 __add__ 오버라이딩