# 객체지향 프로그래밍
# 데이터를 저장할때
# 안전하게 검증된 값만 저장하고 싶다.
# 검증된 값들과 동작을 묶고 싶다.


# 은행계좌 클래스
class BankAccount:
    def __init__(self, name):
        # 검증하는 코드 작성 가능
        self.name = name
        self.balance = 0 # 계좌개설시 무조건 0원

    def check_balance(self):
        print(f"{self.name}님의 잔액: {self.balance}")

    # 예금
    def deposit(self, amount):
        # amount가 숫자인지 검증
        self.balance += amount

    # 출금
    def withdraw(self, amount):
        if amount > self.balance:
            print("잔액부족!")
            return

        # 검증 이후에 객체에 담긴 데이터를 조작할 수 있다.
        # 객체에 담긴 데이터는 언제나 신뢰가능하다.
        self.balance -= amount

acc1 = BankAccount("홍길동") # 홍길동 계좌생성
acc2 = BankAccount("김길동") # 김길동 계좌생성

acc1.deposit(10000)
acc2.deposit(5000)

acc1.withdraw(6000)
acc2.withdraw(6000)

acc1.check_balance()
acc2.check_balance()

# Cup 클래스
# 필드: size(최대용량), water(현재물의양) - 생성시 0
# 함수:
# fill(self, amount) - size를 넘어가면 안됨
# drink(self, amount) - water를 넘어가면 안됨
# check(self): 현재물의 양 출력

class Cup:
    def __init__(self, size):
        self.size = size
        self.water = 0

    def check(self):
        print(f"현재 물의양: {self.water}ml")

    def fill(self, amount):
        if self.water + amount > self.size:
            print("물이 넘칩니다!!")
            return

        self.water += amount

    def drink(self, amount):
        if amount > self.water:
            print("물이 부족합니다!")
            return

        self.water -= amount



class Player:
    def __init__(self, _nickname, hp=100):
        self._nickname = _nickname
        self.hp = hp

    def change_nickname(self, new_name):
        self._nickname = new_name

p1 = Player("홍길동")
# 필드명앞에 '_'붙히면 직접접근할때 경고창.
print(p1._nickname) # 객체정보에 접근
print(p1.hp) # 객체정보에 접근

# 직접 접근해서 변경까지 가능
p1._nickname = "김길동"
print(p1._nickname)

# 동적으로 객체에 필드를 추가 가능
p1.anything = "아무거나"
print(p1.anything)