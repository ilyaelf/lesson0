from threading import Thread,Lock
class BankAccount():
    def __init__(self):
        self.amount = 1000
    def deposit(self,deposit):
        with lock:
            self.amount += deposit
            print(f'deposited {deposit},new balance is {self.amount}')
            return self.amount
    def withdraw(self,withdraw):
        with lock:
            self.amount -= withdraw
            print(f'withdrew {withdraw}, new balance is {self.amount}')
            return self.amount


def deposit_task(account, amount):
  for _ in range(5):
    account.deposit(amount)

def withdraw_task(account, amount):
  for _ in range(5):
    account.withdraw(amount)
      
lock = Lock()
account = BankAccount()

deposit_thread = Thread(target=deposit_task, args=(account, 100))
withdraw_thread = Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()