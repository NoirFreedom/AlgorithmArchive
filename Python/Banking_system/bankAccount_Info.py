# -*- coding: utf-8 -*-
"""mainQuest01.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YPpqU0ngG18VRt5I0GjwWtKjMl6x7iJJ
"""

import random as r
import time as t


# Q1. Account 클래스 : 은행에 가서 계좌를 개설하면 은행이름, 예금주, 계좌번호, 잔액이 설정됩니다.
#     Account 클래스를 생성한 후 생성자(hint: 매직매서드..!!)를 구현해보세요. 생성자에서는 예금주와 초기 잔액만 입력 받습니다.
#     은행이름은 SC은행으로 계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성됩니다. (은행이름: SC은행, 계좌번호: 111-11-111111)
class Account:
  deposit_count = 0 # 이자 조건충족 확인을 위해 해당함수 내부가 아닌 인스턴스 변수를 정의함.
  cls_total_account_num = 1 # 클래스 변수를 사용해서 Account 클래스로부터 생성된 계좌 객체의 개수를 세기위함
  total_account_num = [] # Account 클래스로부터 생성된 계좌의 개수를 출력하는 get_account_num() 메서드를 사용하기 위한 리스트


  def __init__(self, bank_name, holder, balance):
    self.bank_name = bank_name     #클래스 변수사용 - 속성값 할당
    self.holder = holder
    self.ac_num = self.generate_account_num() # generate_account_num()로 계좌번호 생성 후 할당
    self.balance = balance
    self.deposit_transactions = [] # 임금액을 담기위한 인스턴스 변수의 리스트
    self.withdraw_transactions = [] # 출금액을 담기위한 인스턴스 변수의 리스트
    self.cls_total_account_num += 1



  def generate_account_num(self):
    ac_num = f"{r.randint(100,999)}-{r.randint(10,99)}-{r.randint(100000,999999)}" # 계좌번호 부여 | random모듈의 randint메소드를 사용하여 임의의 정수 추출
    return ac_num



# Q3. 클래스 변수 출력 : Account 클래스로부터 생성된 계좌의 개수를 출력하는 get_account_num() 메서드를 추가하세요.
  def get_account_num(self):
    len(self.total_account_num)


# Q4. 입금 메서드 : Account 클래스에 입금을 위한 deposit 메서드를 추가하세요. 입금은 최소 1원 이상만 가능합니다.
  def deposit(self):
    d = 0
    while d <= 0: # 0보다 큰 값이 할당 될 동안 아래 input을 출력
      d = int(input("입금하실 금액을 입력하세요 : "))
      self.balance += d # 계좌 잔액에 입력받은 금액을 더함
      print(f"{d}원이 입력되었습니다")
      print("입금 후 잔액 :" , self.balance, "원")
      self.deposit_count += 1 # 이자계산을 위한 count
      self.deposit_transactions.append(d) # 입금내역 확인을 위해 해당 리스트에 append함

    # Q7. 이자 지급하기: 입금 횟수가 5회가 될 때 잔고를 기준으로 1%의 이자가 잔고에 추가되도록 코드를 변경해보세요.
    if self.deposit_count >= 5: # 이자 count가 5와같거나 초과될 시
      interest = int(self.balance * 0.01) # 이자는 총금액에 1%
      self.balance += interest # 이자를 계좌잔액 더함
      print(f"이자 {interest}가 지급 되었습니다.")
      self.deposit_count == 0 # 이자지급완료, 다시 0으로 초기화함




# Q5. 출금 메서드 : Account 클래스에 출금을 위한 withdraw 메서드를 추가하세요. 출금은 계좌의 잔고 이상으로 출금할 수는 없습니다.
  def withdraw(self):
    w = 0
    while w <= 1 or w > self.balance:
      w = int(input("출금하실 금액을 입력하세요 "))
      if w > self.balance:
        print("잔액이 부족합니다")
        t.sleep(1)
    self.balance -= w
    print("출금 후 잔액 :" , self.balance, "원")
    self.withdraw_transactions.append(w)


    # Q10. 입출금 내역
    # 입금과 출금 내역이 기록되도록 코드를 업데이트 하세요.
    # 입금 내역과 출금 내역을 출력하는 deposit_history와 withdraw_history 메서드를 추가하세요.

  def deposit_history(self):
    for i in self.deposit_transactions:
      print(f"입금된 금액 : {i} 원")

  def withdraw_history(self):
    for i in self.withdraw_transactions:
      print(f"출금된 금액 : {i} 원")




# Q6. 정보 출력 메서드 : Account 인스턴스에 저장된 정보를 출력하는 display_info() 메서드를 추가하세요. 잔고는 세자리마다 쉼표를 출력하세요.
# (은행이름: SC은행, 예금주: 파이썬, 계좌번호: 111-11-111111, 잔고: 10,000원)

  def display_info(self):
    return f"Millionaire은 {self.bank_name},{self.holder},{self.ac_num},{self.balance} 입니다!!"



# Q9. 객체 순회 반복문을 통해 리스트에 있는 객체를 순회하면서 잔고가 100만원 이상인 고객의 정보만 출력하세요.
def find_milion():
  for account in total_account: # 아래 정의한 변수에 Account클래스로 생성된 객체들을 담고, 각 객체들의 balance를 조사함
    if account.balance > 1000000:
      print(account.display_info())



print(f"계좌번호는 {account.ac_num} 입니다")
print(f"현재 잔액은 {account.balance}원 입니다")

# Q2. 클래스 변수: 클래스 변수를 사용해서 Account 클래스로부터 생성된 계좌 객체의 개수를 저장하세요.
print(f"현재까지 계설된 계좌는 총 {Account.cls_total_account_num}개 입니다")




account = Account('SC_BANK', 'anonymous', 10000000000)

# Q8. 여러 객체 생성 Account 클래스로부터 3개 이상 인스턴스를 생성하고 생성된 인스턴스를 리스트에 저장해보세요.
account1 = Account('SHINHAN_BANK','anonymous1',1000000000)
account2 = Account('KOOKMIN_BANK', 'anonymous2', 20000)
account3 = Account('WOORI_BANK', 'anonymous3', 30000)

total_account = [account1, account2, account3]




account.get_account_num()
account.deposit()
account.withdraw()
account.display_info()
find_milion()
account.deposit_history()
account.withdraw_history()